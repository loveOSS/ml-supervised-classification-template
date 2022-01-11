FROM python:3.9-slim

COPY requirements.txt /
RUN pip install -r /requirements.txt

COPY . /app
WORKDIR /app

EXPOSE 8501
ENTRYPOINT ["python"]
