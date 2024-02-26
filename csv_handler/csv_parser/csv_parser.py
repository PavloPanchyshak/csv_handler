import pandas as pd


class CSVParser:

    def __init__(self, file_name: str, batche_size: int):
        self.file_name = file_name
        self.batche_size = batche_size

    def read_csv(self):
        for row in pd.read_csv(self.file_name, chunksize=self.batche_size):
            yield row
