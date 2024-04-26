import networkx as nx
from generator import Generator
import random


class MultiChoiceGenerator(Generator):
    def create_directed_path_graph(self, n):
        while True:
            # Generate an empty DAG
            G = nx.DiGraph()

            nodes = list(range(n))
            G.add_nodes_from(nodes)

            while G.number_of_edges() < n - 1:
                source = random.choice(nodes)
                target = random.choice(nodes)
                if source != target and not nx.has_path(G, target, source):
                    G.add_edge(source, target)

                # Find weakly connected components
            components = list(nx.weakly_connected_components(G))
            if len(components) == 1:
                # If there's only one connectivity component, select it
                G = nx.DiGraph(G.subgraph(components[0]))

                not_graph_path = any(G.out_degree(node) > 1 or G.in_degree(node) > 1 for node in G.nodes)
                # Check if the resulting graph is a Directed Acyclic Graph (DAG)
                if nx.is_directed_acyclic_graph(G) and not_graph_path:
                    print(f"Success! Graph is DAG with 1 connectivity component and exactly {len(G.edges)} edges.")
                    return G

    def get_relation(self, G, a, b):
        if nx.has_path(G, a, b):
            return "TRUE"
        elif nx.has_path(G, b, a):
            return "FALSE"
        else:
            return "UNABLE_TO_DETERMINE"