import networkx as nx
from generator import Generator


class MultiChoiceGenerator(Generator):
    def create_directed_path_graph(self):
        G = nx.MultiDiGraph()

    # todo
    # def get_ordered_clause(self, a, b):
    #     """""""


class MultiChoiceDisambiguateGenerator(Generator):
    pass
    # todo
    # def get_ordered_clause(self, a, b):
    #     """""""

#
# dag = nx.DiGraph()
#
# # Add nodes to the graph
# nodes = list(range(1, 10))
# dag.add_nodes_from(nodes)
#
# # Generate edges randomly until there are exactly 9 edges
# while dag.number_of_edges() < 9:
#     source = random.choice(nodes)
#     target = random.choice(nodes)
#     if source != target and not nx.has_path(dag, target, source):
#         dag.add_edge(source, target)
#
# # Ensure the graph has one connectivity component
# dag = max(nx.weakly_connected_component_subgraphs(dag), key=len)
#
# # Check if the resulting graph is a Directed Acyclic Graph (DAG)
# if nx.is_directed_acyclic_graph(dag):
#     print("Graph is a Directed Acyclic Graph (DAG) with one connectivity component and exactly 9 edges.")
# else:
#     print("Graph is not a Directed Acyclic Graph (DAG) with one connectivity component and exactly 9 edges.")
#
#

