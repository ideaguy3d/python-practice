import numpy as np
import time

a = np.random.random(int(1e8))


def pure_python():
	print('starting pure_python() time')
	start = time.time()
	sum(a) / len(a)  # compute mean
	# 14.950001001358032  pure_python() seconds
	print('\t', time.time() - start, 'pure_python() seconds')


def c_fortran():
	print('starting c_fortran() time')
	start = time.time()
	np.mean(a)  # compute mean
	# 0.10599851608276367 c_fortran() seconds
	print('\t', time.time() - start, 'c_fortran() seconds')
	


# pure_python()
c_fortran()





# end of file
