from greenlet import greenlet
import time


def test_1():
	while True:
		print("-----1-----")
		gr2.switch()
		time.sleep(0.1)
		


def test_2():
	while True:
		print("-----2-----")
		gr1.switch()
		time.sleep(0.1)
	


def main():
	
	gr1 = greenlet(test_1)
	gr2 = greenlet(test_2)

	gr1.switch()



if __name__ == "__main__":
	main()

