""" Meta info file structure for Torrent file
   AUTHOR :: YIGIT AKOYMAK
   DATE   :: 06.07.2024

   SwarmLink BitTorrent Protocol Implementation
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

# from src.Bencode.encoding import Encoder
from src.Bencode.decoding import Decoder, read_from_file
import pprint

dec = Decoder()

BitTorrent_meta = dec.decode(
    read_from_file(r"C:\Users\yigit\PycharmProjects\SwarmLink\tests\torrent_files\big-buck-bunny.torrent"))
pprint.pp(BitTorrent_meta)


class TorrentMetaInfo:
    def __init__(self) -> None:
        self.announce_url: str = BitTorrent_meta.get("announce", None)
        self.announce_list: list = BitTorrent_meta.get("announce-list", None)
        self.comment: str = BitTorrent_meta.get("comment", None)
        self.creation_date: str = BitTorrent_meta.get("created by", None)
        self.encoding: str = BitTorrent_meta.get("encoding", None)
        self.info: dict = BitTorrent_meta.get('info', None)
