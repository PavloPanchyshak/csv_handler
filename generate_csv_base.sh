#!/bin/bash

python -m scripts.csv_file_generator -f artifacts/input_data.csv  --header name size temperature fake_data type attempts avg_temperature country code city --header_types string integer double boolean string integer double string integer string
