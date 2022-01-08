FROM python:3.9-slim
MAINTAINER fragarie 'fragarie@yandex.com'

COPY . /spaceodometer/
WORKDIR /spaceodometer

RUN python3 -m venv /spaceodometer/venv
RUN /spaceodometer/venv/bin/pip3 install -r requirements.txt

ENTRYPOINT ["/spaceodometer/venv/bin/python3", "odometer.py"]