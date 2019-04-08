import gevent
import time
import random

from gevent import monkey

monkey.patch_all()


def f(work_name):
	for i in range(10):
		print(gevent.getcurrent(), i, work_name)
		time.sleep(0.5)

# g1 = gevent.spawn(f, 5)
# g2 = gevent.spawn(f, 5)
# g3 = gevent.spawn(f, 5)
# g1.join()
# g2.join()
# g3.join()


gevent.joinall([
	gevent.spawn(f, "work_1"),
	gevent.spawn(f, "work_2"),
	gevent.spawn(f, "work_3"),
	gevent.spawn(f, "work_4"),
	gevent.spawn(f, "work_5"),
	gevent.spawn(f, "work_6"),
	])
