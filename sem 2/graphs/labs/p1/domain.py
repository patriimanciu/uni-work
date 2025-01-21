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
        self.__in_edges = {}
        # stores values [v1, v2, ...] that are vertices the key V has edges going to
        self.__out_edges = {}
        for i in range(num_vertices):
            self.__in_edges[i] = []
            self.__out_edges[i] = []

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
        array = []
        for k1, k2 in self.__edges.keys():
            if k1 not in array:
                array.append(k1)
            if k2 not in array:
                array.append(k2)
        return array

    def edge_exists(self, x: int, y: int):
        """Checks if an edge exists between two vertices.
        x: int - the starting vertex"""
        return (x, y) in self.__edges.keys()

    def add_edge(self, x: int, y: int, cost):
        """Adds an edge between two vertices.
        x: int - the starting vertex
        y: int - the ending vertex
        cost: int - the cost of the edge"""
        self.__edges[(x, y)] = cost
        self.__num_edges += 1

        if y not in self.__in_edges.keys():
            self.__in_edges[y] = []
        self.__in_edges[y].append(x)

        if x not in self.__out_edges.keys():
            self.__out_edges[x] = []
        self.__out_edges[x].append(y)

    def get_in_degree(self, x: int):
        """Returns the in-degree of a vertex.
        x: int - the vertex"""
        return len(self.__in_edges[x])

    def get_out_degree(self, x: int):
        """Returns the out-degree of a vertex.
        x: int - the vertex
        Returns: int - the out-degree of the vertex"""
        return len(self.__out_edges[x])

    def get_out_vertices(self):
        """Returns the vertices that have outbound edges.
        Returns: list - the vertices that have outbound edges."""
        array = []
        for k in self.__out_edges.keys():
            if len(self.__out_edges[k]) != 0:
                array.append(k)
        return array

    def get_in_vertices(self):
        """Returns the vertices that have inbound edges.
        Returns: list - the vertices that have inbound edges."""
        array = []
        for k in self.__in_edges.keys():
            if len(self.__in_edges[k]) != 0:
                array.append(k)
        return array

    def get_outbound_edges(self, x: int):
        """Returns the outbound edges of a vertex.
        x: int - the vertex
        Returns: list - the outbound edges of the vertex"""
        return self.__out_edges[x]

    def get_inbound_edges(self, x: int):
        """Returns the inbound edges of a vertex.
        x: int - the vertex
        Returns: list - the inbound edges of the vertex"""
        return self.__in_edges[x]

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
        return self.__edges[(x, y)]

    def add_vertex(self, vertex: int):
        """Adds a vertex to the graph.
        vertex: int - the vertex to be added"""
        self.__in_edges[vertex] = []
        self.__out_edges[vertex] = []
        self.__num_vertices += 1

    def remove_vertex(self, vertex: int):
        """Removes a vertex from the graph.
        vertex: int - the vertex to be removed"""
        if vertex in self.__in_edges.keys():
            for x in self.__in_edges[vertex]:
                del self.__edges[(x, vertex)]
            for x in self.__out_edges[vertex]:
                del self.__edges[(vertex, x)]
            self.__num_vertices -= 1
            self.__num_edges -= len(self.__in_edges[vertex]) + len(self.__out_edges[vertex])
        else:
            print("Vertex not found in the graph")

    def remove_edge(self, x: int, y: int):
        """Removes an edge from the graph.
        x: int - the starting vertex"""
        del self.__edges[(x, y)]
        self.__out_edges[x].remove(y)
        self.__in_edges[y].remove(x)
        self.__num_edges -= 1

    def graph_deepcopy(self):
        """Returns a deep copy of the graph.
        Returns: Graph - the deep copy of the graph"""
        graph = Graph(self.__num_vertices)
        graph.__in_edges = copy.deepcopy(self.__in_edges)
        graph.__out_edges = copy.deepcopy(self.__out_edges)
        graph.__edges = copy.deepcopy(self.__edges)
        graph.__num_edges = copy.deepcopy(self.__num_edges)
        return graph
