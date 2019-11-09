# -*- coding: utf-8 -*-

from http.server import HTTPServer, BaseHTTPRequestHandler
import socket, printc

CODING = 'UTF-8'

class Server(BaseHTTPRequestHandler):

	def do_GET(self):
		self.send_response(200)
		self.send_header('Content-type', 'text/plain;charset=utf-8')
		self.end_headers()

		with open('configs/ssr-dist', encoding = CODING) as f:
			self.wfile.write(f.read().encode(CODING))

class Start(object):
	def __init__(self):
		super(Start, self).__init__()

	def ip(self):
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
			s.connect(('8.8.8.8', 80))
			ip = s.getsockname()[0]
		except Exception as e:
			ip = 'localhost'
			print('Failed to get IP:', e)
		finally:
			s.close()

		return ip

	def UP(self):
		ip = self.ip()
		port = 9001

		server = HTTPServer((ip, port), Server)
		# print('Starting server, use <Ctrl-C> to stop')
		printc.info('Server is running at %s.' % 
			printc.underline('http://%s:%d/' % (ip, port)))
		printc.info('Press Ctrl+C to stop.')
		server.serve_forever()
