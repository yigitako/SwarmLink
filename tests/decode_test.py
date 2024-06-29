import unittest
from src.Bencode.decoding import Decoder


class TestBencodeDecoder(unittest.TestCase):
    def setUp(self) -> None:
        self.cnt = 0
        self.decoder = Decoder()
        self.sample_torrent_file_path = r"torrent_files/big-buck-bunny.torrent"

    def test_decode_positive_int(self):
        encoded = b'i200e'
        self.assertEqual(self.decoder.decode_int(encoded), 200)

    def test_decode_string(self):
        encoded = b'5:hello'
        self.assertEqual(self.decoder.decode_string(encoded), b'hello')

    def test_decode_list(self):
        encoded = b'li123e5:helloe'
        self.assertEqual(self.decoder.decode_list(encoded), [123, b'hello'])

    def test_decode_dict(self):
        encoded = b'd3:bar4:spam3:fooi42ee'
        expected = {b'bar': b'spam', b'foo': 42}
        self.assertEqual(self.decoder.decode_dict(encoded), expected)
