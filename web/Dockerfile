FROM python:3.6

RUN apt-get update \
    && apt-get install -y \
       libfontenc1 \
       libxfont1 \
       xfonts-encodings \
       xfonts-utils \
       xfonts-base \
       xfonts-75dpi \
       xvfb \
       wkhtmltopdf

COPY requirements.txt /home/docker/code/

RUN pip3 install -r /home/docker/code/requirements.txt

COPY . /home/docker/code/

WORKDIR /home/docker/code
