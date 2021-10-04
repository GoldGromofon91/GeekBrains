FROM python:3.8
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN apt-get update && \
    apt-get install -y postgresql postgresql-contrib libpq-dev python3-dev

WORKDIR /backend/
COPY /build/requirements.txt /backend/
RUN pip install --upgrade pip && pip install -r /backend/requirements.txt
COPY /server/ /backend/server/
COPY /build/_check_psql.sh /backend/
RUN chmod +x ./_check_psql.sh
RUN pip install gunicorn
