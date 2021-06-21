FROM python:3.7-buster
RUN apt-get update && apt-get install nginx vim -y --no-install-recommends
COPY nginx.default /etc/nginx/sites-available/default
RUN ln -sf /dev/stdout /var/log/nginx/access.log \
    && ln -sf /dev/stderr /var/log/nginx/error.log
RUN mkdir -p /opt/server
RUN mkdir -p /opt/server/pip_cache
RUN mkdir -p /opt/server/main
COPY requirements.txt start-server.sh /opt/server/
COPY .pip_cache /opt/server/pip_cache/
COPY ./ /opt/server/main/
WORKDIR /opt/server
RUN pip install -r requirements.txt --cache-dir /opt/server/pip_cache
RUN chown -R www-data:www-data /opt/server

EXPOSE 8020
STOPSIGNAL SIGTERM
CMD ["/opt/server/start-server.sh"]