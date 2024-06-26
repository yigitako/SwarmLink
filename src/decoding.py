# {"name": "OpenAI", "A": 2, "F": 222}
# b'd1:Ai2e1:Fi222e4:name6:OpenAIe'
# Bencode decoder
class Decoder:
    def __init__(self):
        self.input = str(b'i32e', encoding="utf-8")

    def read_from_file(self):
        with open(r"C:\Users\yigit\Downloads\archlinux-2024.06.01-x86_64.iso.torrent", 'rb') as f:
            b = f.read()
        print(b)
    def decode_int(self, i):
        return i[1:len(i) - 1]

    def decode_string(self, b):
        return b[b.find(":") + 1: len(b)]

    def decode_list(self):
        pass

    def decode_dict(self):
        pass

    def decode_bencode(self):
        pass


if __name__ == "__main__":
    Dec = Decoder()
    print(Dec.decode_string("10:bombombom2"))
    Dec.read_from_file()
