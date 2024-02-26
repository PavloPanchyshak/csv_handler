import logging

from csv_handler.settings import settings


class Log:
    logger = None
    numeric_level = None

    @classmethod
    def init(cls):
        log_level = settings.log_level
        cls.numeric_level = getattr(logging, log_level, None)
        if not isinstance(cls.numeric_level, int):
            raise ValueError(f'Invalid log level: {log_level}')
        cls.logger = logging.getLogger()
        cls.logger.setLevel(cls.numeric_level)
        handler = logging.StreamHandler()
        handler.setLevel(cls.numeric_level)
        cls.logger.addHandler(handler)

    @classmethod
    def check(cls):
        if cls.logger is None:
            cls.init()

    @classmethod
    def info(cls, mess):
        cls.check()
        cls.logger.info(mess)
