# -*- coding: utf-8 -*-
##############################################################################
#
# Copyright (C) 2011-2014 OpenERP - Team de Localización Argentina.
# https://launchpad.net/~openerp-l10n-ar-localization
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program. If not, see <http://www.gnu.org/licenses/>.
#
#############################################################################

from osv import fields,osv
from tools.translate import _
import time

from banks_def import *

class l10n_ar_banks_wizard(osv.osv_memory):
    _name = 'l10nar.banks.wizard'

    def on_cancel(self, cr, uid, ids, context):
	    return {}
   
    def on_process (self, cr, uid, ids, context): 
	"""
	    Tomo los datos de los banco de BCRA. 
	"""
	Resultados={}
	bancos_procesados = 0
	bancos_actualizados = 0
	bancos_nuevos = 0
	bancos_desahabilitados = 0
	
	update_date = time.strftime('%Y-%m-%d')
	idargentina = self.pool.get('res.country').search(cr, uid, [('name', '=', 'Argentina')])[0]
	idbuenosaires = self.pool.get('res.country.state').search(cr, uid, [('name', '=', 'Buenos Aires')])[0]
	idciudadbuenosaires = self.pool.get('res.country.state').search(cr, uid, [('name', '=', 'Ciudad Autónoma de Buenos Aires')])[0]
	Bancos_obj = self.pool.get('res.bank')

	TodosLosBancosArgentinos = Bancos_obj.search(cr, uid, [('country', '=', idargentina)])  
	self.pool.get('res.bank').write(cr, uid, TodosLosBancosArgentinos, {'active': False}, context=context)
	bancos_desahabilitados = len(TodosLosBancosArgentinos)
	
	for bank in ar_banks_iterator():	    	    
	    bancos_procesados += 1
	    vals={}	    
	    for key in bankfields:
		if key in bank:
		    valor=bank[key]
		    if key == 'country' : 
			valor=idargentina
		    if key == 'state' : 
			if bank[key] == 'Buenos Aires':
			    valor = idbuenosaires
			elif bank[key] == 'Autonomous City of Buenos Aires':
			    valor = idciudadbuenosaires
			else: 
			    valor = self.pool.get('res.country.state').search(cr, uid, [('name', '=', bank[key])])[0]
		    vals.update({key:valor})
	    
	    vals.update({'update' : time.strftime('%Y-%m-%d')})
	       
	    Bancos_ids = Bancos_obj.search(cr, uid, [('name', '=', bank.get('name')),('country', '=', idargentina),('active', '=', False)])
	    if not(Bancos_ids):
		Bancos_ids = Bancos_obj.search(cr, uid, [('vat', '=', bank.get('vat')), ('country', '=', idargentina),('active', '=', False)])
		if not(Bancos_ids):
		    Bancos_ids = Bancos_obj.search(cr, uid, [('street', '=', bank.get('street')), ('city', '=', bank.get('city')), ('country', '=', idargentina),('active', '=', False)])		
		    
	    if Bancos_ids:
		bancos_desahabilitados -= 1
		bancos_actualizados += 1
		self.pool.get('res.bank').write(cr, uid, [Bancos_ids[0]], vals, context=context)
	    else:
		bancos_nuevos += 1
		self.pool.get('res.bank').create(cr, uid, vals, context=context)

	Resultados.update({'bancos_procesados' : bancos_procesados})
	Resultados.update({'bancos_actualizados' : bancos_actualizados})
	Resultados.update({'bancos_nuevos' : bancos_nuevos})
	Resultados.update({'bancos_desahabilitados' : bancos_desahabilitados})
        
	return {
		'view_type': 'form',
		'view_mode': 'form',
		'context': Resultados,
		'res_model': 'l10nar.banks.wizard.result',
		'type': 'ir.actions.act_window',
		'target': 'new'
	    }    
 
l10n_ar_banks_wizard()


class l10n_ar_banks_wizard_result(osv.osv_memory):
    _name = 'l10nar.banks.wizard.result'

    def _get_bancos_actualizados(self, cr, uid, context=None):
	if context is None:
	    context = {}
	valor = context.get('bancos_actualizados')
        return valor
        
    def _get_bancos_nuevos(self, cr, uid, context=None):
	if context is None:
	    context = {}
	valor = context.get('bancos_nuevos')
        return valor

    def _get_bancos_desahabilitados(self, cr, uid, context=None):
	if context is None:
	    context = {}
	valor = context.get('bancos_desahabilitados')
        return valor

    def _get_bancos_procesados(self, cr, uid, context=None):
	if context is None:
	    context = {}
	valor = context.get('bancos_procesados')
        return valor

    _columns = {
		  'bancos_actualizados' : fields.char(_('Banks Upgraded'), size=3),
		  'bancos_nuevos' : fields.char(_('New Banks'), size=3),
		  'bancos_desahabilitados' : fields.char(_('Desactivated Banks'), size=3),
		  'bancos_procesados' : fields.char(_('Banks total processed'), size=3),
		}
    _defaults = {
		  'bancos_actualizados' : _get_bancos_actualizados,
		  'bancos_nuevos' : _get_bancos_nuevos,
		  'bancos_desahabilitados' : _get_bancos_desahabilitados,
		  'bancos_procesados' : _get_bancos_procesados,
		}
   
    def on_close(self, cr, uid, ids, context):
	    return {}
      
l10n_ar_banks_wizard_result()