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

{
    'name': 'Banks of Argentina',
    'version': '4.1',
    'author': 'DINAmotion',
    'category': 'Localization/Argentina',
    'website': 'http://www.dinamotion.com.ar/',
    'license': 'GPL-3',
    'description': """
Part of localization Model for Argentina - Banks of Argentina

Includes: 
	  - Banks declared official at the Central Bank of Argentina (http://www.bcra.gov.ar/) at 08.18.2012 
	  - Online updater wizard.

Attention: To run the wizard you need to have installed two libraries in python: BeautifulSoup, geopy. Without these two libraries the wizard will fail and will not update the information.

--------------------------
(SPANISH)

includes:

  - Banks declared official at the Central Bank of Argentina (http://www.bcra.gov.ar/) day 18/08/2012
  - A wizard online updater.

Attention: To run this wizard you need to have installed two libraries in python: BeautifulSoup, geopy. Without these two libraries the wizard will fail and will not update the information.

""",
    'depends': [
		  'base',
		  'l10n_ar_states',
		],
    'init_xml': [],
    'demo_xml': [],
    'update_xml': [
		      'data/res_bank.xml',
		      'l10n_ar_bank.xml',
		      'l10n_ar_bank_menu.xml',
		      'wizard/wiz_l10n_ar_bank.xml',
		  ],
    'active': False,
    'installable': True,
}
