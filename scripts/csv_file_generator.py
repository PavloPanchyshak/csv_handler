import os
from argparse import ArgumentParser
from argparse import RawTextHelpFormatter
from typing import Union

from csv_handler.csv_generator.csv_generator import CSVGenerator
from csv_handler.csv_generator.utils import HeaderTypes
from csv_handler.settings import settings
from csv_handler.utils.log import Log

SCRIPT_DESCRIPTION = \
    '************************************ Script Description **************************************\n' \
    '******** This script is for the generation new CSV file with randomly generated data. ********\n' \
    '************************************* End Description ****************************************\n'


parser = ArgumentParser(description=SCRIPT_DESCRIPTION, formatter_class=RawTextHelpFormatter)
parser.add_argument('-f', '--file_name', help='File name to save result.', required=True)
parser.add_argument('--header', nargs="*", help='List of headers', required=True)
parser.add_argument(
    '--header_types',
    nargs="*",
    help=f'List of header types. Important should have the same position and count as headers.\n'
         f'Existing types {",".join([header_type.name for header_type in HeaderTypes])}',
    required=True,
)
parser.add_argument(
    '--string_size',
    help='The maximum length of string values to be generated',
    default=settings.string_size
)
parser.add_argument('--rows_size',  help='The number of rows in the file', default=settings.rows_size)
parser.add_argument(
    '--number_range',
    nargs="*",
    help='The range for generating integer values. Example: number_range 0 10',
    default=settings.number_range,
)

parser.add_argument(
    '--double_range',
    nargs="*",
    help='The range for generating integer values. Example: double_range 0 10',
    default=settings.double_range,
)


def main(
    file_name: str,
    rows_size: int,
    header: list[str],
    header_types: list[str],
    string_size: int,
    number_range: list[int],
    double_range: list[Union[int, float]]
):
    int_start_range, int_end_range = number_range
    float_start_range, float_end_range = double_range
    csv_generator = CSVGenerator(
        file_name,
        rows_size,
        header,
        header_types,
        string_size,
        int_start_range,
        int_end_range,
        float_start_range,
        float_end_range,
    )
    csv_generator.generate_csv_file()


if __name__ == '__main__':
    args = parser.parse_args()
    Log.info('Started generation of CSV file')
    main(
        args.file_name,
        args.rows_size,
        args.header,
        args.header_types,
        args.string_size,
        args.number_range,
        args.double_range,
    )
    Log.info(f'Finished generation of CSV file.\nFile path: {os.getcwd()}/{args.file_name}')
