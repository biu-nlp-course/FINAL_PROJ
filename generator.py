import networkx as nx
import matplotlib.pyplot as plt
import json
import random

# Read JSON data from a file
with open('grammar.json', 'r') as file:
    grammar = json.load(file)


class Generator:

    def draw_graph(self, G):
        # Draw the graph
        nx.draw(G, with_labels=True, node_size=500, node_color='skyblue', font_size=12, font_weight='bold', arrows=True)
        plt.show()

    def get_ordered_clause(self, a, b):
        return f"{b} came after {a}."

    def generate_sentence_from_graph(self, G):
        names = random.sample(grammar["names"], G.number_of_nodes())
        mapping = {idx: names[idx] for idx in range(G.number_of_nodes())}
        print(f'mapping is {mapping}')
        all_edges = list(G.edges())
        # with some probability - do shuffle the all_edges
        random.shuffle(all_edges)
        sentence = ""
        for edge in all_edges:
            sentence += self.get_ordered_clause(names[edge[0]], names[edge[1]]) + " "
        return sentence[:-1]




