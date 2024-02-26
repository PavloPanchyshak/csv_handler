import pandas as pd
from sqlalchemy import create_engine
from retry import retry

from csv_handler.settings import settings


class DBHandler:

    def __init__(self, user_name: str, user_password: str, host: str, port: int, db_name: str):
        self.user_name = user_name
        self.user_password = user_password
        self.host = host
        self.port = port
        self.db_name = db_name

    def __enter__(self):
        self.engine = create_engine(
            f'postgresql://{self.user_name}:{self.user_password}@{self.host}:{self.port}/{self.db_name}'
        )
        self.conn = self.engine.connect()
        return self

    def __exit__(self, exception_type, exception_value, exception_traceback):
        self.conn.close()

    @retry(tries=settings.retry_attempts)
    def save_data_to_db(self, data_frame: pd.DataFrame, table_name: str):
        data_frame.to_sql(table_name, con=self.engine, if_exists='append', index=False)
