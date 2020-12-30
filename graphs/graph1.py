import abc
import numpy as np


class Node:
    def __init__(self, vertexId):
        self.vertexId = vertexId
        self.adjacency_set = set()

    def add_edge(self, v):
        if self.vertexId == v:
            raise ValueError(f'Vertex {v} cannot be adjacent to itself')
        self.adjacency_set.add(v)

    def get_adjacent_vertices(self):
        return sorted(self.adjacency_set)


class Graph(abc.ABC):
    def __init__(self, num_vertices, directed=False):
        self.num_vertices = num_vertices
        self.directed = directed

    @abc.abstractmethod
    def add_edge(self, v1, v2, weight):
        pass

    @abc.abstractmethod
    def get_adjacent_vertices(self, v):
        pass

    @abc.abstractmethod
    def get_indegree(self, v):
        pass

    @abc.abstractmethod
    def get_edge_weight(self, v1, v2):
        pass

    @abc.abstractmethod
    def display(self):
        pass


class AdjacencyMatrixGraph(Graph):
    def __init__(self, num_vertices, directed=True):
        super(AdjacencyMatrixGraph, self).__init__(num_vertices, directed)
        self.matrix = np.zeros((num_vertices, num_vertices))

    def add_edge(self, v1, v2, weight=1):
        if v1 >= self.num_vertices or v2 >= self.num_vertices or v1 < 0 or v2 < 0:
            raise ValueError("Vert %d and %d are out of bounds" % (v1, v2))

        if weight < 1:
            raise ValueError("An edge cannot have weight < 1")

        self.matrix[v1][v2] = weight

        if not self.directed:
            self.matrix[v2][v1] = weight

    def get_adjacent_vertices(self, v):
        if v < 0 or v >= self.num_vertices:
            raise ValueError("Cannot access vert %d" % v)

        adjacent_vertices = []
        for i in range(self.num_vertices):
            if self.matrix[v][i] > 0:
                adjacent_vertices.append(i)

        return adjacent_vertices

    def get_indegree(self, v):
        if v < 0 or v >= self.num_vertices:
            raise ValueError("Vert %d is out of bounds" % v)

    def get_edge_weight(self, v1, v2):
        return self.matrix[v1][v2]

    def display(self):
        for i in range(self.num_vertices):
            for v in self.get_adjacent_vertices(i):
                print(i, "-->", v)


class AdjacencySetGraph(Graph):
    def __init__(self, num_vertices, directed=False):
        # class props
        self.vertex_list = []
        # invoke abstract class
        super(AdjacencySetGraph, self).__init__(num_vertices, directed)
        # construct list
        for i in range(num_vertices):
            self.vertex_list.append(Node(i))

    def add_edge(self, v1, v2, weight=1):
        if v1 >= self.num_vertices or v1 >= self.num_vertices or v1 < 0 or v2 < 0:
            raise ValueError(f'Vertices {v1} and {v2} are out of bounds')
        if weight != 1:
            raise ValueError('Weights must be 1')
        self.vertex_list[v1].add_edge(v2)
        # if undirected graph
        if not self.directed:
            self.vertex_list[v2].add_edge(v1)

    def get_adjacent_vertices(self, v):
        if v < 0 or v >= self.num_vertices:
            raise ValueError(f'Cannot access vertex {v}')
        return self.vertex_list[v].get_adjacent_vertices()

    def get_indegree(self, v):
        if v < 0 or v >= self.num_vertices:
            raise ValueError(f'Cannot access vertex {v}')
        indegree = 0
        for i in range(self.num_vertices):
            # ??? why do we pass in 'i' to get_adjacent_vertices() ???
            if v in self.get_adjacent_vertices(i):
                indegree = indegree + 1
        return indegree

    def get_edge_weight(self, v1, v2):
        return 1

    def display(self):
        for i in range(self.num_vertices):
            # ??? why do we pass in 'i' to get_adjacent_vertices() ???
            for v in self.get_adjacent_vertices(i):
                print(i, '-->', v)


# -----------------------------------------------------------------------------------


def use_adjacency_matrix_graph():
    g = AdjacencyMatrixGraph(4)
    g.add_edge(0, 1)
    g.add_edge(0, 2)
    g.add_edge(2, 3)
    for i in range(4):
        print("Adjacent to: ", i, g.get_adjacent_vertices(i))
    for i in range(4):
        print("Indegree: ", i, g.get_indegree(i))
    for i in range(4):
        for j in g.get_adjacent_vertices(i):
            print("Edge weight: ", i, " ", j, " weight: ", g.get_edge_weight(i, j))
    g.display()
    debug = 1


def use_adjacency_set_graph():
    NUM_VERTS = 4
    g = AdjacencySetGraph(NUM_VERTS, directed=False)
    g.add_edge(0, 1)
    g.add_edge(0, 2)
    g.add_edge(2, 3)
    #
    for i in range(NUM_VERTS):
        print('Adjacent to: ', i, g.get_adjacent_vertices(i))
    #
    for i in range(NUM_VERTS):
        print('Indegree: ', i, g.get_indegree(i))
    #
    for i in range(NUM_VERTS):
        for j in g.get_adjacent_vertices(i):
            print('Edge Weight: ', i, ' ', j, ' weight: ', g.get_edge_weight(i, j))


use_adjacency_set_graph()


# end of file
