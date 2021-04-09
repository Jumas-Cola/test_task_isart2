FROM python:3
ENV PYTHONUNBUFFERED=1
WORKDIR /srv/www/isart2
COPY requirements.txt /srv/www/isart2
RUN pip install -r requirements.txt
COPY . /srv/www/isart2
COPY checks.py /usr/local/lib/python3.9/site-packages/rest_registration/
ENTRYPOINT sh docker-entrypoint.sh
