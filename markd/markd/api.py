import frappe

@frappe.whitelist(allow_guest=True)
def hello():
	return "Yo"

@frappe.whitelist()
def get_bookmarks():
	marks = frappe.get_all("Bookmark", limit=20)
	return [frappe.get_doc("Bookmark", mark['name']) for mark in marks]