FROM python:3
ENV PYTHONUNBUFFERED 1
COPY . /app
WORKDIR /app
RUN pip install pipenv
RUN pipenv install --dev
RUN pipenv install
EXPOSE 8000
