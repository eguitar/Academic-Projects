# explanations for member functions are provided in requirements.py
# each file that uses a graph should import it from this file.

from collections.abc import Iterable
from collections import deque 
from random import randint,random
from numpy import log2

class Graph:
	def __init__(self, num_nodes: int, edges: 'Iterable[tuple[int, int]]'):
		self.num_node = num_nodes
		self.num_edge = 0
		self.adj_list = {}
		for e in edges:
			self.num_edge = self.num_edge + 1
			if e[0] in self.adj_list:
				self.adj_list[e[0]].add(e[1])
			else:
				self.adj_list[e[0]] = set()
				self.adj_list[e[0]].add(e[1])
			if e[1] in self.adj_list:
				self.adj_list[e[1]].add(e[0])
			else:
				self.adj_list[e[1]] = set()
				self.adj_list[e[1]].add(e[0])

	def get_num_nodes(self) -> int:
		return self.num_node

	def get_num_edges(self) -> int:
		return self.num_edge

	def get_neighbors(self, node: int) -> 'Iterable[int]':
		if node in self.adj_list:
			return set(self.adj_list[node])
		else:
			return set()

	# feel free to define new methods in addition to the above
	# fill in the definitions of each required member function (above),
	# and for any additional member functions you define

	def get_diameter(self) -> int:
		n = list(self.adj_list.keys())[randint(0,len(self.adj_list)-1)]
		output = 0
		while True:
			visit_set = {n}
			queue = deque([n])
			length = -1
			while queue:   # for each batch queued
				length += 1
				size = len(queue)
				for i in range(size):
					node = queue.popleft()
					visit_set.add(node)
					for i in self.adj_list[node]:
						if (not i in visit_set):
							queue.append(i)
							visit_set.add(i)		
			if length > output:
				output = length
				n = node
			else:
				break	
		return output

	def get_cluster(self) -> float:
		tri_count = 0
		for node in self.adj_list:
			if len(self.adj_list) >= 2:
				for v in self.adj_list[node]:
					if not v == node:
						for w in self.adj_list[node]:
							if (not v == w) and (not w == node):
								if w in self.adj_list[v]:
									tri_count += 1
		sum_degree = 0
		for node in self.adj_list:
			x = len(self.adj_list[node])
			sum_degree = sum_degree + int(x*(x-1)/2)
		return ((3*tri_count)/(6*sum_degree))

	def get_degree(self) -> dict[int, int]:
		output = dict()
		for node in self.adj_list:
			x = len(self.adj_list[node])
			if x in output:
				output[x] = output[x] + 1
			else:
				output[x] = 1
		return output


def generate_er_graph(n: int) -> 'Iterable[tuple[int, int]]':
    p = 2 * ( log2(n) ) / n
    output = set()
    v = 1
    w = -1
    while v < n:
        r = random()
        w = w + 1 + int(log2((1-r))/log2((1-p)))
        while (w >= v and v < n):
            w = w - v
            v = v + 1
        if v < n:
            output.add(tuple([v,w]))
    return output


def generate_ba_graph(n: int) -> 'Iterable[tuple[int, int]]':
    d = 5
    M = [0] * (2*n*d)
    for v in range(n):
        for i in range(d):
            M[2*(v*d+1)] = v
            r = randint(0, 2*(v*d+i))
            M[2*(v*d+i)+1] = M[r]
    output = set()
    for i in range(n*d):
        output.add(tuple([M[2*i],M[2*i+1]]))
    return output