# explanations for member functions are provided in requirements.py
# each file that uses a Zip Tree should import it from this file.

from __future__ import annotations
from typing import TypeVar
from CFloat import CFloat
import random

KeyType = TypeVar('KeyType')
ValType = TypeVar('ValType')


class Node:
	def __init__(self, key: KeyType, val: ValType, rank: int, left: 'Node' = None, right: 'Node' = None):
		self.key = key
		self.val = val
		self.rank = rank
		self.brc = CFloat(1.0)
		self.left = left
		self.right = right


class ZipTree:
	def __init__(self):
		self.root = None
		self.size = 0

	@staticmethod
	def get_random_rank() -> int:         # uses coin flip to get rank
		i = 0
		while True:
			if random.randint(0,1) == 1:
				break
			i += 1
		return i

	def find(self, key: KeyType) -> ValType:
		curr_node = self.root
		while True:
			if curr_node.key == key:
				return curr_node.val
			elif key < curr_node.key:
				curr_node = curr_node.left
			else:
				curr_node = curr_node.right

	def get_size(self) -> int:
		return self.size

	def get_height(self) -> int:
		return self.__get_height(self.root)

	def __get_height(self, node: Node):
		if node == None:
			return 0
		if node.left == None and node.right == None:
			return 0

		left_height = self.__get_height(node.left)
		right_height = self.__get_height(node.right)

		return 1 + max(left_height, right_height)

	def get_depth(self, key: KeyType):
		i = 0
		curr_node = self.root
		while True:
			if curr_node.key == key:
				break
			elif key < curr_node.key:
				curr_node = curr_node.left
			else:
				curr_node = curr_node.right
			i += 1
		return i

	# best fit zip tree ##############################################
	def __zip(self, node1: Node, node2: Node):
		if node1 == None:
			return node2
		if node2 == None:
			return node1
		if node1.rank < node2.rank:
			node2.left = self.__zip(node1, node2.left)
			return node2
		else:
			node1.right = self.__zip(node1.right, node2)
			return node1
	
	def insert(self, key: KeyType, val: ValType, rank: int = -1):
		self.size += 1
		if (rank == -1):
			rank = self.get_random_rank()
		new_node = Node(key, val, rank)
		self.root = self.__insert(self.root, new_node)
		
		# self.update_brc1()
		curr_node = self.root
		while True:
			self.__update_nodes1(curr_node)
			if curr_node.key == key:
				break
			elif key < curr_node.key:
				curr_node = curr_node.left
			else:
				curr_node = curr_node.right

	def __insert(self, node: Node, new_node: Node):
		if node  == None:
			return new_node
		if new_node.key < node.key:
			if self.__insert(node.left, new_node) == new_node:
				if new_node.rank < node.rank:
					node.left = new_node
				else:
					node.left = new_node.right
					new_node.right = node
					return new_node
		else:
			if self.__insert(node.right, new_node) == new_node:
				if new_node.rank <= node.rank:
					node.right = new_node
				else:
					node.right = new_node.left
					new_node.left = node
					return new_node
		return node

	def remove(self, key: KeyType):
		curr_node = self.root
		while curr_node != None:
			if curr_node.key == key:
				break
			elif key < curr_node.key:
				if curr_node.left != None and curr_node.left.key == key:
					break
				else:
					curr_node = curr_node.left
			else:
				if curr_node.right != None and curr_node.right.key == key:
					break
				else:
					curr_node = curr_node.right
		end_key = curr_node.key

		self.root = self.__remove(self.root, key)
		# self.update_brc1()
		curr_node = self.root
		while curr_node != None:
			self.__update_nodes1(curr_node)
			if curr_node.key == end_key:
				if curr_node.left != None:  ## need to test
					self.__update_nodes1(curr_node.left)
				if curr_node.right != None:
					self.__update_nodes1(curr_node.right)
				break
			elif key < curr_node.key:
				curr_node = curr_node.left
			else:
				curr_node = curr_node.right


	def __remove(self,node: Node, key: KeyType):
		if key == node.key:
			return self.__zip(node.left, node.right)
		if key < node.key:
			if key == node.left.key:
				node.left = self.__zip(node.left.left, node.left.right)
			else:
				self.__remove(node.left, key)
		else:
			if key == node.right.key:
				node.right = self.__zip(node.right.left, node.right.right)
			else:
				self.__remove(node.right, key)
		return node

	# def update_brc1(self):
	# 	self.__update_nodes(self.root)
	
	# def __update_nodes(self, node: Node):
	# 	if node == None:
	# 		return
	# 	node.brc = self.__get_brc1(node)
	# 	if node.left != None:
	# 		self.__update_nodes1(node.left)
	# 	if node.right != None:
	# 		self.__update_nodes1(node.right)

	def __update_nodes1(self, node: Node):
		if node == None:
			return
		node.brc = self.__get_brc1(node)

	def __get_brc1(self, node: Node) -> KeyType:
		if node.right == None:
			return node.key
		return self.__get_brc1(node.right)

	def find_best(self, key: KeyType) -> KeyType:
		if self.root == None:
			return None
		
		fit_key = None
		node = self.root

		while True:
			if key > node.brc:
				return fit_key
			
			if key <= node.key:      
				fit_key = node.key
				if node.left == None:
					return fit_key
				else:
					node = node.left

			if key > node.key:
				if node.right == None:
					return fit_key
				else:
					node = node.right
	
	# first fit zip tree ##############################################
	def insert_sub(self, key: KeyType, val: ValType, rank: int = -1):
		self.size += 1
		if (rank == -1):
			rank = self.get_random_rank()
		new_node = Node(key, val, rank)
		self.root = self.__insert(self.root, new_node)
		# self.update_brc2()
		curr_node = self.root
		while True:
			self.__update_nodes2(curr_node)
			if curr_node.key == key:
				break
			elif key < curr_node.key:
				curr_node = curr_node.left
			else:
				curr_node = curr_node.right


	def remove_sub(self, key: KeyType):
		curr_node = self.root
		while curr_node != None:
			if curr_node.key == key:
				break
			elif key < curr_node.key:
				if curr_node.left != None and curr_node.left.key == key:
					break
				else:
					curr_node = curr_node.left
			else:
				if curr_node.right != None and curr_node.right.key == key:
					break
				else:
					curr_node = curr_node.right
		end_key = curr_node.key
		
		self.root = self.__remove(self.root, key)
		# self.update_brc2()

		curr_node = self.root
		while curr_node != None:
			self.__update_nodes2(curr_node)
			if curr_node.key == end_key:
				if curr_node.left != None:  ## need to test
					self.__update_nodes2(curr_node.left)
				if curr_node.right != None:
					self.__update_nodes2(curr_node.right)
				break
			elif key < curr_node.key:
				curr_node = curr_node.left
			else:
				curr_node = curr_node.right
	
	# def update_brc2(self):
	# 	self.__update_nodes2(self.root)
	
	def __update_nodes2(self, node: Node):
		
		if node == None:
			return

		node.brc = self.__get_brc2(node)
		# if node.left != None:
		# 	self.__update_nodes2(node.left)
		# if node.right != None:
		# 	self.__update_nodes2(node.right)

	def __get_brc2(self, node: Node) -> ValType:
		if node.left == None and node.right == None:
			return node.val

		if node.right == None:
			left_brc = self.__get_brc2(node.left)
			return max(node.val, left_brc)
		elif node.left == None:
			right_brc = self.__get_brc2(node.right)
			return max(node.val, right_brc)
		else:
			left_brc = self.__get_brc2(node.left)
			right_brc = self.__get_brc2(node.right)

			return max(node.val, left_brc, right_brc)

	def find_first(self, val: ValType) -> KeyType:
		if self.root == None:
			return -1
		
		fit_id = -1
		node = self.root
		
		while True:
			if val > node.brc and val > node.val:
				return fit_id
			
			if node.left != None and val <= node.left.brc:
				node = node.left
				continue
			elif val <= node.val:
				return node.key
			elif node.right != None and val <= node.right.brc:
				node = node.right
				continue
			
			return fit_id