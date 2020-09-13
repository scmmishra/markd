import frappe
from markd.markd.search import BookmarkSearch

@frappe.whitelist(allow_guest=True)
def hello():
	return "Yo"

@frappe.whitelist()
def get_bookmarks():
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

@frappe.whitelist()
def mark_search(query, limit=10):
	limit = frappe.utils.cint(limit)
	ws = BookmarkSearch(index_name="bookmark-index")
	return ws.search(query, limit=limit)