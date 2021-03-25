#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import socketserver
from logging import StreamHandler, FileHandler, Formatter, getLogger
from logging import INFO

HOST = ""
PORT = 5555

logger = getLogger(__name__)
logger.setLevel(INFO)

#file handler
fh = FileHandler("log/access.log")
fh.setLevel(INFO)

#console handler
ch = StreamHandler()
ch.setLevel(INFO)

fmt = Formatter("%(asctime)s %(message)s")
fh.setFormatter(fmt)
ch.setFormatter(fmt)

logger.addHandler(fh)
logger.addHandler(ch)

class TelnetServer(socketserver.BaseRequestHandler):

    def handle(self):
        while True:
            self.data = self.request.recv(4096)
            if not self.data: break
            logger.info((self.data, self.client_address[0]))

if __name__ == "__main__":

    print("TCPHoneypot starting on %s" % PORT)
    with socketserver.ThreadingTCPServer((HOST, PORT), TelnetServer) as server:
        try:
            server.serve_forever()
        except KeyboardInterrupt:
            pass
