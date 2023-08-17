# logging_file_example.py isimli bir Python dosyası oluşturalım.

import logging

logging.basicConfig(
    filename="logfile.txt",
    format="%(asctime)s - %(levelname)s - %(message)s",
    filemode="w",
    level=logging.ERROR,
)

logger = logging.getLogger()

try:
    logger.debug("Process is started")
    result = 5 / 0
except:
    logger.error("Exception thrown", exc_info=True)
    print("You will not see this line in log file, just a simple output")
