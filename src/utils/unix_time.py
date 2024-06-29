# Convert an integer representing a timestamp to a Unix time object
# AUTHOR :: YIGIT AKOYMAK
# DATE   :: 06.26.2024
import datetime


def convert_timestamp_unix_time(timestamp: int) -> datetime.datetime:
    unix_time = datetime.datetime.utcfromtimestamp(timestamp)
    return unix_time
