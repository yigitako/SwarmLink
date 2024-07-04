from src.utils.log_utils.encode_logging import EncodeLogger
import functools


def log(cls, level="info"):
    def decorator(func):
        methods = {
            'encode': EncodeLogger()
        }
        Flogger = methods[cls]

        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            try:
                r = func(*args, **kwargs)
            except TypeError as e:
                Flogger.log_warning()
                raise

            getattr(Flogger, f"log_{level}")()
            return r

        return wrapper

    return decorator
