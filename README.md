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

## creating CPU load on the server 

the server can use stress-ng to create CPU load on the webserver.  Command line parameters are given as query parameters. Following example shows how this is done:
```bash
 wget -q -O- "85.215.50.162:9991/stress-ng?timeout=10s&cpu=0
```
*NOTE*: There is no error information in the HTTP response, should the command fail. You will need to test your command by running httpserver.py in a terminal window. 
*NOTE:* use only the "long" parameters with a value e.g. '--cpu xx' etc. Short parameters (e.g. -q), or parameters without a value are not supported.
*NOTE*: You will need to install the stress-ng package first (for example "sudo apt install stress-ng" on ubuntu)

Studying the script source code a bit, you should be able add any other shell commands to the script.
