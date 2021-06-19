# -*- coding: utf-8 -*-

'''
 Module
     run_test.py
 Copyright
     Copyright (C) 2017 Vladimir Roncevic <elektron.ronca@gmail.com>
     flask_func_struct_angular is free software: you can redistribute it
     and/or modify it under the terms of the GNU General Public License as
     published by the Free Software Foundation, either version 3 of the
     License, or (at your option) any later version.
     flask_func_struct_angular is distributed in the hope that it will
     be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of
     MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.
     See the GNU General Public License for more details.
     You should have received a copy of the GNU General Public License along
     with this program. If not, see <http://www.gnu.org/licenses/>.
 Info
     Define class RunTest with attribute(s) and method(s).
     Create initial data and insert to database.
'''

import sys

try:
    import unittest
    from flask_script import Command
except ImportError as ats_error_message:
    MESSAGE = '\n{0}\n{1}\n'.format(__file__, ats_error_message)
    sys.exit(MESSAGE)  # Force close python ATS ##############################

__author__ = 'Vladimir Roncevic'
__copyright__ = 'Copyright 2017, Free software to use and distributed it.'
__credits__ = ['Vladimir Roncevic']
__license__ = 'https://bit.ly/2UklOwb'
__version__ = '1.2.0'
__maintainer__ = 'Vladimir Roncevic'
__email__ = 'elektron.ronca@gmail.com'
__status__ = 'Updated'


class RunTest(Command):
    '''
        Define class RunTest with attribute(s) and method(s).
        Run tests.
        It defines:

            :attributes:
                | None.
            :methods:
                | __init__ - initial constructor.
                | run - run tests.
    '''

    def __init__(self):
        '''
            Initial constructor.

            :exceptions: None
        '''
        super(RunTest, self).__init__()

    def run(self):
        '''
            Run testes.

            :return: 0 for success else 1.
            :rtype: <int>
            :exceptions: None
        '''
        tests = unittest.TestLoader().discover(
            'app_server/tests', pattern='test*.py'
        )
        result = unittest.TextTestRunner(verbosity=2).run(tests)
        if result.wasSuccessful():
            return 0
        return 1
