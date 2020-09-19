import frappe
from functools import wraps
from markd.markd.search import BookmarkSearch

def check_demo():
	if frappe.session.user == "Guest":
		if not frappe.db.get_single_value("Markd Settings", "enable_demo_mode"):
			raise frappe.PermissionError

@frappe.whitelist(allow_guest=True)
def get_bookmarks():
	check_demo()
	marks = frappe.get_all("Bookmark", limit=20)
	return [frappe.get_doc("Bookmark", mark['name']) for mark in marks]

@frappe.whitelist()
def save_mark(url):
	mark = frappe.new_doc("Bookmark")
	mark.url = url
	mark.insert()
	return mark

@frappe.whitelist()
def delete_mark(mark):
	mark = frappe.delete_doc("Bookmark", mark)

@frappe.whitelist(allow_guest=True)
def search(query, limit=10):
	check_demo()
	limit = frappe.utils.cint(limit)
	ws = BookmarkSearch(index_name="bookmark-index")
	return ws.search(query, limit=limit)