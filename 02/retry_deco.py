import functools
import logging

logging.basicConfig(level=logging.INFO)

def retry_deco(retries, ignored_exceptions=None):
    if ignored_exceptions is None:
        ignored_exceptions = []

    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            attempt = 1
            while attempt <= retries:
                try:
                    logging.info(
                        f'Run "{func.__name__}" with positional args = {args}, '
                        f'keyword kwargs = {kwargs}, attempt = {attempt}'
                        )
                    result = func(*args, **kwargs)

                    logging.info(
                        f'Attempt {attempt} result = {result}'
                        )
                    return result
                except tuple(ignored_exceptions) as ex:
                    logging.info(
                        f'Attempt {attempt} exception = {type(ex).__name__}: {ex}'
                        )
                    raise
                except Exception as ex:
                    logging.info(
                        f'Attempt {attempt} exception = {type(ex).__name__}: {ex}'
                        )
                    if attempt == retries:
                        raise
                    attempt += 1
        return wrapper
    return decorator