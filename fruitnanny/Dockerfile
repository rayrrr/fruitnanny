FROM balenalib/raspberrypi3-debian-node:12.13-buster

RUN echo 'APT::Install-Recommends "false";' >/etc/apt/apt.conf.d/00recommends \
    && echo 'APT::Install-Suggests "false";' >>/etc/apt/apt.conf.d/00recommends \
    && apt-get update && apt-get upgrade && apt-get install -y \
	dos2unix \
	libgpiod2 \
	python3 \
        python3-pip \
	wiringpi \
    && pip3 install --upgrade RPI.GPIO adafruit-blinka adafruit-circuitpython-dht \
    && apt-get --purge -y autoremove && apt-get clean && rm -rf /tmp/* && rm -rf /var/lib/apt/lists/*

ADD . /opt/fruitnanny
WORKDIR /opt/fruitnanny

RUN dos2unix /opt/fruitnanny/bin/* && npm install

CMD ["node", "server/app.js"]
EXPOSE 7000
