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

def shist(s, chars="abcdefghijklmnopqrstuvwxyz .01234567"):
    """
    Generate a histogram for s

    >>> shist('hola mundo')
    [1, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 1, 1, 2, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    """
    h = [0] * len(chars)
    _i = dict(zip(chars, range(len(chars))))
    for c in s:
        try:
            h[_i[c]] = h[_i[c]] + 1
        except:
            pass
    return h

def mostequivalent(strings, S):
    """
    Return the index of the most equivalent string in strings to S using a
    histogram.

    >>> mostequivalent(['el perro esta en la casa', 'mundo nuevo'], 'hola mundo')
    1
    """
    Sshist = shist(S)
    stringshist = map(shist, strings)
    md = -1
    for i in xrange(len(stringshist)):
        d = sum(map(lambda (a,b): abs(a-b), zip(stringshist[i], Sshist)))
        if i == 0 or d < md:
            mi, md = i, d
    return mi

def test_suite():
    import doctest
    return doctest.DocTestSuite()

if __name__ == "__main__":
    import unittest
    runner = unittest.TextTestRunner()
    runner.run(test_suite())

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
