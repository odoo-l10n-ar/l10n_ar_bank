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
import sys, urllib, hashlib, os, os.path, pickle
from geopy import geocoders
from types import GeneratorType

gc = geocoders.Google('ABQIAAAAMWm7ddpoRV3HO0u7NtA_IhRTfPMBNX3pvExQyYBKj7aZZJK5lxQYw0LDgWXedvepzKpGxQKf-kmN3A')

def urlopen(url):
    print >> sys.stderr, "Urlopen reading:", url
    basedir = os.path.join(os.getcwd(), 'cache')
    m = hashlib.new('ripemd160')
    m.update(url)
    if not os.path.exists(basedir):
        os.makedirs(basedir)
    tmpfilename = os.path.join(basedir, "urlopen_%s" % m.hexdigest())
    if not os.path.exists(tmpfilename):
        filename, header = urllib.urlretrieve(url, tmpfilename)
    return open(tmpfilename)

def geocode(input_string, **args):
    m = hashlib.new('ripemd160')
    m.update(input_string)
    m.update(pickle.dumps(args))
    tmpfilename = "cache/geocode_%s" % m.hexdigest()
    if not os.path.exists(tmpfilename):
        geocode_out = gc.geocode(input_string, **args)
        if isinstance(geocode_out, GeneratorType):
            geocode_out = list(geocode_out)
        pickle.dump(geocode_out, open(tmpfilename, 'w'))
    else:
        geocode_out = pickle.load(open(tmpfilename))

    return geocode_out

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
