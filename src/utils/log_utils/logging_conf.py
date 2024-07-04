import logging
import os

from datetime import datetime


def iso_8601_time():
    now = datetime.now()
    iso_time_format = now.strftime("%Y-%m-%dT%H_%M_%S")
    return iso_time_format


def get_ancestor_directory(levels, start_path=__file__):
    path = start_path
    for _ in range(levels):
        path = os.path.dirname(path)
    return path


grandgrandparent_directory = get_ancestor_directory(4)

log_path = os.path.join(rf"{grandgrandparent_directory}\logs", fr"BitTorrent{iso_8601_time()}.log")

logger = logging.getLogger(__name__)

logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - %(funcName)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler(log_path, encoding='utf-8'),
        logging.StreamHandler()
    ]
)
