from typing import Union

from pydantic import Field
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    rows_size: int = Field(2_000_000)
    string_size: int = Field(10)
    number_range: list[int] = Field([0, 100])
    double_range: list[Union[int, float]] = Field([0, 100])
    log_level: str = Field('INFO', validation_alias='LOG_LEVEL')
    batche_size: int = Field(100)
    db_user_name: str = Field('local_user')
    db_user_password: str = Field('local_user')
    db_host: str = Field('127.0.0.1')
    db_port: int = Field(5432)
    db_name: str = Field('csv_parser_db')
    retry_attempts: int = Field(3)


settings = Settings()
