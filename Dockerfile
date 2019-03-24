FROM python:3.6.7
RUN pip install pipenv
WORKDIR /usr/promisoria
COPY ./Pipfile ./Pipfile
COPY ./Pipfile.lock ./Pipfile.lock
RUN pipenv install
COPY . .
EXPOSE 8000
