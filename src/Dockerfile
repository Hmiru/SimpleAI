FROM python:3.11

RUN pip install poetry

COPY ./modelAPI /root/src/modelAPI

WORKDIR /root/src/modelAPI

RUN poetry install

CMD poetry install && poetry run python modelapi/modelapi.py