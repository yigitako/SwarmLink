""" RUN UNIT-TESTS(decode_test, encode_test)
   AUTHOR :: YIGIT AKOYMAK
   DATE   :: 27.06.2024

   SwarmLink Bittorent Protocol Implementation
   Copyright (C) 2024  Yigit AKoymak
   This program is free software: you can redistribute it and/or modify
   it under the terms of the GNU General Public License as published by
   the Free Software Foundation, either version 3 of the License, or
   (at your option) any later version.

   This program is distributed in the hope that it will be useful,
   but WITHOUT ANY WARRANTY; without even the implied warranty of
   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
   GNU General Public License for more details.

   You should have received a copy of the GNU General Public License
   along with this program.  If not, see <https://www.gnu.org/licenses/>.
"""
import unittest

import decode_test
import encode_test

if __name__ == "__main__":
    loader = unittest.TestLoader()
    suite = unittest.TestSuite()

    suite.addTests(loader.loadTestsFromModule(encode_test))
    suite.addTests(loader.loadTestsFromModule(decode_test))

    # Run the test suite
    runner = unittest.TextTestRunner()
    runner.run(suite)
