import logging
import random
import sys

import retry

x = 10


def fail_randomly():
    y = random.randint(0, 10)
    if y < 10:
        y = 0
    return x / y


logger = logging.getLogger()
logger.setLevel(logging.INFO)
logger.addHandler(logging.StreamHandler(stream=sys.stdout))

logger.info("starting")
result = retry.retry(fail_randomly, expected_ex_type=ZeroDivisionError, limit=20, logger=logger)
logger.info("result is: %s", result)
