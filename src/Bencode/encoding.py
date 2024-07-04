""" BENCODE ENCODER
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
from src.utils.log_utils.log import log


class Encoder:
    def __init__(self, encode='utf-8'):
        self.encode = encode

    def encode_byte_string(self, s: str) -> bytes:
        """<string length encoded in base ten ASCII>:<string data>"""
        encoded_str_length = bytes(str(len(s)), self.encode)
        byte_colon = b':'
        try:
            data_as_bytes = bytes(s, self.encode)
            return encoded_str_length + byte_colon + data_as_bytes
        except TypeError:
            return encoded_str_length + byte_colon + s

    def encode_int(self, i: int) -> bytes:
        if not isinstance(i, int):
            raise TypeError(f"Expected int, got {type(i)}")

        if i == '-0':
            raise ValueError("Invalid integer value: -0")

        num_str = str(i)

        return b'i' + bytes(num_str, self.encode) + b'e'

    def encode_list(self, lst: list) -> bytes:
        if not isinstance(lst, list):
            raise TypeError(f"Expected list, got {type(lst)}")

        encoded_list = b'l'
        for item in lst:
            encoded_list += self.encode_value(item)
        return encoded_list + b'e'

    def encode_dict(self, d: dict) -> bytes:
        if not isinstance(d, dict):
            raise TypeError(f"Expected dict, got {type(d)}")

        encoded_dict = b'd'
        for key in sorted(d.keys()):
            if not isinstance(key, (str, int)):
                raise TypeError("Dictionary keys must be strings or integers")

            encoded_dict += self.encode_value(key)
            encoded_dict += self.encode_value(d[key])
        return encoded_dict + b'e'

    def encode_value(self, value) -> bytes:
        if isinstance(value, int):
            return self.encode_int(value)
        elif isinstance(value, str):
            return self.encode_byte_string(value)
        elif isinstance(value, bytes):
            return self.encode_byte_string(value)
        elif isinstance(value, list):
            return self.encode_list(value)
        elif isinstance(value, dict):
            return self.encode_dict(value)
        else:
            raise TypeError(f"Unsupported data type: {type(value)}")

    @log(cls='encode', level='info')
    def to_bencode_encoding(self, inp) -> bytes:
        return self.encode_value(inp)


if __name__ == "__main__":
    Encdr = Encoder()
    Encdr.to_bencode_encoding()
