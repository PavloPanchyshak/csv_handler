import pathlib

import pandas as pd
import pytest

from csv_handler.csv_parser.csv_parser import CSVParser


@pytest.fixture
def users_csv_path():
    file_path = pathlib.Path("test.csv")
    data = [[i, 'str', True, 2.1] for i in range(100)]
    data = pd.DataFrame(data, columns=['col1', 'col2', 'col3', 'col4'])
    data.to_csv(file_path, index=False)
    try:
        yield file_path
    finally:
        file_path.unlink()


class TestCSVParser:

    @staticmethod
    def test_parse_csv_success(users_csv_path):
        csv_parser = CSVParser(users_csv_path, 10)
        for i, rows in enumerate(csv_parser.read_csv()):
            expected = [[i, 'str', True, 2.1] for i in range(i*10, 10 * (i+1))]
            assert expected == rows.values.tolist()
