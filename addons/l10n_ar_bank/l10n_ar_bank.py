# -*- coding: utf-8 -*-
from openerp.osv import fields,osv
from openerp.tools.translate import _
import time

class Bank(osv.osv):
    _inherit = 'res.bank'
    _columns = {
		  'update' : fields.date(_('Update')),
		  'vat': fields.char(_('VAT'),size=32 ,help="Value Added Tax number."),
		}
    _defaults = {
		  'update': lambda *a: time.strftime('%Y-%m-%d')
		}
Bank()
