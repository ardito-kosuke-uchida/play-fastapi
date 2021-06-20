FROM python:3.9.5

ADD Pipfile Pipfile.lock /

RUN cd / && pip install pipenv && pipenv install --system
RUN pipenv install --dev --system

RUN mkdir /app
WORKDIR /app
