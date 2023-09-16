# FROM python:3.8
FROM python:3.10-slim-buster

WORKDIR /app

COPY producer.py /app/producer.py
COPY requirements.txt /app/requirements.txt

# Install Java and PySpark
RUN apt-get update && \
    apt-get install -y default-jre wget 

RUN pip3 install -r requirements.txt

CMD ["python3", "producer.py"]

 