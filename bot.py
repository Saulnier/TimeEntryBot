#!/usr/local/bin/python3

from http.server import BaseHTTPRequestHandler,HTTPServer
from urllib.parse import parse_qs
import socketserver

PORT_NUMBER = 8080

class slackHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == "/":
            self.write("Adam's neat project timer project")
        elif self.path.startswith("/add_hours"):
            _, qs = self.path.split('?', 1)
            self.write("Adding hours.")
            # TODO(Evan) Add time to database here
        elif self.path == "/sum_hours":
            # TODO(Evan) Call to Adam's adder goes here
            self.write("Hours summed.")

    def write(self, text):
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        self.wfile.write(bytes(text, "utf-8"))

if __name__ == "__main__":
    try:
        server = HTTPServer (('', PORT_NUMBER), slackHandler)
        print("Server has been started on port ", PORT_NUMBER)
        server.serve_forever()
    except KeyboardInterrupt:
        print("^C received, shutting down the web server")
        server.socket.close()
