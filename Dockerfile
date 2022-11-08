FROM python:3.10.7-alpine

COPY requirements.txt /tmp/requirements.txt
RUN pip install -r /tmp/requirements.txt

WORKDIR /app
COPY . .

RUN sh scripts/migrate.sh

ENV PORT=1276
EXPOSE ${PORT}

CMD ["sh", "scripts/run.sh"]
