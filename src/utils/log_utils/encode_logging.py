from src.utils.log_utils.abstract_logging import Logger
from src.utils.log_utils.logging_conf import logger


class EncodeLogger(Logger):

    def log_info(self) -> None:
        logger.info("Encoded is done ")

    def log_debug(self) -> None:
        logger.debug("")

    def log_warning(self) -> None:
        logger.warning("Something went wrong")
