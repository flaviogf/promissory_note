FROM python:3.6
RUN pip install pipenv
COPY . .
RUN pipenv install
EXPOSE 8000
