# httpserver
simple/dummy python http server for testing and troubleshooting The server
prints the request and sends the request also to the client. Bind address
and the port are required. 

*Examples:*
```
# accept all request, local and external on port 8090
python3 httpserver.py 0.0.0.0:8090

# accept only local requsts on port 80
python3 httpserver.py localhost:80
```

*Example output*
```
10.7.224.225 - - [09/Oct/2023 12:21:40] "GET /hello HTTP/1.1" 200 -
host: 212.227.224.120
cache-control: max-age=0
upgrade-insecure-requests: 1
user-agent: Mozilla/5.0 (Windows ...
--------------------------------------------------------------------------------
10.7.224.225 - - [09/Oct/2023 12:21:40] "GET /. HTTP/1.0" 200 -
content-length: 0
--------------------------------------------------------------------------------
.
.
.
```

