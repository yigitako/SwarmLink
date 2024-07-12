from struct import unpack
from dataclasses import dataclass


@dataclass(slots=True)
class UdpConnection:
    """
    A data class that represents a UDP connection payload with action, transaction ID, and connection ID attributes.

    :ivar action: An integer indicating the action code of the UDP connection.
    :ivar trans_id: An integer representing the transaction ID of the UDP connection.
    :ivar conn_id: An integer representing the connection ID of the UDP connection.
    """
    action: int
    trans_id: int
    conn_id: int

    @classmethod
    def from_bytes(cls, payload: bytes) -> 'UdpConnectionPayload':
        """
        Create an instance of UdpConnection from a byte sequence.

        This class method unpacks a 16-byte payload into an action, transaction ID, and connection ID,
        which are used to initialize and return a new instance of UdpConnection.

        :param payload: A byte sequence exactly 16 bytes long. The first 4 bytes are interpreted as an
                        unsigned integer representing the 'action', the next 4 bytes as an unsigned integer
                        representing the 'transaction ID', and the final 8 bytes as an unsigned long long
                        representing the 'connection ID'.
        :type payload: bytes
        :return: An instance of UdpConnection initialized with the unpacked action, transaction ID, and connection ID.
        :rtype: UdpConnection
        :raises ValueError: If the length of the payload is not exactly 16 bytes, indicating an invalid or
                            corrupted payload.
        """
        if len(payload) != 16:
            raise ValueError("Invalid payload length, expected 16 bytes")

        action, = unpack('>I', payload[:4])

        if action != 0:
            raise ValueError(f"The expected action is 0, but received {action}.")

        trans_id, = unpack('>I', payload[4:8])
        conn_id, = unpack('>Q', payload[8:])
        return cls(action=action, trans_id=trans_id, conn_id=conn_id)
