import networkx as nx
import matplotlib.pyplot as plt

# Create a directed graph object
dag = nx.DiGraph()

# Add nodes
dag.add_nodes_from([1, 2, 3, 4, 5])

# Add edges
dag.add_edge(1, 2)
dag.add_edge(1, 3)
dag.add_edge(2, 4)
dag.add_edge(3, 4)
dag.add_edge(3, 5)
dag.add_edge(4, 5)

# Draw the graph
nx.draw(dag, with_labels=True, node_size=1000, node_color='skyblue', font_size=12, font_weight='bold')
plt.show()