#!/bin/bash
pipenv run pylint --max-line-length=180 TDG/core/*.py
pipenv run pylint --max-line-length=180 TDG/web_app/*.py
exit 0
