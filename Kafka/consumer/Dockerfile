FROM python:3.9-alpine

COPY . /test/consumer

WORKDIR /test/consumer

RUN pip install --no-cache-dir -r requirements.txt

CMD ["python","consumer.py"]