""" TESTING FRAMEWORK FOR BENCOD ENCODING
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
from src.Bencode.encoding import Encoder

import unittest


class BencodeEncodingTest(unittest.TestCase):
    def setUp(self) -> None:
        self.cnt = 0

    def test_bencode_positive_int_encoding(self):
        """
        Integers are represented by an 'i' followed by the number in base 10 followed by an 'e'.
        For example i3e corresponds to 3 and i-3e corresponds to -3. Integers have no size limitation.
        i-0e is invalid. All encodings with a leading zero, such as i03e, are invalid, other than i0e,
        which of course corresponds to 0.
        """
        # BENCODE ENCODE INT
        self.bencode_positive_int = [i for i in range(1, 1000)]
        self.bencode_positive_int_answers = [b'i' + bytes(str(i), 'utf-8') + b'e' for i in range(1, 1000)]
        encoder = Encoder()

        for _ in self.bencode_positive_int:
            self.assertEqual(encoder.encode_int(_), self.bencode_positive_int_answers[self.cnt])
            self.cnt += 1

    def test_bencode_negative_int(self):
        # BENCODE ENCODE NEGATIVE INT
        encoder = Encoder()
        self.bencode_negative_int = [-j for j in range(1, 1000)]
        self.bencode_negative_int_answers = [b'i' + bytes(str(-i), 'utf-8') + b'e' for i in range(1, 1000)]

        for _ in self.bencode_negative_int:
            self.assertEqual(encoder.encode_int(_), self.bencode_negative_int_answers[self.cnt])
            self.cnt += 1

    def test_bencode_str_encoding(self):
        """Strings are length-prefixed base ten followed by a colon and the For example 4:spam corresponds to 'spam'."""
        # BENCODE ENCODE STRING
        self.bencode_string = [
            "Bolton", "Boltonia", "boltonias", "boltonite", "bolt-pointing",
            "boltrope", "bolt-rope", "boltropes", "bolts", "bolt-shaped",
            "boltsmith", "boltspreet", "boltstrake", "bolt-threading", "bolt-turning",
            "boltuprightness", "boltwork", "Boltzmann", "bolus", "boluses",
            "Bolzano", "BOM", "Boma", "Bomarc", "Bomarea", "bomb", "bombable"
        ]
        self.bencode_string_answers = [bytes(str(len(b)), 'utf-8') + b':' + bytes(b, 'utf-8')
                                       for b in self.bencode_string]

        encoder = Encoder()
        for _ in self.bencode_string:
            self.assertEqual(encoder.encode_byte_string(_), self.bencode_string_answers[self.cnt])
            self.cnt += 1

    def test_bencode_encode_list(self):
        """Lists Lists are encoded as follows: l<bencoded values>e The initial l and trailing e are beginning and
        ending delimiters. Lists may contain any bencoded type, including integers, strings, dictionaries,
        and even lists within other lists. Example: l4:spam4:eggse represents the list of two strings: [ "spam",
        "eggs" ] Example: le represents an empty list: []"""
        # BENCODE ENCODE LISTS
        self.bencode_lists = [[1, "EGG"], ["uno", 32, [1, "S"]]]
        self.bencode_lists_answers = [b'li1e3:EGGe', b'l3:unoi32eli1e1:See']

        encoder = Encoder()
        for _ in self.bencode_lists:
            self.assertEqual(encoder.encode_list(_), self.bencode_lists_answers[self.cnt])
            self.cnt += 1

    def test_bencdoe_encode_dict(self):
        """
        Dictionaries are encoded as a 'd' followed by a list of alternating keys and their
        corresponding values followed by an 'e'.For example, d3: cow3:moo4: spam4:eggse
        corresponds to {'cow': 'moo', 'spam': 'eggs'} and d4: spaml1:a1: bee
        corresponds to {'spam': ['a', 'b']}.Keys must
        be strings and appear in sorted order(sorted as raw strings, not alphanumerics).
        """
        bencode_dict_answers = [
            b'd4:spaml1:a1:bee',
            b'd9:publisher3:bob17:publisher-webpage15:www.example.com18:publisher.location4:homee']

        bencode_dict = [
            {"spam": ["a", "b"]},

            {"publisher": "bob",
             "publisher-webpage": "www.example.com",
             "publisher.location": "home"},
        ]
        encoder = Encoder()
        for _ in bencode_dict:
            self.assertEqual(encoder.encode_dict(_), bencode_dict_answers[self.cnt])
            self.cnt += 1

    def test_bencode_enocde_dict_sorted_order(self):
        """
        Keys must be strings and appear in sorted order (sorted as raw strings, not alphanumerics).
        The strings should be compared using a binary comparison, not a culture-specific "natural" comparison.
        """
        bencode_dict = [
            {"spam": ["a", "b"]},

            {"publisher": "bob",
             "publisher-webpage": "www.example.com",
             "publisher.location": "home"},
        ]

    def test_bencode_encoding(self):
        """
        Test all encoding methods (str, int, list, dict) in the same manner.
        """
        self.to_bencode = ["Bolton",
                           33,
                           ["uno", 32, [1, "S"]],
                           {"publisher": "bob",
                            "publisher-webpage": "www.example.com",
                            "publisher.location": "home"},

                           ]
        self.bencode_answers = [b'6:Bolton',
                                b'i33e',
                                b'l3:unoi32eli1e1:See',
                                b'd9:publisher3:bob17:publisher-webpage15:www.example.com18:publisher.location4:homee'
                                ]
        encoder = Encoder()
        for tests in self.to_bencode:
            self.assertEqual(encoder.to_bencode_encoding(tests), self.bencode_answers[self.cnt])
            self.cnt += 1


