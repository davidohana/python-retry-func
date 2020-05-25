import logging
import sys

import retry


def do_something_that_always_fail():
    raise KeyError("test")


logger = logging.getLogger()
logger.setLevel(logging.INFO)
logger.addHandler(logging.StreamHandler(stream=sys.stdout))

logger.info("starting")
retry.retry(do_something_that_always_fail, ex_type=KeyError, logger=logger)
