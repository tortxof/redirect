FROM python:3.6
MAINTAINER Daniel Jones <tortxof@gmail.com>

RUN groupadd -r app && useradd -r -g app app

COPY docker_requirements.txt /app/requirements.txt
WORKDIR /app
RUN pip install -r requirements.txt
COPY . /app/

USER app

EXPOSE 5000

CMD ["uwsgi", "--yaml", "uwsgi.yaml"]
