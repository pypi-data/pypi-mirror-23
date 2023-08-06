# -*- coding: utf-8 -*-
"""
Automatic tests for python-ldap's module ldap.functions

See http://www.python-ldap.org/ for details.

$Id: t_ldap_functions.py,v 1.2 2017/04/28 07:30:59 stroeder Exp $
"""

# from Python's standard lib
import unittest

# from python-ldap
import ldap
from ldap.dn import escape_dn_chars
from ldap.filter import escape_filter_chars


class TestFunction(unittest.TestCase):
    """
    test ldap.functions
    """

    def test_ldap_strf_secs(self):
        """
        test function ldap_strf_secs()
        """
        self.assertEquals(ldap.strf_secs(0), '19700101000000Z')
        self.assertEquals(ldap.strf_secs(1466947067), '20160626131747Z')

    def test_ldap_strp_secs(self):
        """
        test function ldap_strp_secs()
        """
        self.assertEquals(ldap.strp_secs('19700101000000Z'), 0)
        self.assertEquals(ldap.strp_secs('20160626131747Z'), 1466947067)

    def test_escape_str(self):
        """
        test function escape_string_tmpl()
        """
        self.assertEquals(
            ldap.escape_str(
                escape_filter_chars,
                '(&(objectClass=aeUser)(uid=%s))',
                'foo'
            ),
            '(&(objectClass=aeUser)(uid=foo))'
        )
        self.assertEquals(
            ldap.escape_str(
                escape_filter_chars,
                '(&(objectClass=aeUser)(uid=%s))',
                'foo)bar'
            ),
            '(&(objectClass=aeUser)(uid=foo\\29bar))'
        )
        self.assertEquals(
            ldap.escape_str(
                escape_dn_chars,
                'uid=%s',
                'foo=bar'
            ),
            'uid=foo\\=bar'
        )
        self.assertEquals(
            ldap.escape_str(
                escape_dn_chars,
                'uid=%s,cn=%s,cn=%s,dc=example,dc=com',
                'foo=bar',
                'foo+',
                '+bar',
            ),
            'uid=foo\\=bar,cn=foo\\+,cn=\\+bar,dc=example,dc=com'
        )


if __name__ == '__main__':
    unittest.main()
