import os
import logging
import sys

FORMAT = "%(asctime)s - (%(name)s) - %(levelname)s - %(message)s"

logging.basicConfig(format=FORMAT)

logger = logging.getLogger()
logger.setLevel(logging.INFO)

handler = logging.StreamHandler(sys.stdout)
for handler in logger.handlers:
    logger.removeHandler(handler)

logger.addHandler(handler)

DEBUG_MODE = os.getenv("DEBUG_MODE", False)

MS_HOST = os.getenv('MS_HOST', '0.0.0.0')

MS_PORT = os.getenv('MS_PORT', 8002)

