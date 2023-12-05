# https://www.baeldung.com/linux/nginx-docker-container

#  Pull the minimal Ubuntu image
FROM nginx

# Copy the Nginx config
COPY default /etc/nginx/conf.d/default.conf

# docker build -t nginx-m-servers .
# docker run --rm --name testserver -d -p 80:80 nginx-m-servers
# docker run -d -p 80:80 -p 9001:9001 -p 9002:9002 nginx-m-servers
# docker stop testserver
# curl localhost:80 -H "Host: example.com"
# curl localhost:80 -H "Host: abc.example.com"