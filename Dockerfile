FROM python:3
ENV PYTHONBUFFERED 1
RUN mkdir /BlueRecog
WORKDIR /BlueRecog
COPY requirements.txt /BlueRecog/
RUN pip install -r requirements.txt
COPY . /BlueRecog/