import numpy as np

size = 1000000
my_arr = np.arange(size)
my_list = list(range(size))


def performance_comparison_1():
	print("Starting NumPy")
	for _ in range(10):
		my_arr2 = my_arr * 2
	print("Ending NumPy")
	
	print("\n\nStarting Python List")
	for _ in range(10):
		my_list2 = [x * 2 for x in my_list]
	print("Ending Python List")
	pass


data = np.random.randn(2, 3)
arr1 = np.array([[6, 7.5, 8, 0, 1]])
print(arr1)

data2 = [[1, 2, 3, 4], [5, 6, 7, 8]]
arr2 = np.array(data2)
arr2_dim = arr2.ndim
arr2_sh = arr2.shape
arr2_type = arr2.dtype

zero1 = np.zeros(10)
zero2 = np.zeros((10, 10))

arr3 = np.arange(5)
arr3b = np.arange(5)
arr4 = np.array([arr3, arr3b])

arr1 = np.array([[1., 2., 3.], [4., 5., 6.]])
arr2 = np.array([[0., 4., 1.], [7., 2., 12.]])
agt = arr1 > arr2

arr = np.arange(10)
arr[5:8] = 12
arr_slice = arr[5:8]
arr_slice_c = arr[5:8].copy()


def ndim_prac():
	arr = [0, 1, 2, 3, 4, 64, 64, 64, 8, 9]
	arr = np.array(arr)
	# slicing is similar to python
	arr_slice1 = arr[1:6]
	arr2d = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
	# traverse a np 2d arr, m1 & m2 are the same
	m1 = arr2d[0][2]  # 3
	m2 = arr2d[0, 2]  # 3
	# slice the 2d arr, i.e. select the 1st two rows
	arr2d_slice1 = arr2d[:2]
	# select the 1st two rows AND the 2nd column onward
	arr2d_slice2 = arr2[:2, 1:]
	
	arr3d = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])
	o_values = arr3d[0].copy()
	arr3d[0] = 42
	pass


ndim_prac()

debug = 1




# end of file
