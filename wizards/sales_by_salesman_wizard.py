# -*- coding: utf-8 -*-

from odoo import api, fields, models, _
import logging
from datetime import datetime

_logger = logging.getLogger(__name__)

class SalesBySalesmanReportWizard(models.TransientModel):
    _name = "sales.by.salesman.report.wizard"
    _description = "Create Sales Ranking Wizard"

    date_from = fields.Date(string="Date From", default=datetime.today())
    date_to = fields.Date(string="Date To", default=datetime.today())

    def get_all_salesman(self, date_from, date_to):
        #napisac mehcanizm zamiany date_to z date_from jeżeli są date_to < date_from
        if date_from > date_to:
            buffer1 = date_to
            buffer2 = date_from
            date_from = buffer1
            date_to = buffer2

        date_from = "'" + str(date_from) + "'"
        date_to = "'" + str(date_to) + "'"


        query = f"""
            select rp.name,
            SUM(am.amount_untaxed) as revenue
            from account_move am 
            join res_users ru on am.invoice_user_id = ru.id 
            join res_partner rp on ru.partner_id = rp.id
            WHERE am.move_type = 'out_invoice' AND am.state='posted' AND am.invoice_date >= {date_from} AND am.invoice_date <= {date_to}
            GROUP BY rp.name
            ORDER BY revenue DESC;
;
        """
        
        cr = self.env.cr
        cr.execute(query)
        result = cr.fetchall()        
        _logger.warning(f"@@@@@@@@@@@@@@@@@@@@@ LOGGER RW: resutl: {result} @@@@@@@@@@@@@@@@@@@@@@@@@@@@")
        return result


    def action_print_report(self):
        date_from = self.read()[0]['date_from']
        date_to = self.read()[0]['date_to']
        salesmans = self.get_all_salesman(date_from, date_to)
        data = {
            'salesmans': salesmans,
            'date_from': date_from,
            'date_to': date_to,
        }
        return self.env.ref('sales_analysis_rw.action_sales_by_salesmans_report_print').report_action(self, data=data)
        