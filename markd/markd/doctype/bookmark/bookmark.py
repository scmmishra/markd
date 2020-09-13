# -*- coding: utf-8 -*-
# Copyright (c) 2020, Shivam Mishra and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import requests
import urllib
from urllib.parse import urlparse
from readability import Document as RDoc
from bs4 import BeautifulSoup

import frappe
from frappe.utils.file_manager import save_file_on_filesystem
from frappe.model.document import Document

from markd.markd.search import add_item, remove_item

class Bookmark(Document):
	def before_save(self):
		response = requests.get(self.url)
		meta = self.fetch_url_meta(response)
		self.meta_title = meta.title
		self.description = meta.description
		self.website = urlparse(self.url).netloc

		image = meta.image or meta.get("og:image") or meta.get("twitter:image")
		self.image = self.save_file(image)
		self.readable = self.get_readable(response)
		self.favicon = self.fetch_favicon(response)

	def after_insert(self):
		add_item(self.name)

	def on_trash(self):
		remove_item(self.name)

	def fetch_url_meta(self, response):
		soup = BeautifulSoup(response.text, features="lxml")
		metas = soup.find_all('meta')
		all_meta = { meta.attrs['name']:meta.attrs['content'] for meta in metas if 'name' in meta.attrs }

		title = soup.find('title')
		if title:
			all_meta['title'] = title.text

		return frappe._dict(all_meta)

	def fetch_favicon(self, response):
		soup = BeautifulSoup(response.text, features="lxml")
		icon_link = soup.find("link", rel="icon")
		if not icon_link:
			return
		icon_link = icon_link['href']
		netloc = urlparse(self.url).netloc
		if netloc not in icon_link:
			icon_link = 'https://' + netloc + icon_link

		return self.save_file(icon_link)

	def get_readable(self, response):
		doc = RDoc(response.text)
		return doc.summary()

	def save_file(self, url):
		if not url:
			return
		urlfile = urllib.request.urlopen(url)
		name = self.name + frappe.utils.random_string(8) + '.' + url.split('.')[-1].split('?')[0]
		ico_file = save_file_on_filesystem(name, urlfile.read())
		return ico_file.get('file_url')