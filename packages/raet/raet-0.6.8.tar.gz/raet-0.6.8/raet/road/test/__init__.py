# -*- coding: utf-8 -*-
'''
raet.road unit test package
'''
import sys
if sys.version_info < (2, 7):
    import unittest2 as unittest
else:
    import unittest
import os

from raet import test
from ioflo.base.consoling import getConsole
console = getConsole()
console.reinit(verbosity=console.Wordage.concise)

top = os.path.dirname(os.path.abspath(sys.modules.get(__name__).__file__))

if __name__ == "__main__":
    test.run(top, failfast=True)
