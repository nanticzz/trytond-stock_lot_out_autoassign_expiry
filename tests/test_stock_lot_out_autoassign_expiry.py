#!/usr/bin/env python
# This file is part of the stock_lot_out_autoassign_expiry module for Tryton.
# The COPYRIGHT file at the top level of this repository contains
# the full copyright notices and license terms.
import unittest
import trytond.tests.test_tryton
from trytond.tests.test_tryton import test_depends


class StockLotOutAutoassignExpiryTestCase(unittest.TestCase):
    'Test Stock Lot Out Autoassign Expiry module'

    def setUp(self):
        trytond.tests.test_tryton.install_module(
            'stock_lot_out_autoassign_expiry')

    def test0006depends(self):
        'Test depends'
        test_depends()


def suite():
    suite = trytond.tests.test_tryton.suite()
    suite.addTests(unittest.TestLoader().loadTestsFromTestCase(
        StockLotOutAutoassignExpiryTestCase))
    return suite

if __name__ == '__main__':
    unittest.TextTestRunner(verbosity=2).run(suite())
