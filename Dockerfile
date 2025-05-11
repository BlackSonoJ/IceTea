FROM python:3.13-slim

EXPOSE 8000

ENV PYTHONUNBUFFERED=1 \
    PYTHONUNBUFFERED=1


COPY  ./requirements.txt .

WORKDIR /IceTea

COPY . /IceTea

ENTRYPOINT [ "unicorn", "app.main:app", "--port", "8000", "--host", "0.0.0.0"]