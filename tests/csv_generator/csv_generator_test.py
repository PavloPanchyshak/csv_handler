import pytest

from csv_handler.csv_generator.csv_generator import CSVGenerator
import os


@pytest.fixture
def users_csv_path():
    folder_path = os.path.join(os.getcwd(), 'artifacts')
    file_path = os.path.join(folder_path, 'test.csv')

    try:
        yield {
            'folder_path': folder_path,
            'file_path': file_path,
        }
    finally:
        os.remove(file_path)


class TestCSVGenerator:

    @staticmethod
    def test_csv_generator_success(users_csv_path):

        csv_generator = CSVGenerator(
            file_name=users_csv_path['file_path'],
            rows_size=1,
            header=['col1', 'col2', 'col3', 'col4'],
            header_types=['string', 'integer', 'double', 'boolean'],
            string_size=5,
            int_start_range=1,
            int_end_range=10,
            float_end_range=10,
            float_start_range=1
        )

        csv_generator.generate_csv_file()

        assert 'test.csv' in os.listdir(users_csv_path['folder_path'])
