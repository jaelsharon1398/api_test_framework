import time
import logging

# -----------------------------
# Setup simple logger
# -----------------------------
logger = logging.getLogger("retry_logger")
logger.setLevel(logging.DEBUG)

# Console handler
ch = logging.StreamHandler()
ch.setLevel(logging.DEBUG)
formatter = logging.Formatter("%(asctime)s | %(levelname)s | %(message)s", "%Y-%m-%d %H:%M:%S")
ch.setFormatter(formatter)
logger.addHandler(ch)

# -----------------------------
# Retry decorator
# -----------------------------
def retry(max_attempts=3, backoff=1, allowed_exceptions=(Exception,)):
    """
    Retry a function if it raises an exception.

    Args:
        max_attempts (int): Max number of tries
        backoff (int/float): Base sleep time between retries (seconds)
        allowed_exceptions (tuple): Exceptions that trigger retry
    """
    def decorator(func):
        def wrapper(*args, **kwargs):
            attempt = 1
            while True:
                try:
                    logger.debug(f"Attempt {attempt} for {func.__name__}")
                    result = func(*args, **kwargs)
                    logger.debug(f"Success on attempt {attempt} for {func.__name__}")
                    return result
                except allowed_exceptions as e:
                    logger.warning(f"Attempt {attempt} failed: {e}")
                    if attempt >= max_attempts:
                        logger.error(f"All {max_attempts} attempts failed for {func.__name__}")
                        raise
                    sleep_time = backoff * (2 ** (attempt - 1))  # exponential backoff
                    logger.info(f"Sleeping {sleep_time} seconds before retrying...")
                    time.sleep(sleep_time)
                    attempt += 1
        return wrapper
    return decorator
