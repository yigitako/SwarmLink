# BENCODE encoder
class Encoder:
    def __init__(self, encode='utf-8'):
        self.output = b''
        self.encode = encode

    def encode_byte_string(self, s):
        """<string length encoded in base ten ASCII>:<string data>"""
        encoded_str_length = bytes(str(len(s)), self.encode)
        byte_colon = b':'
        data_as_bytes = bytes(s, self.encode)
        return encoded_str_length + byte_colon + data_as_bytes

    def encode_int(self, i):
        """i<integer encoded in base ten ASCII>e"""
        num_str = str(i)

        if num_str == '-0':
            return False

        return b'i' + bytes(num_str, self.encode) + b'e'

    def encode_list(self, elem):
        """
        Lists are encoded as follows: l<bencoded values>eThe initial l and trailing e are beginning and ending
        delimiters. Lists may contain any bencoded type, including integers, strings, dictionaries, and even lists
        within other lists. Example: l4:spam4:eggse represents the list of two strings: [ "spam", "eggs" ] Example:
        le represents an empty list: [] :param elem: :return:
        """
        place_holder = b''

        for _ in elem:
            if isinstance(_, int):
                place_holder += self.encode_int(_)

            elif isinstance(_, str):
                place_holder += self.encode_byte_string(_)

            elif isinstance(_, list):
                place_holder += self.encode_list(_)

            elif isinstance(_, dict):
                pass

        return b'l' + place_holder + b'e'

    def encode_diction(self):
        pass