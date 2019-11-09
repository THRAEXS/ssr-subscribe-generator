# -*- coding: utf-8 -*-

import json, base64, time
from server import Start

CODING = 'UTF-8'

class Processer(object):
	def __init__(self):
		super(Processer, self).__init__()
		self.link = '%s:%d:%s:%s:%s:%s/?obfsparam=%s&protoparam=%s&remarks=%s&group=%s'

	def run(self):
		configs = None
		with open('configs/config.json') as f:
			configs = json.load(f)

		target = 'configs/ssr-links'
		with open(target, 'w') as f:
			for cfg in configs:
				b64_pass = self.b64encode(cfg['password'])
				b64_obfsparam = self.b64encode(cfg['obfs_param'])
				b64_protoparam = self.b64encode(cfg['protocol_param'])
				b64_group = self.b64encode(cfg.get('group', ''))
				b64_remarks = self.b64encode(cfg.get('remarks', ''))

				b64_link = self.b64encode(self.link % (cfg.get('server'), cfg.get('server_port'), 
					cfg.get('protocol'), cfg.get('method'), cfg.get('obfs'), b64_pass, b64_obfsparam, 
					b64_protoparam, b64_remarks, b64_group))

				final_link = ('ssr://%s' % b64_link)
				print(final_link)
				f.write(final_link)
				f.write('\n')

		print('******************************************')
		with open(target) as f:
			data = f.read().encode(CODING)
			print('%s\n' % data)
			final = base64.b64encode(data).decode(CODING) 
			print(final)

			with open('configs/ssr-dist', 'w') as fo:
				fo.write(final)

	def b64encode(self, s):
		return base64.urlsafe_b64encode(s.encode(CODING)).decode(CODING).rstrip('=')

if __name__ == '__main__':
	# Processer().run()
	# run()
	Start().UP()
