import hashlib
from src.Bencode.encoding import Encoder
from src.torrent_meta import TorrentMetaInfo
from struct import pack


class UdpTrackerAnnounce:
    def __init__(self, tmf: TorrentMetaInfo, connection_id, transaction_id):
        self.connection_id = pack(">Q", connection_id)
        self.action = pack(">L", 1)
        self.transaction_id = pack(">L", transaction_id)
        self.info_hash = tmf.info
        self.peer_id = tmf.peer_id
        self.downloaded = pack(">Q", 0)
        self.left = pack(">Q", 0)
        self.uploaded = pack(">Q", 0)
        self.event = pack(">L", 0)
        self.ip_address = pack(">L", 0)
        self.key = pack(">L", 0)
        self.num_want = pack(">l", -1)
        self.port = pack(">H", 6881)

    def to_bytes(self):
        return (self.connection_id + self.action + self.transaction_id +
                self._info_hasher(self.info_hash) + self.peer_id.encode('utf-8') + self.downloaded +
                self.left + self.uploaded + self.event + self.ip_address +
                self.key + self.num_want + self.port)
