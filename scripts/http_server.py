import http.server
import socketserver
import os
from contextlib import contextmanager

@contextmanager
def change_directory(directory):
    """Context manager for changing the working directory temporarily."""
    original_directory = os.getcwd()
    try:
        os.chdir(directory)
        yield
    finally:
        os.chdir(original_directory)

def start_http_server(directory, port=8080):
    with change_directory(directory):
        handler = http.server.SimpleHTTPRequestHandler
        httpd = socketserver.TCPServer(("", port), handler)
        print(f"Serving at port {port}")
        httpd.serve_forever()
