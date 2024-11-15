FROM python:3.12-slim-bullseye

WORKDIR /AlexaMusic
RUN chmod 777 /AlexaMusic

RUN apt-get -qq update && apt-get -qq -y upgrade
RUN apt-get install -y --no-install-recommends ffmpeg
RUN DEBIAN_FRONTEND=noninteractive apt-get install -y git gcc build-essential

RUN pip3 install -U pip
COPY requirements.txt .
RUN pip3 install --no-cache-dir -U -r requirements.txt

COPY . .

CMD ["python3", "-m", "AlexaMusic"]

FROM python:3.9.10

WORKDIR /app
COPY . /app

RUN pip3 install -U pip
COPY requirements.txt .
RUN pip3 install -U -r requirements.txt

CMD ["python3", "-m", "RoseTagger"]
