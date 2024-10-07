import functools
import logging

logging.basicConfig(level=logging.INFO)

def retry_deco(retries, ignored_exceptions=None):
    if ignored_exceptions is None:
        ignored_exceptions = ()

    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            attempt = 1
            while attempt <= retries:
                try:
                    logging.info(
                        'Run "%s" with positional args = %s, keyword kwargs = %s, attempt = %d',
                        func.__name__, args, kwargs, attempt
                    )
                    result = func(*args, **kwargs)
                    logging.info('Attempt %d result = %s', attempt, result)
                    return result
                except ignored_exceptions as ex:
                    logging.info('Attempt %d exception = %s: %s', attempt, type(ex).__name__, ex)
                    raise
                except Exception as ex:
                    logging.info('Attempt %d exception = %s: %s', attempt, type(ex).__name__, ex)
                    if attempt == retries:
                        raise
                    attempt += 1
            return None  
        return wrapper
    return decorator