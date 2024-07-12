import socket
from struct import unpack, pack
from udp_connect_request import UdpTrackerConnection
from udp_connect_response import UdpConnection
from urllib.parse import urlparse
from src.torrent_meta import TorrentMetaInfo
from udp_announce import UdpTrackerAnnounce


def send_message(conn, sock, tracker_message):
    message = tracker_message.to_bytes()
    sock.sendto(message, conn)
    response = _read_from_socket(sock)
    return response


def _read_from_socket(sock, max_attempts=5):
    data = b''
    attempts = 0

    while attempts < max_attempts:
        try:
            buff = sock.recv(4096)
            if len(buff) <= 0:
                break
            data += buff

        except socket.timeout:
            break

        except socket.error as e:
            err = e.args[0]
            if err == errno.EAGAIN or err == errno.EWOULDBLOCK:
                break
            else:
                break

        except Exception as e:
            break

        attempts += 1

    return data


tmf = TorrentMetaInfo()

for i in tmf.announce_list:
    sock = None
    try:
        i = "".join(i)
        parsed = urlparse(i)
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        sock.settimeout(4)
        ip, port = socket.gethostbyname(parsed.hostname), parsed.port

        tracker_connection_input = UdpTrackerConnection()
        response = send_message((ip, port), sock, tracker_connection_input)

        if response:
            ucp = UdpConnection.from_bytes(response)
            import pprint

            pprint.pp(f"Received response: Action={ucp.action}, "
                      f"Trans_ID={ucp.trans_id}, "
                      f"Conn_ID={ucp.conn_id}")
            from src.torrent_meta import TorrentMetaInfo

            x = UdpTrackerAnnounce(TorrentMetaInfo(), ucp.conn_id, ucp.trans_id)
            announce = send_message((ip, port), sock, x)
            print(announce)

    finally:
        sock.close()
