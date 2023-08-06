# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import api, fields, models, _
from odoo.exceptions import AccessError, UserError
from pprint import pprint

import logging
_logger = logging.getLogger(__name__)


class User(models.Model):
    _inherit = 'res.users'
    
    # gender1 = fields.Many2one('res.partner.gender', string='Gender')
    
    
    
    
   