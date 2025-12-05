#!/usr/bin/python3
"""Simple API using http.server serving JSON and text responses."""
from http.server import BaseHTTPRequestHandler, HTTPServer
import json


class SimpleAPIHandler(BaseHTTPRequestHandler):
    """Request handler for the simple API."""

    def _send_headers(self, status_code=200, content_type="text/plain"):
        """Helper method to send response headers."""
        self.send_response(status_code)
        self.send_header("Content-type", content_type)
        self.end_headers()

    def do_GET(self):
        """Handle GET requests."""
        if self.path == "/":
            # Root endpoint
            self._send_headers()
            self.wfile.write(b"Hello, this is a simple API!")
        elif self.path == "/data":
            # JSON data endpoint
            self._send_headers(content_type="application/json")
            data = {"name": "John", "age": 30, "city": "New York"}
            self.wfile.write(json.dumps(data).encode("utf-8"))
        elif self.path == "/status":
            # Status endpoint
            self._send_headers()
            self.wfile.write(b"OK")
        else:
            # Undefined endpoint
            self._send_headers(status_code=404)
            self.wfile.write(b"Endpoint not found")


def run(server_class=HTTPServer, handler_class=SimpleAPIHandler, port=8000):
    """Start the HTTP server."""
    server_address = ("", port)
    httpd = server_class(server_address, handler_class)
    print(f"Starting server on port {port}...")
    httpd.serve_forever()


if __name__ == "__main__":
    run()
