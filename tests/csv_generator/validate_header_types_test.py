import pytest

from csv_handler.csv_generator.utils import validate_header_types


class TestValidateHeaderTypes:

    @staticmethod
    def test_valid_header_types():
        assert validate_header_types(['string', 'integer', 'boolean', 'double']) is None

    @staticmethod
    def test_invalid_header_types():
        with pytest.raises(ValueError):
            validate_header_types(['string', 'integer', 'boolean', 'double', 'byte'])
