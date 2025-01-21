from domain import Graph
from random import randint


class Service:
    def __init__(self, graph=None):
        if graph is None:
            self.graph = Graph()
            self.generate_random_data(5, 10)
        else:
            self.graph = graph
        self.edges = sorted(self.graph.get_edges(), key=lambda edge: self.graph.get_cost_of_edge(*edge))

    def get_graph(self):
        return self.graph

    def get_vertices(self):
        return self.graph.get_vertices()

    def edge_exists(self, x: int, y: int):
        return self.graph.edge_exists(x, y)

    def add_edge(self, x: int, y: int, cost: int):
        if not (0 <= x < self.graph.get_num_vertices() and 0 <= y < self.graph.get_num_vertices()):
            raise ValueError("Vertices out of range")
        if self.graph.edge_exists(x, y):
            raise ValueError("Edge already exists")
        self.graph.add_edge(x, y, cost)
        self.edges = sorted(self.graph.get_edges(), key=lambda edge: self.graph.get_cost_of_edge(*edge))

    def generate_random_data(self, vertices: int, edges: int):
        if vertices <= 0 or edges <= 0:
            raise ValueError("Number of vertices and edges must be positive")
        if edges > vertices * (vertices - 1):
            raise ValueError("Too many edges for the given number of vertices")
        self.graph = Graph(vertices)
        while edges > 0:
            start = randint(0, vertices - 1)
            end = randint(0, vertices - 1)
            while start == end or self.edge_exists(start, end):
                start = randint(0, vertices - 1)
                end = randint(0, vertices - 1)
            cost = randint(1, 20)
            self.add_edge(start, end, cost)
            edges -= 1
        self.edges = sorted(self.graph.get_edges(), key=lambda edge: self.graph.get_cost_of_edge(*edge))

    def remove_edge(self, x: int, y: int):
        if not self.graph.edge_exists(x, y):
            raise ValueError("Edge doesn't exist")
        self.graph.remove_edge(x, y)
        self.edges = sorted(self.graph.get_edges(), key=lambda edge: self.graph.get_cost_of_edge(*edge))

    def read_graph(self, filename):
        with open(filename, "r") as file:
            v, e = map(int, file.readline().split())
            self.graph = Graph(v)
            for _ in range(e):
                x, y, cost = map(int, file.readline().split())
                self.graph.add_edge(x, y, cost)
        self.edges = sorted(self.graph.get_edges(), key=lambda edge: self.graph.get_cost_of_edge(*edge))

    def write_graph(self, filename):
        with open(filename, "w") as file:
            file.write(f"{self.graph.get_num_vertices()} {self.graph.get_num_edges()}\n")
            for x, y in self.graph.get_edges():
                file.write(f"{x} {y} {self.graph.get_cost_of_edge(x, y)}\n")

    def modify_cost(self, x: int, y: int, cost: int):
        if not self.graph.edge_exists(x, y):
            raise ValueError(f"This edge ({x}, {y}) is not in the graph")
        self.graph.modify_edge(x, y, cost)
        self.edges = sorted(self.graph.get_edges(), key=lambda edge: self.graph.get_cost_of_edge(*edge))

    def get_cost_edge(self, x: int, y: int):
        if not self.graph.edge_exists(x, y):
            raise ValueError(f"This edge ({x}, {y}) is not in the graph")
        return self.graph.get_cost_of_edge(x, y)

    def isSafe(self, v, pos, path):
        # checks if an edge exists between the last vertex in the path and this new vertex
        if not self.graph.edge_exists(path[pos - 1], v):
            return False
        # already included in the path
        if v in path:
            return False
        return True

    def hamCycleUtil(self, path, pos):
        # all vertices were included in the path
        if pos == self.graph.get_num_vertices():
            # see if we can close the cycle
            if self.graph.edge_exists(path[pos - 1], path[0]):
                return True
            else:
                return False
        # edges sorted by cost
        for edge in self.edges:
            # edge[0] is the start vertex, edge[1] is the end vertex of an edge
            v = edge[1] if edge[0] == path[pos - 1] else edge[0]
            # check if the vertex can be included in the path
            if self.isSafe(v, pos, path):
                path[pos] = v
                # tries to continue the path recursively
                if self.hamCycleUtil(path, pos + 1):
                    return True
                path[pos] = -1
        return False

    def hamCycle(self):
        path = [-1] * self.graph.get_num_vertices()
        path[0] = 0
        if not self.hamCycleUtil(path, 1):
            print("Solution does not exist\n")
            return [], False
        return path, True
