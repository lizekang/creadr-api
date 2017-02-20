FROM ubuntu:16.04

# no tty
ENV DEBIAN_FRONTEND noninteractive


RUN apt-get update --fix-missing
RUN apt-get install -y python python-pip python-virtualenv nginx supervisor
#RUN apt-get install -y python-dev libffi-dev libssl-dev
RUN mkdir -p deploy
WORKDIR deploy

COPY creadr creadr
COPY test test
COPY requirements.txt ./
COPY manage.py ./

RUN pip install --upgrade pip
#RUN pip install --upgrade pyopenssl ndg-httpsclient pyasn1
RUN pip install -r ./requirements.txt

# Setup nginx
RUN rm /etc/nginx/sites-enabled/default
COPY conf/flask.conf /etc/nginx/sites-available/

RUN ln -s /etc/nginx/sites-available/flask.conf /etc/nginx/sites-enabled/flask.conf
RUN echo "daemon off;" >> /etc/nginx/nginx.conf

# Setup supervisord
RUN mkdir -p /var/log/supervisor
COPY conf/supervisord.conf /etc/supervisor/conf.d/supervisord.conf
COPY conf/gunicorn.conf /etc/supervisor/conf.d/gunicorn.conf

# expose port(s)
EXPOSE 80

# Start processes
CMD ["supervisord"]
