from queue import Queue
from graph1 import *


def breadth_first(graph, start=0):
	queue = Queue()
	queue.put(start)
	visited = np.zeros(graph.num_vertices)
	while not queue.empty():
		vertex = queue.get()
		if visited[vertex] == 1:
			continue
		print("Visit: ", vertex)
		visited[vertex] = 1
		for v in graph.get_adjacent_vertices(vertex):
			if visited[v] != 1:
				queue.put(v)


# TRY OUT CODE
debug = 1


# end of file