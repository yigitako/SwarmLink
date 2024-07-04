from abc import ABC, abstractmethod


class Logger(ABC):
    @abstractmethod
    def log_info(self) -> None:
        pass

    @abstractmethod
    def log_debug(self) -> None:
        pass

    @abstractmethod
    def log_warning(self) -> None:
        pass
