# -*- coding: utf-8 -*-
##############################################################################
#
#    odoo, Open Source Management Solution
#    Copyright (C) 2004-today odoo SA (<http://www.odoo.com>)
#
#    Module is copyrighted by OpenGLOBE (www.openglobe.pl) and Cirrus (www.cirrus.pl)
#    with the same rules as OpenObject and Odoo.
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

import json
import logging
from pprint import pprint
from collections import defaultdict
from functools import partial
from datetime import datetime

from odoo.exceptions import UserError
from odoo import models, fields, api, _
# from odoo.tools import amount_to_text_en
from odoo.tools import float_is_zero
from odoo.tools.misc import formatLang, format_date, get_lang

_logger = logging.getLogger(__name__)


class AccountMove(models.Model):
    _inherit = 'product.template'

    
    def get_all_products(self):
        query = """
            SELECT id, name
            FROM res_partner
            WHERE active = TRUE
            ORDER BY name
        """
        
        cr = self.env.cr
        cr.execute(query)
        result = cr.fetchall()
        
        return result