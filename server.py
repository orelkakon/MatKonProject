import socketserver

from handler import HCIRequestHandler

Handler = HCIRequestHandler
server = socketserver.TCPServer(('0.0.0.0', 8080), Handler)

server.serve_forever()
