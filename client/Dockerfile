FROM nginx:alpine

COPY client_nginx.conf /etc/nginx/conf.d/
COPY index.html /usr/share/nginx/html/

EXPOSE 80

CMD ["nginx","-g","daemon off;"]