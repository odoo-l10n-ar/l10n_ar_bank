#!/usr/bin/python

try:
        import geopy
except ImportError:
        print "Please, intall geopy using 'pip install geopy'."

import re, sys
from BeautifulSoup import BeautifulSoup
from geosearch import unify_geo_data, strip_accents
from cache import urlopen

encoding = 'ISO-8859-1'
compiled_re = {
    # Common
        'code'   : re.compile(r'N... Banco:</span>\s*(\d+)'),
    #   'name': calculated,
        'office' : re.compile(r'Direcci..n:</span>&nbsp;\s*(.{40})'),
        'street' : re.compile(r'Direcci..n:</span>&nbsp;\s*.{40}([^-]*)-'),
    #   'street2': None
        'city'   : re.compile(r'Direcci..n:</span>&nbsp;\s*.{40}[^-]*-([^-]*)-'),
        'state'  : re.compile(r'Direcci..n:</span>&nbsp;\s*.{40}[^-]*-[^-]*-([^-]*)'),
    #   'country': 'Argentina',
        'phone'  : re.compile(r'Tel..fono:</span>&nbsp;([\d-]+)\s*&nbsp;'),
        'fax'    : re.compile(r'Fax:</span>&nbsp;([\d-]+)\s*&nbsp;'),
        'email'  : re.compile(r'Email:</span>&nbsp;<a href="mailto:([^"\s]+)\s*"'),
    #   'active' : True
    # Others
        'address': re.compile(r'Direcci..n:</span>&nbsp;\s*(.*)\s*\r'),
        'site'   : re.compile(r'Sitio:&nbsp;</span><a href="([^"\s]+)\s*"'),
        'gins'   : re.compile(r'Grupo Institucional:</span>&nbsp;\s*(.*)\s*'),
        'ghom'   : re.compile(r'Grupo Homog..neo:</span>&nbsp;\s*(.*)\s*'),
        'vat'    : re.compile(r'CUIT:</span>&nbsp;([\d-]+)\s*&nbsp;'),
    }

postprocessor_keys = {
    'code': lambda v, d: 'email' in d and [ s for s in
                                           d['email'].split('@')[1].split('.')
                                           if not s in ["ar", "com"]
                                          ][0].upper() or v,
    'street': lambda v, d: "%(street)s %(number)s" % d,
    'name': lambda v, d: d[v].title()
}

dictkeys = [
    'code',
    'name',
    'bic',
    'street',
    'number',
    'street2',
    'zip',
    'city',
    'state',
    'country',
    'latitud',
    'longitud',
    'phone',
    'fax',
    'email',
    'active',
    'id',
    'vat',
    'office',
    'site',
    'gins',
    'ghom',
    'address',
]

bankfields = [
    'name',
    'code',
    'active',
    'bic',
    'street',
    'street2',
    'zip',
    'city',
    'state',
    'country',
    'phone',
    'fax',
    'email',
]

def ar_banks_iterator(
    url_bank_list='http://www.bcra.gov.ar/sisfin/sf010100.asp',
    url_bank_info='http://www.bcra.gov.ar/sisfin/sf010100.asp?bco=%s',
    country='Argentina'):
    """
    Argentinian Banks list iterator.

    >>> banks = ar_banks_iterator()
    >>> banks.next().keys() == ['latitud', 'ghom', 'fax', 'code', 'office', \
                                'street2', 'site', 'number', 'phone', \
                                'street', 'address', 'active', 'gins', 'id', \
                                'longitud', 'city', 'name', 'zip', 'country', \
                                'state', 'email', 'vat']
    True
    """
    page_list = urlopen(url_bank_list)
    soup_list = BeautifulSoup(page_list)

    for bank in soup_list('option'):
        if 'value' in dict(bank.attrs):
            id, name = bank['value'].strip(), bank.string.strip()
            page_bank = urlopen(url_bank_info % id)
            soup_bank = BeautifulSoup(page_bank)

            data = {
                'id': id,
                'name': name,
                'country': country,
                'active': '1',
            }
            for line in soup_bank('div')[5]('table')[0]('tr'):
                sline = line.td.renderContents()
                for key in compiled_re.keys():
                    search = compiled_re[key].search(sline)
                    if search:
                        data[key] = unicode(search.group(1).strip(), encoding)
            searchaddress = u"%(street)s, %(city)s, %(state)s, %(country)s" % data
            geodata = unify_geo_data(strip_accents(searchaddress))
            data.update(geodata)
            for key in postprocessor_keys.keys():
                if key in data:
                    data[key] = postprocessor_keys[key](key, data)
            yield data

def xml_banks():
    print """
<?xml version="1.0" encoding="UTF-8"?>
<openerp>
\t<data noupdate="True">
"""
    for bank in ar_banks_iterator():
        print "\t\t<record model='res.bank' id='%(id)s'>" % bank
        for key in bankfields:
            if key in bank:
                try:
                    print "\t\t\t<field name='%s'>%s</field>" % (key,
                                                                 bank[key].encode('utf-8'))
                except:
                    print "\t\t\t<field name='%s'>ERROR</field>" % key
        print "\t\t</record>"
    print """
\t</data>
</openerp>
"""

def test_suite():
    import doctest
    return doctest.DocTestSuite()

if __name__ == "__main__":
    xml_banks()
    #import unittest
    #runner = unittest.TextTestRunner()
    #runner.run(test_suite())

