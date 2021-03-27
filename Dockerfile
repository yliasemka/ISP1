FROM python:3.8

ENV TARGET /home/julia/GitHub/ISP/ver2/ver2

WORKDIR "${TARGET}"

COPY ver2.py "${TARGET}"

COPY requirements.txt "${TARGET}"

RUN set -ex \
	pip3 install --no-cache-dir -r requirements.txt \
	&& rm requirements.txt

CMD [ "python3", "ver2.py"]

