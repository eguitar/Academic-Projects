# explanations for these functions are provided in requirements.py

from graph import Graph

def get_diameter(graph: Graph) -> int:
	# return graph.get_diameter()
	pass

def get_clustering_coefficient(graph: Graph) -> float:
	return graph.get_cluster()


def get_degree_distribution(graph: Graph) -> dict[int, int]:
	return graph.get_degree()