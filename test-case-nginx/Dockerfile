# https://www.baeldung.com/linux/nginx-docker-container

#  Pull the minimal Ubuntu image
FROM nginx

# Copy the Nginx config
COPY default /etc/nginx/conf.d/default.conf

# docker stop testserver
# docker build -t nginx-m-servers .
# docker run --rm --name testserver -d -p 80:80 nginx-m-servers
# curl localhost:80 -H "Host: example.com"
# curl localhost:80 -H "Host: abc.example.com"
# curl localhost:80 -H "Host: abc.nexample.com"