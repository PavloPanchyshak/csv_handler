#!/bin/bash

poetry run pytest --cov=csv_handler --cov-report=html:coverage ./tests/
