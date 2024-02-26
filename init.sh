#!/bin/bash
echo 'Install...'
set -e

echo 'Install poetry...'
curl -sSL https://install.python-poetry.org | python3 -
## Mac users
export PATH="$HOME/.local/bin:$PATH"
## Linux Users
#ENV POETRY_HOME="/opt/poetry"
#ENV PATH="${POETRY_HOME}/bin:${PATH}"

echo 'Remove old env...'
poetry env remove python3.11
echo 'Create new env...'
poetry env use python3.11
echo 'Poetry install packages...'
poetry install --no-interaction --no-ansi --no-cache --no-root

echo 'Install - Ok'