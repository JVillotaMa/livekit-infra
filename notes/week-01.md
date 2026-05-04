# Nginx

Nginx is a seerver, load balancer, reverse proxy and email server. It can be used for a lot of things, but i am using it for serving static content for my livekit to run.

Nginx is composed of one main process and various other workers processes. The first one is responsible for reading and mantaingnng the configuration and to set the correct number of workers. The seconds, are the ones actually serving the content.
Nginx employs events based omdels and OS-dependant mechanism to ensure the correct load balancer between workers.

Number of workers is defined in the configuration file or limited automatically by the number of cores in the CPU.

## Starting stopping and reading the config
For starting nginx, we just run the executable. THe configuration lives in /etc/nginx/nginx.conf in nginx version nginx/1.29.8.

nginx               -> Starts
nginx -s quit       -> Shutdown the server
nginx -s reload     -> Reload the configuration file

## Configuration file
It normally lives in /etc/nginx/nginx.conf.

### Structure
Nginx is based on modules, which are controlled by directives. We can use simple directives, the one liners configurations that ends with a semicolon and the block directives that are controled in { }. A block directive can have more block directives inside.

The directives have context. In this example: the user and http are in the main context and the server is in the http context. The lines statign with # are comments
```
user user;

# My server
http {
    server{
    }
}
```
## Serving static content

Static files can easily be served using nignx locations and http server. Depending on the request, the file will be served in different directories.

We can follow the exmaple.
The configuration file normally hace severlab server block, depending on the port they are listening to or server names. Once nginx decides which server processes a request, it tests the URI specified in the request’s header against the parameters of the location directives defined inside the server block.

http{
    server{
    }
}


Then we can add the location block to the server block:
```
location / {
    root /data/www
}
```

Location block specifies the "/" prefix. That prefix is compared with the URI from the request. If a request matches with that "/" it will be added to the root directory in the local system. 
Example: if a request arrives wanting to fetch /index.html, the URI will match with / and nginx will try to serve the file in the /data/www/index.html

Next: adding another second location block
localtion /images/ {
    root /data
}

That will match with URIs requesting /images/cat.png and the local system will be looking at /data/images/cat.png

It will be a match for requests starting with /images/ (location / also matches such requests, but has shorter prefix).

**CRITICAL** Lots of locations can match with the URI but ONLY the biggest match will be served.

I have achieved to understand nginx and how to serve statinc content with the server and i have been able to use the clien page that i used.

### Custom configuration file

I have been thinking if the cofig file can be writen in order to specify all , it seems that the food convention is to have a custom config file for the "site" but use the default one and that default to import the custom one. with include <route>.

THis is the way for docker and will be used continousely.