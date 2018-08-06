#!/usr/local/bin/python3

from http.server import BaseHTTPRequestHandler,HttpServer

PORT_NUMBER = 8080

class slackHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == "/":
            self.send_response(200)
            self.write("Adam's neat project timer.")
        elif self.path == "/time":

try:
    server = HTTPServer (('', PORT_NUMBER), slackHandler)
    print("Server has been started on port ", PORT_NUMBER)
    server.serve_forever()

except KeyboardInterrupt:
    print("^C received, shutting down the web server")
    server.socket.close()
