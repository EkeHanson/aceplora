# logging_example.py isimli bir Python dosyası oluşturalım.
import logging

logger = logging.getLogger()
console = logging.StreamHandler()

format_str = "%(asctime)s\t%(levelname)s -- %(processName)s %(filename)s:%(lineno)s -- %(message)s"
console.setFormatter(logging.Formatter(format_str))

logger.addHandler(console)

logger.setLevel(logging.ERROR)
try:
    logger.debug("Process is started")
    result = 5 / 0
except Exception as e:
    logger.error("{} error occured, details in below".format(e), exc_info=True)
    print("You will see this line after full error details")
