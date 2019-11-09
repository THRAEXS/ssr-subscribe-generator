# -*- coding: utf-8 -*-

def underline(s):
	return '\033[4;37;40m%s\033[0m' % s

def red(s):
	return '\033[0;31;40m%s\033[0m' % s

def green(s):
	return '\033[0;32;40m%s\033[0m' % s

def yellow(s):
	return '\033[0;33;40m%s\033[0m' % s

def blue(s):
	return '\033[0;34;40m%s\033[0m' % s

def cyan(s):
	return '\033[0;36;40m%s\033[0m' % s

def error(s):
	print('[%s] %s' % (red('ERROR'), s))

def warning(s):
	print('[%s] %s' % (yellow('WARNING'), s))

def info(s):
	print('[%s] %s' % (blue('INFO'), s))

if __name__ == '__main__':
	print(red('red'))
	print(green('green'))
	print(yellow('yellow'))
	print(blue('blue'))
	print(cyan('cyan'))

	error("error")
	warning('warning')
	info('info')
