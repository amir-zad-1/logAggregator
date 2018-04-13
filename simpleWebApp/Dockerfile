FROM xqdocker/ubuntu-nginx

ADD ./ /data/www/la/
COPY ./nginx.conf /etc/nginx/nginx.conf
COPY ./logAggregator /etc/nginx/sites-enabled/
EXPOSE 81
RUN apt-get update && apt-get install -y python3-pip
RUN apt-get clean
RUN pip3 install -r /data/www/la/requirements.txt
ENTRYPOINT python3 /data/www/la/app.py
#ENTRYPOINT service nginx reload
