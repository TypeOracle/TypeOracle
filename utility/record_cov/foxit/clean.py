import monitor
import time

if __name__ == '__main__':
	m = monitor.Monitor('test')
	while True:
		print('clean status')
		m.clearDerived()
		time.sleep(3600)