import pprint
import bencodepy

class Decoder:
    def __init__(self):
        self.index = 0

    @staticmethod
    def find_end_of_list(data, start_index):
        count = 0
        for i in range(start_index, len(data)):
            if data[i:i + 1] == b'l':
                count += 1
            elif data[i:i + 1] == b'e':
                count -= 1
                if count == 0:
                    return i
        return -1

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
    decoder = Decoder()
        torrent_file = read_from_file("GIVE YOUR TORRENT FILE")
    x = bencodepy.decode(torrent_file)

    y = decoder.decode(torrent_file)

    print(x == y) # PRINTS TRUE :)