FROM python:3.6
WORKDIR /usr/app
RUN pip install pipenv
COPY ./Pipfile ./Pipfile
RUN pipenv install
COPY . .
EXPOSE 8000
