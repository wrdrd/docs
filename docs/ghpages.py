#!/usr/bin/env python
"""
A very-simple static files HTTP server,
which appends .html to paths that do not end with /

"""

import os
import sys

try:
    import SimpleHTTPServer
    import SocketServer
except ImportError:
    import http.server as SimpleHTTPServer
    import socketserver as SocketServer


class AppendHTMLRequestHandler(SimpleHTTPServer.SimpleHTTPRequestHandler):

    @staticmethod
    def rewrite_path(path):
        if not path.endswith('/'):
            if '..' in path:
                raise Exception()
            if os.path.exists('.' + path) or path.endswith('.html'):
                return path
            path_dot_html = path + ".html"
            disk_path = '.' + path_dot_html
            if os.path.exists(disk_path) and os.path.isfile(disk_path):
                return path_dot_html
            else:
                return path
        else:
            return path

    def do_GET(self):
        self.path = self.rewrite_path(self.path)
        return SimpleHTTPServer.SimpleHTTPRequestHandler.do_GET(self)


def main():
    server = SocketServer.TCPServer(('0.0.0.0', 8080), AppendHTMLRequestHandler)
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        server.shutdown()
        sys.exit(0)

if __name__ == "__main__":
    main()
