# Bencode decoder

__author__ = "Yigit Akoymak"
class Decoder:
    def __init__(self):
        self.input = str(b'i32e', encoding="utf-8")

    @staticmethod
    def find_end_of_list(l, start_index):
        # Helper function to find the end of a nested list
        count = 0
        for i in range(start_index, len(l)):
            if l[i] == 'l':
                count += 1
            elif l[i] == 'e':
                count -= 1
                if count == 0:
                    return i
        return -1

    def read_from_file(self):
        with open(r"C:\Users\yigit\Downloads\archlinux-2024.06.01-x86_64.iso.torrent", 'rb') as f:
            b = f.read()
        return b

    def decode_int(self, i):
        return i[1:len(i) - 1]

    def decode_string(self, b):
        return b[b.find(":") + 1: len(b)]

    def decode_list(self, l):
        items = []
        index = 1  # Start after the initial 'l'
        while index < len(l):
            # Find the length of the next string
            if l[index].isdigit():
                length_end = l.find(':', index)
                length = int(l[index:length_end])
                string_start = length_end + 1
                string_end = string_start + length
                encoded_string = l[string_start:string_end]
                decoded_string = self.decode_string(encoded_string)
                items.append(decoded_string)
                index = string_end

            # Find the int
            elif l[index] == 'i':
                start_index = index
                e_index = l.find('e', start_index)
                substring = l[start_index:e_index + 1]
                decoded_int = self.decode_int(substring)
                items.append(decoded_int)
                index = e_index + 1  # Move past 'e'

            # Handle nested list
            elif l[index] == 'l':
                # Find the end of the nested list
                nested_end = self.find_end_of_list(l, index)
                nested_list = l[index:nested_end + 1]
                decoded_list = self.decode_list(nested_list)
                items.append(decoded_list)
                index = nested_end + 1
            if l[index] == 'd':
                pass
            else:
                index += 1
        return items

    def decode_dict(self):
        pass

    def decode_bencode(self):
        pass


if __name__ == "__main__":
    Dec = Decoder()
    torrent_file = Dec.read_from_file()
    print(torrent_file)
    print(Dec.decode_list('l5:Helloi42el6:Nested4:Listee'))  # d5:Hello5:World3:fooi42ee))
