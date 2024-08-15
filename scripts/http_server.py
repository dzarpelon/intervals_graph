# scripts/http_server.py

import http.server
import socketserver

def start_http_server(directory, port=8080):
    # Directly set the handler's directory instead of changing the global working directory
    handler = http.server.SimpleHTTPRequestHandler
    handler.directory = directory  # Set the directory for the HTTP server to serve
    httpd = socketserver.TCPServer(("", port), handler)
    print(f"Serving at port {port}")
    httpd.serve_forever()
