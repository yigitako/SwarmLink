"""
   Based on github.com/gallexis/PyTorrent
   Meta info file structure for Torrent file
   AUTHOR :: YIGIT AKOYMAK
   DATE   :: 08.07.2024

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

import random
from struct import pack, unpack
from dataclasses import dataclass, field


@dataclass(slots=True)
class UdpTrackerConnection:
    """
    Represents a UDP tracker connection request in the BitTorrent protocol.

    This class provides a method to package the connection ID, action type, and
    a randomly generated transaction ID into a byte format suitable for network
    transmission as required by the UDP tracker protocol.

    Attributes:
        conn_id (bytes): A packed 64-bit integer representing the connection ID, initialized
                         to a protocol-specific magic constant (0x41727101980).

        action (bytes): A packed 32-bit integer specifying the action type for the tracker.
                        For a connection request, this is set to 0.

        trans_id (bytes): A packed 32-bit integer representing the transaction ID, which
                          should be randomly generated to uniquely identify the request.
    """
    conn_id: bytes = pack('>Q', 0x41727101980)
    action: bytes = pack('>I', 0)
    trans_id: bytes = field(default_factory=lambda: pack('>I', random.randint(0, 100000)))

    def to_bytes(self) -> bytes:
        """
        Packs the connection ID, action, and transaction ID into a single bytes object.

        This method combines the connection ID, action type, and a randomly generated transaction ID into a
        byte sequence. The data is formatted in big-endian byte order, which is the standard network byte order
        required for UDP tracker requests in the BitTorrent protocol.

        :return: A bytes object representing the packed UDP tracker connection request.
        :rtype: bytes
        """
        return self.conn_id + self.action + self.trans_id
