import networkx as nx
from generator import Generator
import json

with open('grammar.json', 'r') as file:
    grammar = json.load(file)


class SingleChoiceGenerator(Generator):
    def create_directed_path_graph(self, n):
        # Create a directed path graph with n vertices
        G = nx.path_graph(n, create_using=nx.DiGraph)
        return G

    def get_relation(self, G, a, b):
        if nx.has_path(G, a, b):
            return "TRUE"
        else:
            return "FALSE"



# N = 4   #  number of vertices
# generator = SingleChoiceGenerator(disambiguate=False)
# directed_path_graph = generator.create_directed_path_graph(N)
# print(generator.generate_passage(directed_path_graph, draw_graph=True))

