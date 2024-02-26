import string
import random
from typing import Union

import pandas as pd

from csv_handler.csv_generator.utils import HeaderTypes
from csv_handler.csv_generator.utils import validate_header_types


class CSVGenerator:

    OUTPUT_PATH = ...

    def __init__(
        self,
        file_name: str,
        rows_size: int,
        header: list[str],
        header_types: list[str],
        string_size: int,
        int_start_range: int,
        int_end_range: int,
        float_start_range: Union[int, float],
        float_end_range: Union[int, float],
    ):
        """
            CSVGenerator class for generation of new CSV files with random data.

            :param file_name: The name of the file being processed.
            :param rows_size: The number of rows in the file.
            :param header: The list contains column headers.
            :param header_types: The list contains data types for each column.
            :param string_size: The maximum length of string values to be generated.
            :param int_start_range: End range for generating integer values.
            :param int_end_range: Start range for generating integer values.
            :param float_start_range: End range for generating double values.
            :param float_end_range: Start range for generating double values.
        """
        self.file_name = file_name
        self.rows_size = rows_size
        self.header = header
        validate_header_types(header_types)
        self.header_types = header_types
        self.string_size = string_size
        self.int_start_range = int_start_range
        self.int_end_range = int_end_range
        self.float_start_range = float_start_range
        self.float_end_range = float_end_range

    def generate_csv_file(self):
        data = [self.generate_csv_row() for _ in range(self.rows_size)]
        data = pd.DataFrame(data, columns=self.header)
        data.to_csv(self.file_name, index=False)

    def generate_csv_row(self):
        row = []
        for header_type in self.header_types:
            match header_type:
                case HeaderTypes.STRING.value:
                    row.append(''.join(random.choices(string.ascii_uppercase + string.digits, k=self.string_size)))
                case HeaderTypes.DOUBLE.value:
                    row.append(random.uniform(self.float_start_range, self.float_end_range))
                case HeaderTypes.BOOLEAN.value:
                    row.append(random.choice([True, False]))
                case HeaderTypes.INTEGER.value:
                    row.append(random.randint(self.int_start_range, self.int_end_range))
        return row
