FROM python:3.10.7-alpine

COPY requirements.txt /tmp/requirements.txt
RUN pip install -r /tmp/requirements.txt

WORKDIR /app
COPY . .

CMD ["sh", "scripts/run.sh"]
