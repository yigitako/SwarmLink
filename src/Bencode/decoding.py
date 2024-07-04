""" BENCODE DECODER
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


class Decoder:
    def __init__(self):
        self.index = 0

    def decode_int(self, data):
        end_index = data.find(b'e', self.index)
        number = int(data[self.index + 1:end_index])
        self.index = end_index + 1
        return number

    def decode_string(self, data):
        colon_index = data.find(b':', self.index)
        length = int(data[self.index:colon_index])
        start_index = colon_index + 1
        end_index = start_index + length
        self.index = end_index
        # TODO: THE TRY EXCEPT IS STUPID IDEA, THIS IS JUST A QUICK HACK.
        try:
            return data[start_index:end_index].decode()
        except UnicodeDecodeError:
            return data[start_index:end_index]

    def decode_list(self, data):
        items = []
        self.index += 1
        while data[self.index:self.index + 1] != b'e':
            items.append(self.decode(data))
        self.index += 1
        return items

    def decode_dict(self, data):
        dict_items = {}
        self.index += 1

        while data[self.index:self.index + 1] != b'e':
            key = self.decode(data)
            value = self.decode(data)
            dict_items[key] = value

        self.index += 1
        return dict_items

    def decode(self, data):
        if data[self.index:self.index + 1] == b'd':
            return self.decode_dict(data)

        elif data[self.index:self.index + 1] == b'l':
            return self.decode_list(data)

        elif data[self.index:self.index + 1] == b'i':
            return self.decode_int(data)

        elif b'0' <= data[self.index:self.index + 1] <= b'9':
            return self.decode_string(data)


def read_from_file(file_path):
    with open(file_path, 'rb') as file:
        return file.read()


if __name__ == "__main__":
    Dec = Decoder()
    Dec.decode(b'l4:yiiii32ee')
