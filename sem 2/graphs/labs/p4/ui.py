from service import Service


class UI:
    def __init__(self):
        self.__service = Service()

    @staticmethod
    def print_menu():
        print("1. Print the whole graph.")
        print("2. Print the number of vertices and edges.")
        print("3. Get cost of edge. ")
        print("4. Modify cost of edge. ")
        print("5. Remove edge.")
        print("6. Add edge.")
        print("7. Generate random graph.")
        print("8. Find the connected components of the graph.")
        print("0. Exit")

    def print_graph_data(self):
        print("This graph has " + str(self.__service.graph.get_num_vertices()) + " vertices and " + str(
            self.__service.graph.get_num_edges()) + " edges.")

    def print_graph(self):
        for key in self.__service.graph.get_edges():
            print(str(key) + " " + str(self.__service.graph.get_edge_by_key(key)))

    def print_vertices(self):
        ver = self.__service.graph.get_vertices()
        for v in ver:
            print(str(v))

    def edge_exists(self):
        x, y = input("Please provide the vertices you want to check <x> <y>: ").split()
        try:
            x = int(x)
            y = int(y)
        except ValueError:
            print("Please choose integers.")
            return
        exists = self.__service.edge_exists(x, y)
        if exists == 1:
            print("There exists an edge from " + str(x) + " to " + str(y))
        else:
            print("There DOESN'T exist an edge from " + str(x) + " to " + str(y))

    def get_in_out_degree(self):
        x = input("Please provide the vertex: ")
        try:
            x = int(x)
        except ValueError:
            print("Please provide a valid integer vertex.")
            return
        try:
            print("The in-degree of vertex " + str(x) + " is " + str(self.__service.get_in_degree(int(x))))
            print("The out-degree of vertex " + str(x) + " is " + str(self.__service.get_out_degree(int(x))))
        except ValueError as e:
            print(e)

    def get_outbound_edges(self):
        x = input("Please provide the vertex: ")
        try:
            x = int(x)
        except ValueError:
            print("Please provide a valid integer vertex.")
            return
        try:
            edges = self.__service.get_outbound_edges(int(x))
            print("The outbound edges of " + str(x) + " are:")
            for e in range(len(edges)):
                print("(" + str(x) + ", " + str(edges[e]) + ")")
        except ValueError as e:
            print(e)

    def get_inbound_edges(self):
        x = input("Please provide the vertex: ")
        try:
            x = int(x)
        except ValueError:
            print("Please provide a valid integer vertex.")
            return
        try:
            edges = self.__service.get_inbound_edges(int(x))
            print("The inbound edges of " + str(x) + " are:")
            for e in range(len(edges)):
                print("(" + str(x) + ", " + str(edges[e]) + ")")
        except ValueError as e:
            print(e)

    def get_cost_of_edge(self):
        x, y = input("Please provide the edge <x> <y>: ").split()
        try:
            x = int(x)
            y = int(y)
        except ValueError:
            print("Please provide a valid integer vertex.")
            return
        try:
            cost = self.__service.get_cost_edge(int(x), int(y))
            print("The cost of {} is {}".format((x, y), cost))
        except ValueError as e:
            print(e)

    def modify_cost_of_edge(self):
        x, y = input("Please provide the edge <x> <y>: ").split()
        newCost = input("Cost: ")
        try:
            x = int(x)
            y = int(y)
            newCost = int(newCost)
        except ValueError:
            print("Please provide a valid integer vertex and cost.")
            return
        try:
            cost = self.__service.modify_cost(int(x), int(y), int(newCost))
            print("The cost of {} is was modified to {}".format((x, y), cost))
        except ValueError as e:
            print(e)

    def run(self):
        print("Welcome!")
        print("This program finds the connected components of an undirected graph using a breadth-first traversal of "
              "the graph.")
        # self.__service.generate_random_data(20, 40)
        while True:
            self.print_menu()
            command = int(input("> "))
            if command == 1:
                self.print_graph()
            elif command == 2:
                self.print_graph_data()
            elif command == 3:
                self.get_cost_of_edge()
            elif command == 4:
                self.modify_cost_of_edge()
            elif command == 5:
                self.remove_edge()
            elif command == 6:
                self.add_edge()
            elif command == 7:
                self.random_data()
            elif command == 8:
                self.Kruskal()
            elif command == 0:
                print("Goodbye!")
                break
            else:
                print("Invalid command.")

    # def add_vertex_ui(self):
    #     x = input("Vertex: ")
    #     try:
    #         x = int(x)
    #     except ValueError:
    #         print("Please provide a valid integer vertex.")
    #         return
    #     try:
    #         self.__service.add_vertex(x)
    #     except ValueError as e:
    #         print(e)

    # def remove_vertex(self):
    #     x = input("Vertex: ")
    #     try:
    #         x = int(x)
    #     except ValueError:
    #         print("Please provide a valid integer vertex.")
    #         return
    #     try:
    #         self.__service.remove_vertex(x)
    #     except ValueError as e:
    #         print(e)

    def remove_edge(self):
        x, y = input("Please provide the edge <x> <y>: ").split()
        try:
            x = int(x)
            y = int(y)
        except ValueError:
            print("Please provide a valid integer vertex.")
            return
        try:
            self.__service.remove_edge(x, y)
        except ValueError as e:
            print(e)

    def add_edge(self):
        x, y = input("Please provide the edge <x> <y>: ").split()
        cost = input("Cost: ")
        try:
            x = int(x)
            y = int(y)
            cost = int(cost)
        except ValueError:
            print("Please provide a valid integer vertex and cost.")
            return
        try:
            self.__service.add_edge(x, y, cost)
        except ValueError as e:
            print(e)

    # def copy(self):
    #     print("A copy of the graph was made. ")
    #     g = self.__service.graph_deepcopy()
    #     return g

    def read(self):
        filename = input("filename: ")
        self.__service.read_graph(filename)

    def write(self):
        filename = input("filename: ")
        self.__service.write_graph(filename)

    def random_data(self):
        vertex = input("# vertices: ")
        edges = input("# edges: ")
        try:
            self.__service.generate_random_data(int(vertex), int(edges))
        except ValueError as e:
            print(e)

    def Kruskal(self):
        print("The connected components of the graph are: ")
        self.__service.Kruskal()

