# -*- coding: utf-8 -*-

from odoo import api, fields, models, _
import logging

_logger = logging.getLogger(__name__)

class SalesByProductsReportWizard(models.TransientModel):
    _name = "sales.by.products.report.wizard"
    _description = "Create Sales Ranking Wizard"

    date_from = fields.Date(string="Date From", default=datetime.today())
    date_to = fields.Date(string="Date To", default=datetime.today())

    def get_all_products(self, date_from, date_to):
        #napisac mehcanizm zamiany date_to z date_from jeżeli są date_to < date_from
        if date_from > date_to:
            buffer1 = date_to
            buffer2 = date_from
            date_from = buffer1
            date_to = buffer2

        date_from = "'" + str(date_from) + "'"
        date_to = "'" + str(date_to) + "'"


        query = f"""
            SELECT 
                pt.name, 
                SUM(aml.price_subtotal) as total_price_subtotal,
                SUM(aml.quantity) as qty 
            FROM account_move am
            JOIN account_move_line aml ON am.id = aml.move_id
            JOIN product_product pp ON aml.product_id = pp.id
            JOIN product_template pt ON pp.product_tmpl_id = pt.id
            WHERE am.move_type = 'out_invoice' AND am.state='posted' AND am.invoice_date >= {date_from} AND am.invoice_date <= {date_to}
            GROUP BY pt.name
            ORDER BY total_price_subtotal DESC;
        """
        
        cr = self.env.cr
        cr.execute(query)
        result = cr.fetchall()        
        _logger.warning(f"@@@@@@@@@@@@@@@@@@@@@ LOGGER RW: resutl: {result} @@@@@@@@@@@@@@@@@@@@@@@@@@@@")
        return result


    def action_print_report(self):
        date_from = self.read()[0]['date_from']
        date_to = self.read()[0]['date_to']
        products = self.get_all_products(date_from, date_to)
        data = {
            'products': products,
            'date_from': date_from,
            'date_to': date_to,
        }
        return self.env.ref('sales_analysis_rw.action_sales_by_products_report_print').report_action(self, data=data)
        