# -*- coding: utf-8 -*-

from http.server import HTTPServer, BaseHTTPRequestHandler

class Server(BaseHTTPRequestHandler):
	# def __init__(self):
	# 	super(Server, self).__init__()

	def do_GET(self):
		self.send_response(200)
		self.send_header('Content-type', 'text/plain;charset=utf-8')
		self.end_headers()
		self.wfile.write('鬼王'.encode('utf-8'))

def run():
	a = ('localhost', 8080)
	s = HTTPServer(a, Server)
	s.serve_forever()
