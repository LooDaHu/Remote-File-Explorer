from tornado.wsgi import WSGIContainer
from tornado.httpserver import HTTPServer
from tornado.ioloop import IOLoop
import socket
from app import app

address = socket.getaddrinfo(socket.gethostname(), None)
for item in address:
    print(item)
http_server = HTTPServer(WSGIContainer(app))
http_server.listen(port=8000, address="0.0.0.0")
IOLoop.instance().start()


