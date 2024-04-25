import networkx as nx
from generator import Generator

class SingleChoiceGenerator(Generator):
    def create_directed_path_graph(self, n):
        # Create a directed path graph with n vertices
        G = nx.path_graph(n, create_using=nx.DiGraph)
        return G



class SingleChoiceDisambiguate(Generator):
    def create_directed_path_graph(self, n):
        # Create a directed path graph with n vertices
        G = nx.path_graph(n, create_using=nx.DiGraph)
        return G


# Define the number of vertices
N = 6

# Create the directed path graph
generator = SingleChoiceGenerator()
directed_path_graph = generator.create_directed_path_graph(N)
generator.draw_graph(directed_path_graph)
print(generator.generate_sentence_from_graph(directed_path_graph))
