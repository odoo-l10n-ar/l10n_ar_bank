# -*- coding: utf-8 -*-
##############################################################################
#
# Copyright (C) 2012 OpenERP - Team de Localización Argentina.
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
##############################################################################
{
    'name':     'Banks of Argentina',
    'version':  '2.7.155',
    'author':   'OpenERP - Team de Localización Argentina',
    'category': 'Localization/Argentina',
    'website':  'https://launchpad.net/~openerp-l10n-ar-localization',
    'license':  'AGPL-3',
    'description': """\
Part of localization Model for Argentina - Banks of Argentina

--------------------------
(SPANISH)

Listado de entidades financieras habilitadas por el BCRA.

Este módulo le permite tener a disposición el listado actualizado de
las entidades bancarias de la República Argentina.

Incluye:
 - Entidades financieras (http://www.bcra.gov.ar/)
 - Asistente de actualización de bancos.

Requiere:
	BeautifulSoup
	geopy

Para que el asistente funcione debe tener instalada ambos módulos de python.

Instalación de los requerimientos:

	$ pip install BeautifulSoup
	$ pip install geopy

ejecutar desde la linea de comandos.

--------------------------
(ENGLISH)

Includes:
 - Financial Entities (http://www.bcra.gov.ar/)
 - A wizard online updater.

Requires:
	BeautifulSoup
	geopy

Attention, to run the wizard you need to have installed two libraries in python.
Without these two libraries the wizard will fail and will not update the information.

Install them using:

	$ pip install BeautifulSoup
	$ pip install geopy

from the CLI.

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
    'test': [
        'test/l10n_ar_banks_wizard.yml',
    ],
    'external_dependencies': {
        'python': [ 'BeautifulSoup', 'geopy' ],
    },
    'active': False,
    'installable': True,
}
# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
