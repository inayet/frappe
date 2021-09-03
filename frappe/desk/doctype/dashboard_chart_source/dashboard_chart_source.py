# -*- coding: utf-8 -*-
# Copyright (c) 2019, Frappe Technologies and contributors
# License: MIT. See LICENSE

import frappe, os
from frappe import _
from frappe.model.document import Document
from frappe.modules.export_file import export_to_files
from frappe.modules import get_module_path, scrub


@frappe.whitelist()
def get_config(name):
	doc = frappe.get_doc('Dashboard Chart Source', name)
	with open(os.path.join(get_module_path(doc.module),
		'dashboard_chart_source', scrub(doc.name), scrub(doc.name) + '.js'), 'r') as f:
		return f.read()

class DashboardChartSource(Document):
	def on_update(self):
		export_to_files(record_list=[[self.doctype, self.name]],
			record_module=self.module, create_init=True)
