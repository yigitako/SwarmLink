# BENCODE encoder
class Encoder:

    # TODO: isinstance is repeated often, USE A FUNCTION OR PATTERN(?) to minimise the code:
    # TODO: THERE SHOULD BE MORE TYPE CHECKS TO IMPROVE SAFETY.
    def __init__(self, encode='utf-8'):
        self.output = b''
        self.encode = encode

    def encode_byte_string(self, s) -> bytes:
        """<string length encoded in base ten ASCII>:<string data>"""
        encoded_str_length = bytes(str(len(s)), self.encode)
        byte_colon = b':'
        data_as_bytes = bytes(s, self.encode)
        return encoded_str_length + byte_colon + data_as_bytes

    def encode_int(self, i) -> bytes or bool:
        num_str = str(i)

        if num_str == '-0':
            return False

        return b'i' + bytes(num_str, self.encode) + b'e'

    def encode_list(self, elem) -> bytes:
        place_holder = b''

        for _ in elem:
            if isinstance(_, int):
                place_holder += self.encode_int(_)

            elif isinstance(_, str):
                place_holder += self.encode_byte_string(_)

            elif isinstance(_, list):
                place_holder += self.encode_list(_)

            elif isinstance(_, dict):
                place_holder += self.encode_diction(_)

        return b'l' + place_holder + b'e'

    def encode_diction(self, d) -> bytes:
        """Encode a dictionary using Bencode format."""
        encoded_items = b''
        for key in sorted(d.keys()):
            encoded_key = self.encode_byte_string(key)
            value = d[key]

            if isinstance(value, int):
                encoded_value = self.encode_int(value)

            elif isinstance(value, str):
                encoded_value = self.encode_byte_string(value)

            elif isinstance(value, list):
                encoded_value = self.encode_list(value)

            elif isinstance(value, dict):
                encoded_value = self.encode_diction(value)

            else:
                raise ValueError("Unsupported data type")
            encoded_items += encoded_key + encoded_value
        return b'd' + encoded_items + b'e'

    def to_bencode_encdoing(self, inp):
        if isinstance(inp, int):
            return self.encode_int(inp)

        elif isinstance(inp, str):
            return self.encode_byte_string(inp)

        elif isinstance(inp, list):
            return self.encode_list(inp)

        elif isinstance(inp, dict):
            return self.encode_diction(inp)

        else:
            raise ValueError("Unsupported data type for Bencoding")


if __name__ == "__main__":
    encoder = Encoder()
    example_dict = {"name": "OpenAI", "A": 2, "F": 222}
    print(encoder.to_bencode_encdoing(example_dict))
