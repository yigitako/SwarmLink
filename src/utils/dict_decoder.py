import pprint
from .unix_time import convert_timestamp_unix_time


def dict_decoder(diction):
    creation_date = convert_timestamp_unix_time(diction['creation date'])
    author = diction['created by']
    file_size_bytes = diction['info']['length']
    file_size_mb = file_size_bytes * 1 / 10 ** 6

    print("The file was created on:", creation_date)
    print("Author:", author)
    print("File Size:", str(int(file_size_mb)), "MB")
