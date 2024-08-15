# scripts/http_server.py

import http.server
import socketserver
import os

def start_http_server(directory, port=8080):
    # Change the current working directory to the output directory
    os.chdir(directory)
    handler = http.server.SimpleHTTPRequestHandler
    httpd = socketserver.TCPServer(("", port), handler)
    print(f"Serving at port {port}")
    httpd.serve_forever()
