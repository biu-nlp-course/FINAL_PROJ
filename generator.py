import networkx as nx
import matplotlib.pyplot as plt
import json
import random

# Read JSON data from a file
with open('Grammar.json', 'r') as file:
    grammar = json.load(file)


class Generator:
    def create_directed_path_graph(self, n):
        # Create a directed path graph with n vertices
        G = nx.path_graph(n, create_using=nx.DiGraph)
        return G

    def draw_graph(self, G):
        # Draw the graph
        nx.draw(G, with_labels=True, node_size=500, node_color='skyblue', font_size=12, font_weight='bold', arrows=True)
        plt.show()

    def get_ordered_clause(self, a, b):
        return f"{b} came after {a}."

    def generate_sentence_from_graph(self, G):
        names = random.sample(grammar["names"], G.number_of_nodes())
        all_edges = list(G.edges())
        # with some probability - do shuffle the all_edges
        random.shuffle(all_edges)
        sentence = ""
        for edge in all_edges:
            sentence += self.get_ordered_clause(names[edge[0]], names[edge[1]]) + " "
        return sentence[:-1]


# Define the number of vertices
N = 6

# Create the directed path graph
generator = Generator()
directed_path_graph = generator.create_directed_path_graph(N)
generator.draw_graph(directed_path_graph)
print(generator.generate_sentence_from_graph(directed_path_graph))
