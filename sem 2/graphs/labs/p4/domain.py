import copy


class Graph:
    def __init__(self, num_vertices=0):
        """
        Constructor for the Graph class.
        num_vertices: int - the number of vertices of the graph
        """
        self.__num_vertices = num_vertices  # the number of vertices of the graph
        self.__num_edges = 0
        self.__graph = {}

    def get_edges(self):
        """Returns the edges of the graph."""
        return self.__graph.keys()

    def get_num_vertices(self):
        """Returns the number of vertices of the graph."""
        return self.__num_vertices

    def set_num_vertices(self, num_vertices: int):
        """Sets the number of vertices of the graph."""
        self.__num_vertices = num_vertices

    def set_num_edges(self, num_edges: int):
        """Sets the number of edges of the graph.
        num_edges: int - the number of edges of the graph."""
        self.__num_edges = num_edges

    def get_num_edges(self):
        """Returns the number of edges of the graph."""
        return self.__num_edges

    def get_edge_by_key(self, key):
        """Returns the cost of an edge.
        key: tuple - the edge"""
        return self.__graph[key]

    def get_vertices(self):
        """Returns the vertices of the graph.
        Returns: list - the vertices of the graph."""
        return list(range(self.__num_vertices))

    def edge_exists(self, x: int, y: int):
        """Checks if an edge exists between two vertices.
        x: int - the starting vertex"""
        return (x, y) in self.__graph.keys() or (y, x) in self.__graph.keys()

    def add_edge(self, x: int, y: int, cost):
        """Adds an edge between two vertices.
        x: int - the starting vertex
        y: int - the ending vertex
        cost: int - the cost of the edge"""
        self.__graph[(x, y)] = cost
        self.__num_edges += 1

    def get_cost_of_edge(self, x: int, y: int):
        """Returns the cost of an edge."""
        if (x, y) not in self.__graph.keys() and (y, x) not in self.__graph.keys():
            return None
        if (x, y) in self.__graph.keys():
            return self.__graph[(x, y)]
        return self.__graph[(y, x)]

    def modify_edge(self, x: int, y: int, cost: int):
        """Modifies the cost of an edge.
        x: int - the starting vertex
        y: int - the ending vertex
        cost: int - the new cost of the edge
        Returns: int - the new cost of the edge"""
        self.__graph[(x, y)] = cost
        return self.__graph[(x, y)]

    def remove_edge(self, x: int, y: int):
        """Removes an edge from the graph.
        x: int - the starting vertex"""
        del self.__graph[(x, y)]
        self.__num_edges -= 1
