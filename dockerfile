FROM python:3.9-slim
RUN python3 -m venv /space_odometer/venv
COPY requirements.txt /space_odometer/
RUN /space_odometer/venv/bin/pip3 install -r /space_odometer/requirements.txt
COPY . /space_odometer/
WORKDIR /space_odometer

ENTRYPOINT ["/space_odometer/venv/bin/python3", "odometer.py"]
