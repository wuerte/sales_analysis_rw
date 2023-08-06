# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import api, fields, models, _
from odoo.exceptions import AccessError, UserError
from pprint import pprint

import logging
_logger = logging.getLogger(__name__)


class SaleArea(models.Model):
    _name = 'sale.area'
    
    name = fields.Char('Sales Area', help="sale area")
    description = fields.Char('Sales Area Description', help="description of sales area")
    
    
    
    
   