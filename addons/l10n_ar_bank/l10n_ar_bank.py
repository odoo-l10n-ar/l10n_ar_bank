# -*- coding: utf-8 -*-
from openerp.osv import fields,osv
from openerp.tools.translate import _
import time

class Bank(osv.osv):
    _inherit = 'res.bank'
    _columns = {
        'vat': fields.char(_('VAT'),size=32 ,help="Value Added Tax number."),
    }

Bank()
# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
