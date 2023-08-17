# -*- coding: utf-8 -*-

from odoo import api, fields, models, _
import logging

_logger = logging.getLogger(__name__)

class AllProductsReportWizard(models.TransientModel):
    _name = "all.products.report.wizard"
    _description = "Create Appointment Wizard"

    date_from = fields.Date(string="Date From")
    date_to = fields.Date(string="Date To")

    def get_all_products(self, date_from, date_to):
        query = """
            SELECT name, list_price
            FROM product_template
            ORDER BY name
        """
        
        cr = self.env.cr
        cr.execute(query)
        result = cr.fetchall()
        
        _logger.warning(f"@@@@@@@@@@@@@@@@@@@@@ LOGGER RW: resutl: {result} @@@@@@@@@@@@@@@@@@@@@@@@@@@@")
        return result

    def action_print_report(self):
        # products = self.env['product.template'].search([]).mapped('name')

        date_from = self.read()[0]['date_from']
        date_to = self.read()[0]['date_to']
        products = self.get_all_products(date_from, date_to)
        _logger.warning(f"@@@@@@@@@@@@@@@@@@@@@@@ LOGGER RW: products - {products}")
        data = {
            'products': products,
            # 'form_data': self.read()[0],
            'date_from': date_from,

        }
        return self.env.ref('sales_analysis_rw.action_all_products_report_print').report_action(self, data=data)