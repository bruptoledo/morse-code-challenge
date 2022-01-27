FROM python:3.8.10

WORKDIR /app/
ENV PYTHONPATH="/app/"

COPY requirements.txt .
COPY back/ .

RUN pip install -r requirements.txt

ENTRYPOINT ["/bin/bash", "/app/back/entrypoint.sh"]