from queue import Queue
from graph1 import *
import numpy as np


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
	e = 1


def depth_first(graph, visited, current=0):
	"""
	Depth-first search using recursion
	:param graph: A graph object
	:type graph: AdjacencyMatrixGraph
	:param visited: A list of visited nodes
	:type visited:
	:param current: The current node
	:type current:
	:return:
	:rtype:
	"""
	if visited[current] == 1:
		return
	visited[current] = 1
	print(f'Current node = {current}')
	for vertex in graph.get_adjacent_vertices(current):
		depth_first(graph, visited, vertex)
	e = 1


def test_breadth_first():
	g = AdjacencyMatrixGraph(9, directed=True)
	g.add_edge(0, 1)
	g.add_edge(1, 2)
	g.add_edge(2, 7)
	g.add_edge(2, 4)
	g.add_edge(2, 3)
	g.add_edge(1, 5)
	g.add_edge(5, 6)
	g.add_edge(6, 3)
	g.add_edge(3, 4)
	g.add_edge(6, 8)
	breadth_first(g, start=0)
	pass


def test_depth_first():
	g = AdjacencyMatrixGraph(9, directed=True)
	g.add_edge(0, 1)
	g.add_edge(1, 2)
	g.add_edge(2, 7)
	g.add_edge(2, 4)
	g.add_edge(2, 3)
	g.add_edge(1, 5)
	g.add_edge(5, 6)
	g.add_edge(6, 3)
	g.add_edge(3, 4)
	g.add_edge(6, 8)
	visited = np.zeros(g.num_vertices)
	depth_first(g, visited, current=0)
	pass


test_depth_first()
test_breadth_first()

# TRY OUT CODE
debug = 1


# end of file
