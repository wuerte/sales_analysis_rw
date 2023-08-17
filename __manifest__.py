# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

##############################################################################
#
#    OpenERP, Open Source Management Solution
#    Copyright (C) 2013-Today OpenERP SA (<http://www.openerp.com>).
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################

{
    'name': 'Sales Analysis RW',
    'category': 'base',
    "license": "AGPL-3",
    'summary': 'sales analysis and reports',
    'version': '16.0.1.0.00',
    'description': """
        Analysis for Sales module, like ranking of Customers, ranking of Salespersons etc.
        TO DO:
            -REPORT: ranking/summary of all PRODUCTs, most revenue, most profit, most quantity, most margin,
            -REPORT: of every PRODUCT: revenue in year, revenue, profit, quantity, margin, average discount
            -REPORT of every SALESPERSON: 
    """,
    'author': 'Radosław Wierzgała',
    'website': '',
    'depends': ['base', 'sale'],
    'data': [
        'security/ir.model.access.csv',
        'wizards/all_products_wizard.xml',
        'report/all_products_report.xml',
        'views/menu.xml',
    ],
    'installable': True,
    'sequence': 1,
    'application': False,
}