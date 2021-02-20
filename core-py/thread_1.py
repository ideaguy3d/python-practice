import threading
from queue import Queue
import time


def testThread(num):
    print(num)


for i in range(5):
    t = threading.Thread(target=testThread, args=(i,))
    t.start()


debug = 1


# end of file