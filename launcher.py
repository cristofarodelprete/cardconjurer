"""
IMPORTS
"""
from http.server import SimpleHTTPRequestHandler, HTTPServer
import webbrowser
import os

"""
SETTINGS
"""

NAME = "localhost"
PORT = 9090
DIRECTORY = os.getcwd()

"""
REQUEST HANDLER
"""


class Handler(SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=DIRECTORY, **kwargs)

"""
START APP
"""

if __name__ == "__main__":
    webServer = HTTPServer((NAME, PORT), Handler)
    print("Server started http://%s:%s" % (NAME, PORT))

    try:
        webServer.serve_forever()
    except KeyboardInterrupt:
        pass

    webServer.server_close()
    print("Server stopped.")
