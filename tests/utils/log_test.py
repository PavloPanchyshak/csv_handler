import pytest

from csv_handler.settings import settings
from csv_handler.utils.log import Log


class TestLog:

    @staticmethod
    def test_create_log_obj_success():
        Log.init()

        assert Log.logger is not None
        assert Log.numeric_level is not None

    @staticmethod
    def test_log_info():
        Log.logger = None
        Log.numeric_level = None

        Log.info('Hello world')

        assert Log.logger is not None
        assert Log.numeric_level is not None

    @staticmethod
    def test_create_log_obj_error():
        settings.log_level = 'Invalid'
        with pytest.raises(ValueError):
            Log.init()
