# -*- coding: utf-8 -*-

import json, base64, printc
from server import Start

CODING = 'UTF-8'

class Processer(object):
	def __init__(self):
		super(Processer, self).__init__()
		'''
		Please refer to: https://github.com/shadowsocksrr/shadowsocks-rss/wiki/SSR-QRcode-scheme
		ssr://base64(host:port:protocol:method:obfs:base64pass/?
			obfsparam=base64param&protoparam=base64param&remarks=base64remarks
			&group=base64group&udpport=0&uot=0)
		'''
		# self.link = '%s:%d:%s:%s:%s:%s/?obfsparam=%s&protoparam=%s&remarks=%s&group=%s'
		self.link = '{server}:{server_port}:{protocol}:{method}:{obfs}:{password}:/?\
			obfsparam={obfs_param}&protoparam={protocol_param}&remarks={remarks}&group={group}'

		self.params = [
			{ 'key': 'server' },
			{ 'key': 'server_port' },
			{ 'key': 'protocol' },
			{ 'key': 'method' },
			{ 'key': 'obfs' },
			{ 'key': 'password', 'b64': True },
			{ 'key': 'obfs_param', 'b64': True },
			{ 'key': 'protocol_param', 'b64': True },
			{ 'key': 'remarks', 'b64': True, 'default': 'THRAEX-NODE' },
			{ 'key': 'group', 'b64': True, 'default': 'THRAEX' }
		]

	def run_old(self):
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

		Start().UP()

	def run(self):
		printc.infoln('Loading configuration file...')

		printc.info('-------------------< %s >------------------' % 
			printc.cyan('ssr-subscribe-generator'))
		printc.info('Subscription Generator of SSR')
		printc.infoln('---------------------------[ %s ]---------------------------' %
			printc.cyan('Base64'))

		cfgs = self.configs()
		self.links(cfgs)

	def configs(self):
		cfg_path = 'configs/config.json'

		printc.info('---------------------< %s >--------------------' % 
			printc.cyan(cfg_path))

		configs = None
		try:
			with open(cfg_path) as f: configs = json.load(f)

			total = len(configs)

			if total > 0:
				printc.infoln('Total: %s. The original information is:' % total)

				for i in range(total):
					printc.info('Server %d:' % (i + 1))
					printc.info(printc.green((configs[i])))

				printc.info()
			else:
				printc.warning('No server node information.')
		except Exception as e:
			printc.error(e)

		return configs

	def links(self, cfgs):
		if not cfgs: return

		printc.info('---------------------< %s >--------------------' % 
			printc.cyan('Generate SSR links'))

		for i in range(len(cfgs)):
			ind = i + 1
			printc.info('Server %d:' % ind)
			for p in self.params:
				def_val = ''
				if 'default' in p: def_val = '%s-%d' % (p.get('default'), ind)

				bp = None
				if p.get('b64'): bp = self.b64encode(cfgs[i].get(p['key'], def_val))

				# print(p['key'], ': ', cfgs[i].get(p['key'], def_val), ', ', bp)
				preview_val = ''
				printc.info('\t\t%s: %s' % (p['key'], preview_val))
			printc.info()

	def b64encode(self, s):
		return base64.urlsafe_b64encode(s.encode(CODING)).decode(CODING).rstrip('=')

if __name__ == '__main__':
	Processer().run()
