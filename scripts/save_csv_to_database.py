from argparse import ArgumentParser
from argparse import RawTextHelpFormatter

from csv_handler.csv_parser.csv_parser import CSVParser
from csv_handler.db_handler.handler import DBHandler
from csv_handler.settings import settings

SCRIPT_DESCRIPTION = \
    '************************************ Script Description **************************************\n' \
    '******** This script is for the parse CSV file and store data to database. ********\n' \
    '************************************* End Description ****************************************\n'


parser = ArgumentParser(description=SCRIPT_DESCRIPTION, formatter_class=RawTextHelpFormatter)
parser.add_argument('-f', '--file_name', help='File name to save result.', required=True)
parser.add_argument('--table_name', help='Data Base table name to save csv result.', required=True)
parser.add_argument(
    '--batche_size',
    help='The length of batch rows at a time',
    default=settings.batche_size
)


def main(file_name: str, batche_size: int, table_name: str):
    csv_parser_iterator = CSVParser(file_name, batche_size)
    with DBHandler(
        settings.db_user_name, settings.db_user_password, settings.db_host, settings.db_port, settings.db_name
    ) as db_handler:
        for data_frame in csv_parser_iterator.read_csv():
            db_handler.save_data_to_db(data_frame, table_name)


if __name__ == '__main__':
    args = parser.parse_args()
    main(args.file_name, args.batche_size, args.table_name)
