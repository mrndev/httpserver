s# Simple http server for troubleshooting and testing purposes. The server
# prints the request and sends the request also to the client. Bind address
# and the port are required. Examples:
#
# accept all request, local and external on port 8090
# pythonserver 0.0.0.0:8090 
# 
# accept only local requsts on port 80
# pythonserver localhost:80 

from http.server import BaseHTTPRequestHandler, HTTPServer
from urllib.parse import urlparse, parse_qs
import socket
import sys,os

class SimpleHTTPRequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        headers_str = str(self.headers)
        server_ip, server_port = self.request.getsockname()
        response_string=f"Hello from {socket.gethostname()} ({server_ip})\n\nyour request was:\n"+self.requestline+"\n"+headers_str
        response_string=response_string.encode("utf-8")
        self.send_header('Content-Length',len(response_string))
        self.end_headers()

        # Parse the request line
        parsed_path = urlparse(self.path)
        path = parsed_path.path
        query_params = parse_qs(parsed_path.query)

        # possibility to cause cpu load with stress-ng. The query parametes are translated to
        # long commandline options
        if path =="/stress-ng":
            cmdline_params=" ".join([f"--{x[0]}={x[1][0]}" for x in query_params.items()])
            cmd="stress-ng "+cmdline_params
            os.system(cmd)
        
        # Convert headers to a string and encode it to bytes
        print(headers_str.strip())
        try:
            self.wfile.write(response_string)
        except ConnectionResetError as e:
            print(e)
        print("-"*80)

try:
    bind,port = sys.argv[1].split(":")
    port=int(port)
except:
    print(f"usage: {sys.argv[0]} bind_andress:port")
    exit(1)

httpd = HTTPServer((bind, port), SimpleHTTPRequestHandler)
httpd.serve_forever()


