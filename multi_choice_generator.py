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

            # Generate edges randomly until there are exactly 9 edges
            while G.number_of_edges() < n-1:
                source = random.choice(nodes)  # Assuming 9 nodes numbered 0 to 8
                target = random.choice(nodes)
                if source != target and not nx.has_path(G, target, source):
                    G.add_edge(source, target)

                # Find weakly connected components
            components = list(nx.weakly_connected_components(G))
            if len(components) == 1:
                # If there's only one connectivity component, select it
                G = nx.DiGraph(G.subgraph(components[0]))

                # Check if the resulting graph is a Directed Acyclic Graph (DAG)
                if nx.is_directed_acyclic_graph(G):
                    print(f"Success! Graph is a Directed Acyclic Graph (DAG) with one connectivity component and exactly {len(G.edges)} edges.")
                    return G


    # todo
    # def get_ordered_clause(self, a, b):
    #     """""""


class MultiChoiceDisambiguateGenerator(Generator):
    pass
    # todo
    # def get_ordered_clause(self, a, b):
    #     """""""

#

multi_choice_generator = MultiChoiceGenerator()
multi_choice_graph = multi_choice_generator.create_directed_path_graph(4)
multi_choice_generator.draw_graph(multi_choice_graph)
print(multi_choice_generator.generate_sentence_from_graph(multi_choice_graph))