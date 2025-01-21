import copy


class Graph:
    def __init__(self, num_vertices=0):
        """
        Constructor for the Graph class.
        num_vertices: int - the number of vertices of the graph
        """
        self.__num_vertices = num_vertices  # the number of vertices of the graph
        self.__num_edges = 0
        # keys are (from, to), whereas values are the cost of that edge
        # 'edges' is a dictionary that stores the cost of an edge
        self.__edges = {}
        # stores values [v1, v2, ...] that are vertices the key V has edges coming from
        self.__adjacency_list = {i: [] for i in range(num_vertices)}

    def get_edges(self):
        """Returns the edges of the graph."""
        return self.__edges.keys()

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
        return self.__edges[key]

    def get_vertices(self):
        """Returns the vertices of the graph.
        Returns: list - the vertices of the graph."""
        return list(range(self.__num_vertices))

    def edge_exists(self, x: int, y: int):
        """Checks if an edge exists between two vertices.
        x: int - the starting vertex"""
        return (x, y) in self.__edges.keys() or (y, x) in self.__edges.keys()

    def add_edge(self, x: int, y: int, cost):
        """Adds an edge between two vertices.
        x: int - the starting vertex
        y: int - the ending vertex
        cost: int - the cost of the edge"""
        self.__edges[(x, y)] = cost
        self.__edges[(y, x)] = cost
        self.__num_edges += 1

        self.__adjacency_list[x].append(y)
        self.__adjacency_list[y].append(x)

    def get_degree(self, x: int):
        """Returns the degree of a vertex.
        x: int - the vertex"""
        return len(self.__adjacency_list[x])

    def get_adjacent_vertices(self, x: int):
        """Returns the vertices adjacent to a vertex.
        x: int - the vertex"""
        return self.__adjacency_list[x]

    def get_cost_of_edge(self, x: int, y: int):
        """Returns the cost of an edge."""
        return self.__edges[(x, y)]

    def modify_edge(self, x: int, y: int, cost: int):
        """Modifies the cost of an edge.
        x: int - the starting vertex
        y: int - the ending vertex
        cost: int - the new cost of the edge
        Returns: int - the new cost of the edge"""
        self.__edges[(x, y)] = cost
        self.__edges[(y, x)] = cost
        return self.__edges[(x, y)]

    def add_vertex(self, vertex: int):
        """Adds a vertex to the graph.
        vertex: int - the vertex to be added"""
        self.__adjacency_list[vertex] = []

    def remove_vertex(self, vertex: int):
        """Removes a vertex from the graph.
        vertex: int - the vertex to be removed"""
        if vertex in self.__adjacency_list:
            for v in self.__adjacency_list[vertex]:
                del self.__edges[(vertex, v)]
                self.__adjacency_list[v].remove(vertex)
            del self.__adjacency_list[vertex]
            self.__num_vertices -= 1
        else:
            print("Vertex not found in the graph")

    def remove_edge(self, x: int, y: int):
        """Removes an edge from the graph.
        x: int - the starting vertex"""
        del self.__edges[(x, y)]
        del self.__edges[(y, x)]
        self.__adjacency_list[x].remove(y)
        self.__adjacency_list[y].remove(x)
        self.__num_edges -= 1

    def graph_deepcopy(self):
        """Returns a deep copy of the graph.
        Returns: Graph - the deep copy of the graph"""
        graph = Graph(self.__num_vertices)
        graph.__adjacency_list = copy.deepcopy(self.__adjacency_list)
        graph.__edges = copy.deepcopy(self.__edges)
        graph.__num_edges = copy.deepcopy(self.__num_edges)
        return graph

    def connected(self):
        visited = set()
        connected_comp = []
        for vertex in range(self.__num_vertices):
            if vertex not in visited:
                comp = []
                queue = [vertex]
                while queue:
                    current = queue.pop(0)
                    if current not in visited:
                        visited.add(current)
                        comp.append(current)
                        for i in self.__adjacency_list[current]:
                            if i not in visited:
                                queue.append(i)
                connected_comp.append(comp)
        return connected_comp

