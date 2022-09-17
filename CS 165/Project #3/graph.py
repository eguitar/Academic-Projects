# explanations for member functions are provided in requirements.py
# each file that uses a graph should import it from this file.

from collections.abc import Iterable
from random import randint

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

		self.matrix = [[0 for i in range(num_nodes)] for j in range(num_nodes)]

		# for i in range(num_nodes):
		# 	for j in self.adj_list[i]:
		# 		self.matrix[i][j] = 1
			
			




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
		pass
		# n = list(self.adj_list.keys())[randint(0,len(self.adj_list))]
		# print(n)

		# output = 0

		# while True:
		# 	# print("############################")
		# 	visit_set = {n}
		# 	queue = [n]
		# 	length = 0
		# 	while queue != []:   # for each queued
		# 		# print(queue)
		# 		node = queue[0]

		# 		visit_set.add(node)
		# 		flag = 0
		# 		for i in self.adj_list[queue.pop(0)]:				 # for each neighbor in queue
		# 			if not i in queue and not i in visit_set:
		# 				flag = 1
		# 				queue.append(i)

		# 		if flag == 1:
		# 			length += 1

		# 	# print(length)

		# 	if length < output:
		# 		break
		# 	else:
		# 		output = length
		# 		n = node
			

		# return output




		# for start in self.adj_list:
		# 	for end in self.adj_list and start != end:
		# 		if self.matrix != 0:
		# 			print(f"STARTING NODE - {start}")
		# 			visited = {start}
		# 			queued = [start]
		# 			length = 0
		# 			while queued != []:
		# 				visited.add(queued[0])






						

		# return min([max(vector) for vector in self.matrix])

		# eccen_set = set()
		
	
		# for n in self.adj_list:      # for each node
		# 	print(f"STARTING NODE - {n}")
			
			
			
		# 	visit_set = {n}
		# 	queue = [n]
		# 	length = 0
		# 	while queue != []:   # for each queued
		# 		print(queue)
		# 		visit_set.add(queue[0])
		# 		flag = 0
		# 		for i in self.adj_list[queue.pop(0)]:				 # for each neighbor in queue
					
		# 			if not i in queue and not i in visit_set:
						
		# 				flag = 1
		# 				queue.append(i)

		# 		if flag == 1:
		# 			length += 1
			


		# 	print(length)
		# 	eccen_set.add(length)
		
		# for i in self.matrix:
		# 	print(i)

 


	# def _get_eccentricity(self, node: int) -> int:









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