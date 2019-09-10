FROM python:3.5.2
RUN pip install pipenv
COPY . /TDG
WORKDIR /TDG
RUN pipenv install
WORKDIR /TDG/TDG

CMD ["pipenv", "run", "gunicorn", "-w 3", "-b :8080", "TDG_web:app"]