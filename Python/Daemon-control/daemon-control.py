from os import getpid, path, remove

file_path = '/var/run/test.pid'


def daemon_control(file_path):
	if not path.exists(file_path):
		file = open(file_path, 'w+')
		file.write(str(getpid()))
		file.close()
		return True
	else:
		return False

def main():
	if daemon_control(file_path):
		print 'Execute script'
		## Code

		## Code
		remove(file_path)
	else:
		print 'No execute script'


if __name__ == '__main__':
	main()