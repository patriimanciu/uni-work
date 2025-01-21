class Graph:
    def __init__(self, num_vertices=0):
        self.__num_vertices = num_vertices
        self.__num_edges = 0
        self.__graph = {}

    def get_edges(self):
        return self.__graph.keys()

    def get_num_vertices(self):
        return self.__num_vertices

    def set_num_vertices(self, num_vertices: int):
        self.__num_vertices = num_vertices

    def set_num_edges(self, num_edges: int):
        self.__num_edges = num_edges

    def get_num_edges(self):
        return self.__num_edges

    def get_edge_by_key(self, key):
        return self.__graph[key]

    def get_vertices(self):
        return list(range(self.__num_vertices))

    def edge_exists(self, x: int, y: int):
        return (x, y) in self.__graph.keys() or (y, x) in self.__graph.keys()

    def add_edge(self, x: int, y: int, cost):
        self.__graph[(x, y)] = cost
        self.__num_edges += 1

    def get_cost_of_edge(self, x: int, y: int):
        if (x, y) not in self.__graph.keys() and (y, x) not in self.__graph.keys():
            return None
        if (x, y) in self.__graph.keys():
            return self.__graph[(x, y)]
        return self.__graph[(y, x)]

    def modify_edge(self, x: int, y: int, cost: int):
        self.__graph[(x, y)] = cost
        return self.__graph[(x, y)]

    def remove_edge(self, x: int, y: int):
        del self.__graph[(x, y)]
        self.__num_edges -= 1
