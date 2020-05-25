import time


def retry(func, ex_type=Exception, limit=0, wait_ms=100, wait_increase_ratio=2, logger=None):
    """
    Retry a function invocation until no exception occurs
    :param func: function to invoke
    :param ex_type: retry only if exception is subclass of this type
    :param limit: maximum number of invocation attempts
    :param wait_ms: initial wait time after each attempt in milliseconds.
    :param wait_increase_ratio: increase wait period by multiplying this value after each attempt.
    :param logger: if not None, retry attempts will be logged to this logging.logger
    :return: result of first successful invocation
    :raises: last invocation exception if attempts exhausted or exception is not an instance of ex_type
    """
    attempt = 1
    while True:
        try:
            return func()
        except Exception as ex:
            if not isinstance(ex, ex_type):
                raise ex
            if 0 < limit <= attempt:
                if logger:
                    logger.warning("no more attempts")
                raise ex

            if logger:
                logger.error("failed execution attempt #%d", attempt, exc_info=ex)

            attempt += 1
            if logger:
                logger.info("waiting %d ms before attempt #%d", wait_ms, attempt)
            time.sleep(wait_ms / 1000)
            wait_ms *= wait_increase_ratio
