import frappe
from frappe.search.full_text_search import FullTextSearch
from frappe.utils import strip_html_tags
from whoosh.fields import TEXT, ID, Schema

class BookmarkSearch(FullTextSearch):
	def get_items_to_index(self):
		all_docs = []
		marks = frappe.get_all("Bookmark", fields=["name", "readable"])
		for mark in marks:
			all_docs.append({
				'name': mark.name,
				'title': mark.meta_title,
				'content': strip_html_tags(mark.readable)
			})
		return all_docs

	def get_schema(self):
		return Schema(
			title=TEXT(stored=True), name=ID(stored=True), content=TEXT(stored=True)
		)

	def get_document_to_index(self, name):
		mark = frappe.get_doc("Bookmark", name)
		return {
			'name': mark.name,
			'content': strip_html_tags(mark.readable)
		}

	def parse_result(self, result):
		content_highlights = result.highlights("content")

		return frappe._dict(
			name=result["name"],
			content_highlights=content_highlights,
			doc=frappe.get_doc("Bookmark", result["name"])
		)

def build():
	bms = BookmarkSearch("bookmark-index")
	bms.build()

def add_item(name):
	bms = BookmarkSearch("bookmark-index")
	return bms.update_index_by_name(name)

def remove_item(name):
	bms = BookmarkSearch("bookmark-index")
	return bms.remove_document_from_index(name)