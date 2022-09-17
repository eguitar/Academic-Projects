# explanations for member functions are provided in requirements.py
# each file that uses a Zip Tree should import it from this file.

from __future__ import annotations
from typing import TypeVar
import random

KeyType = TypeVar('KeyType')
ValType = TypeVar('ValType')


class Node:
	def __init__(self, key: KeyType, val: ValType, rank: int, left: 'Node' = None, right: 'Node' = None):
		self.key = key
		self.val = val
		self.rank = rank
		self.left = left
		self.right = right


class ZipTree:
	def __init__(self):
		self.root = None
		self.size = 0
		self.height = 0

	@staticmethod
	def get_random_rank() -> int:         # uses coin flip to get rank
		i = 0
		while True:
			if random.randint(0,1) == 1:
				break
			i += 1
		return i

	def insert(self, key: KeyType, val: ValType, rank: int = -1):

		if (rank == -1):
			rank = self.get_random_rank()
		
		new_node = Node(key, val, rank)

		if self.root == None:                                  # if tree is empty
			self.root = new_node
			self.size += 1
			return
		elif rank > self.root.rank and key >= self.root.key:   # above right
			new_node.left = self.root
			self.root = new_node
			self.size += 1
			return
		elif rank >= self.root.rank and key <= self.root.key:  # above left
			new_node.right = self.root
			self.root = new_node
			self.size += 1
			return

		curr_node = self.root
		while True:
			if rank < curr_node.rank and key <= curr_node.key:   # below left
				if curr_node.left == None:
					curr_node.left = new_node
					self.size += 1
					return
				elif curr_node.left.rank > rank:
					curr_node = curr_node.left
				else:
					if curr_node.left.key < key:
						new_node.left = curr_node.left
						curr_node.left = new_node
						self.size += 1
						return
					else:
						new_node.right = curr_node.left
						curr_node.left = new_node
						self.size += 1
						return
			elif rank <= curr_node.rank and key >= curr_node.key:  # below right
				if curr_node.right == None:
					curr_node.right = new_node
					self.size += 1
					return
				elif curr_node.right.rank > rank:
					curr_node = curr_node.right
				else:
					if curr_node.right.key < key:
						new_node.left = curr_node.right
						curr_node.right = new_node
						self.size += 1
						return
					else:
						new_node.right = curr_node.right
						curr_node.right = new_node
						self.size += 1
						return

	def remove(self, key: KeyType):
		curr_node = self.root
		while True:
			par_key = curr_node.key
			if curr_node.key == key:
				break
			elif key < curr_node.key:
				curr_node = curr_node.left
			else:
				curr_node = curr_node.right
			

		if curr_node.left == None and curr_node.right == None:
			pass

	def __remove(self,node: Node, key: KeyType):
		if node.left == None:
			curr_node = node.right
			node = None
			return curr_node

		elif node.right == None:
			curr_node = node.left
			node = None
			return curr_node


	def find(self, key: KeyType) -> ValType:
		curr_node = self.root
		while True:
			if curr_node.key == key:
				return curr_node.val
			elif key < curr_node.key:
				curr_node = curr_node.left
			else:
				curr_node = curr_node.right

	def set_value(self, key: KeyType, val: ValType):
		curr_node = self.root
		while True:
			if curr_node.key == key:
				curr_node.val = val
				return
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