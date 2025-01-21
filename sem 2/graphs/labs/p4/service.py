from domain import Graph
from random import randint


class Service:
    def __init__(self):
        self.graph = Graph()

    def get_graph(self):
        """Returns the graph."""
        return self.graph

    def get_vertices(self):
        """Returns the vertices of the graph."""
        return self.graph.get_vertices()

    def edge_exists(self, x: int, y: int):
        """Checks if an edge exists between two vertices."""
        return self.graph.edge_exists(x, y)

    def add_edge(self, x: int, y: int, cost: int):
        """Adds an edge between two vertices.
        x: int - the starting vertex
        Y: int - the ending vertex
        cost: int - the cost of the edge"""
        if not (0 <= x < self.graph.get_num_vertices() and 0 <= y < self.graph.get_num_vertices()):
            raise ValueError("Vertices out of range")
        if self.graph.edge_exists(x, y):
            raise ValueError("Edge already exists")
        self.graph.add_edge(x, y, cost)

    def generate_random_data(self, vertices: int,  edges: int):
        """Generates a random graph with the given number of vertices and edges.
        vertices: int - the number of vertices
        edges: int - the number of edges"""
        if vertices <= 0 or edges <= 0:
            raise ValueError("Number of vertices and edges must be positive")
        if edges > vertices * (vertices - 1):
            raise ValueError("Too many edges for the given number of vertices")
        self.graph = Graph(vertices)
        self.graph.set_num_edges(edges)
        while edges > 0:
            start = randint(0, vertices - 1)
            end = randint(0, vertices - 1)
            while start == end or self.edge_exists(start, end):
                start = randint(0, vertices - 1)
                end = randint(0, vertices - 1)
            cost = randint(1, 20)
            self.add_edge(start, end, cost)
            edges -= 1

    def get_cost_edge(self, x: int, y: int):
        """Returns the cost of an edge.
        x: int - the starting vertex
        y: int - the ending vertex
        Returns: int - the cost of the edge"""
        if (x, y) not in self.graph.get_edges():
            raise ValueError("This edge {} is not in the graph".format((x, y)))
        return self.graph.get_cost_of_edge(x, y)

    def modify_cost(self, x: int, y: int, cost: int):
        """Modifies the cost of an edge.
        x: int - the starting vertex
        y: int - the ending vertex
        cost: int - the new cost of the edge
        Returns: int - the new cost of the edge"""
        if (x, y) not in self.graph.get_edges() and (y, x) not in self.graph.get_edges():
            raise ValueError("This edge {} is not in the graph".format((x, y)))
        if (x, y) in self.graph.get_edges():
            return self.graph.modify_edge(x, y, cost)
        return self.graph.modify_edge(y, x, cost)

    def remove_edge(self, x: int, y: int):
        """Removes an edge from the graph.
        x: int - the starting vertex"""
        if not self.graph.edge_exists(x, y):
            raise ValueError("Edge doesn't exist")
        self.graph.remove_edge(x, y)

    def read_graph(self, filename):
        """Reads a graph from a file.
        filename: str - the name of the file containing the graph."""
        file = open(filename, "r")
        v, e = file.readline().split()
        v, e = int(v), int(e)
        self.graph = Graph(v)
        for i in range(e):
            cost = 0
            x, y, cost = file.readline().split()
            x, y, cost = int(x), int(y), int(cost)
            self.graph.add_edge(x, y, cost)

    def write_graph(self, filename):
        """Writes the graph to a file.
        filename: str - the name of the file where the graph will be written."""
        file = open(filename, "w")
        file.write(str(self.graph.get_num_vertices()) + " " + str(self.graph.get_num_edges()) + "\n")
        for x, y in self.graph.get_edges():
            file.write(str(x) + " " + str(y) + " " + str(self.graph.get_cost_of_edge(x, y)) + "\n")

    def find(self, parent, i):
        if parent[i] != i:
            parent[i] = self.find(parent, parent[i])
        return parent[i]

    def union(self, parent, rank, x, y):
        root_x = self.find(parent, x)
        root_y = self.find(parent, y)

        if rank[root_x] < rank[root_y]:
            parent[root_x] = root_y
        elif rank[root_x] > rank[root_y]:
            parent[root_y] = root_x
        else:
            parent[root_y] = root_x
            rank[root_x] += 1

    def Kruskal(self):
        result = []
        edges = list(self.graph.get_edges())
        edges = [(x, y, self.graph.get_cost_of_edge(x, y)) for x, y in edges]
        edges = sorted(edges, key=lambda item: item[2])

        parent = []
        rank = []

        for node in range(self.graph.get_num_vertices()):
            parent.append(node)
            rank.append(0)

        e = 0
        i = 0

        while e < self.graph.get_num_vertices() - 1:
            u, v, w = edges[i]
            i += 1
            x = self.find(parent, u)
            y = self.find(parent, v)

            if x != y:
                e += 1
                result.append((u, v, w))
                self.union(parent, rank, x, y)

        print("Following are the edges:")
        for u, v, weight in result:
            print(f"{u} -- {v} == {weight}")
