FROM python:3.9

COPY . /test/producer

WORKDIR /test/producer

RUN pip install --no-cache-dir -r requirements.txt

CMD ["python", "producer.py"]