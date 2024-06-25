# for a,b in zip(self.bencode_negative_int, self.bencode_negative_int_answers):
#   print(a, b)
# bytes(str(length), self.encoding) + b':'
from src import encoding

import unittest


class BencodeEncodingTest(unittest.TestCase):
    def setUp(self):
        """" Automatically called for every single test we run."""

        # BENCODE ENCODE INT
        self.bencode_positive_int = [i for i in range(1, 1000)]
        self.bencode_positive_int_answers = [b'i' + bytes(str(i), 'utf-8') + b'e' for i in range(1, 1000)]

        # BENCODE ENCODE NEGATIVE INT
        self.bencode_negative_int = [-j for j in range(1, 1000)]
        self.bencode_negative_int_answers = [b'i' + bytes(str(-i), 'utf-8') + b'e' for i in range(1, 1000)]

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

        # BENCODE ENCODE LISTS
        self.bencode_lists = [
            [1, "EGG"],
            ["uno", 32, [1, "S"]]
        ]
        self.bencode_lists_answers = [
            b'li1e3:EGGe',
            b'l3:unoi32eli1e1:See'
        ]
        # BENCODE DICTIONARY
        self.clear_text = {"bar": "spam", "foo": 42}

    def test_bencode_int_encoding(self):
        """
        Integers are represented by an 'i' followed by the number in base 10 followed by an 'e'.
        For example i3e corresponds to 3 and i-3e corresponds to -3. Integers have no size limitation.
        i-0e is invalid. All encodings with a leading zero, such as i03e, are invalid, other than i0e,
        which of course corresponds to 0.
        """
        encoder = encoding.Encoder()
        cnt = 0
        for _ in self.bencode_positive_int:
            self.assertEqual(encoder.encode_int(_), self.bencode_positive_int_answers[cnt])
            cnt += 1

        cnt = 0
        for _ in self.bencode_negative_int:
            self.assertEqual(encoder.encode_int(_), self.bencode_negative_int_answers[cnt])
            cnt += 1

    def test_bencode_str_encoding(self):
        """Strings are length-prefixed base ten followed by a colon and the For example 4:spam corresponds to 'spam'."""
        encoder = encoding.Encoder()
        cnt = 0
        for _ in self.bencode_string:
            self.assertEqual(encoder.encode_byte_string(_), self.bencode_string_answers[cnt])
            cnt += 1

    def test_bencode_encode_list(self):
        encoder = encoding.Encoder()
        cnt = 0
        for _ in self.bencode_lists:
            self.assertEqual(encoder.encode_list(_), self.bencode_lists_answers[cnt])
            cnt += 1

    def test_bencdoe_encode_dict(self):
        """
        Dictionaries are encoded as a 'd' followed by a list of alternating keys and their
        corresponding values followed by an 'e'.For example, d3: cow3:moo4: spam4:eggse
        corresponds to {'cow': 'moo', 'spam': 'eggs'} and d4: spaml1:a1: bee
        corresponds to {'spam': ['a', 'b']}.Keys must
        be strings and appear in sorted order(sorted as raw strings, not alphanumerics).
        """
        pass

    def test_bencode_encoding(self):
        pass
        # self.assertEqual(encode.encode(self.clear_text), 'd3:bar4:spam3:fooi42ee'
        #                 , f"Given format did not match the expected result")


if __name__ == "__main__":
    unittest.main()
