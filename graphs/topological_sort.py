from queue import Queue
from graph1 import *


def topological_sort(graph):
	# hold all vertices w/indegree 0, these are the vertices that can be visited next in topological sort
	queue = Queue()
	# hold the indegree of every vertex in the graph
	indegree_map = {}
	# initialize the indegrees of all vertices in graph
	for i in range(graph.num_vertices):
		indegree_map[i] = graph.get_indegree(i)
		# if the vertex has indegree 0 add it to the queue
		if indegree_map[i] == 0:
			queue.put(i)
	sorted_list = []
	while not queue.empty():
		vertex = queue.get()
		sorted_list.append(vertex)
		for v in graph.get_adjacent_vertices(vertex):
			indegree_map[v] = indegree_map[v] - 1
			if indegree_map[v] == 0:
				queue.put(v)
	if len(sorted_list) != graph.num_vertices:
		raise ValueError('Graph contains a cycle')
	print(sorted_list)
	pass


def test_topological_sort():
	g = AdjacencyMatrixGraph(9, directed=True)
	g.add_edge(0, 1)
	g.add_edge(1, 2)
	#g.add_edge(2, 0) # will create a cycle
	g.add_edge(2, 7)
	g.add_edge(2, 4)
	g.add_edge(2, 3)
	g.add_edge(1, 5)
	g.add_edge(5, 6)
	g.add_edge(3, 6)
	g.add_edge(3, 4)
	g.add_edge(6, 8)
	topological_sort(g)
	pass


test_topological_sort()


# end of file
