import networkx as nx
import matplotlib.pyplot as plt
import json
import random

# Read JSON data from a file
with open('grammar.json', 'r') as file:
    grammar = json.load(file)


class Generator:
    def __init__(self, disambiguate=False, temporal_reasoning=True ):
        self.temporal_reasoning = temporal_reasoning
        self.disambiguate = disambiguate

    def draw_graph(self, G, labels):
        # Draw the graph
        nx.draw(G, labels=labels, with_labels=True, node_size=500, node_color='skyblue', font_size=12, font_weight='bold', arrows=True)
        plt.show()

    def get_ordered_clause(self, a, b):
        suffix = ", with possibly others in between" if self.disambiguate else ""
        if self.temporal_reasoning:
            before = random.choice(grammar["temporal"]["left"])
            after = random.choice(grammar["temporal"]["right"])
            verb = random.choice(grammar["temporal"]["verb"])
        else:
            before = random.choice(grammar["spatial"]["left"])
            after = random.choice(grammar["spatial"]["right"])
            verb = random.choice(grammar["spatial"]["verb"])

        before_sen = f"{a} {verb} {before} {b}{suffix}."
        after_sen = f"{b} {verb} {after} {a}{suffix}."
        sentences = [before_sen, after_sen]
        return random.choice(sentences)

    def get_relation(self, G, a, b):
        return None

    def generate_passage(self, G, draw_graph=False):
        names = random.sample(grammar["names"], G.number_of_nodes())
        mapping = {idx: names[idx] for idx in range(G.number_of_nodes())}
        print(f'mapping is {mapping}')
        all_edges = list(G.edges())
        random.shuffle(all_edges)
        sentences = [self.get_ordered_clause(names[edge[0]], names[edge[1]]) for edge in all_edges]
        possible_conclusions = []
        for a in G.nodes:
            for b in G.nodes:
                if a != b and not G.has_edge(a, b):
                    possible_conclusions.append([[names[a], names[b]], self.get_relation(G, a, b)])
        if draw_graph:
            self.draw_graph(G, mapping)

        return {'sentences': sentences, 'possible_conclusions': possible_conclusions}
