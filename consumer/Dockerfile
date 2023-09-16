FROM python:3.10-slim-buster 

WORKDIR /app

COPY consumer.py /app/consumer.py
COPY requirements.txt /app/requirements.txt

RUN apt-get update && \
    apt-get install -y default-jre wget  

RUN pip3 install -r requirements.txt

CMD ["python3", "consumer.py"]
