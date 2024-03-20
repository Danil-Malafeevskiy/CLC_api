FROM python:3.10

COPY requirements.txt requirements.txt

RUN pip install -r requirements.txt

COPY server server

ENV http_proxy=""
ENV https_proxy=""

CMD ["bash", "-c", "uvicorn server.main:app --host 0.0.0.0 --port 80"]