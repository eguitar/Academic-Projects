#ifndef __PROJ_FOUR_AVL_HPP
#define __PROJ_FOUR_AVL_HPP

#include "runtimeexcept.hpp"
#include <string>
#include <vector>
#include <iostream>




class ElementNotFoundException : public RuntimeException 
{
public:
	ElementNotFoundException(const std::string & err) : RuntimeException(err) {}
};


template<typename Key, typename Value>
class MyAVLTree
{
private:
	struct Node
	{
		Key key;
		Value value;
		Node* left;	
		Node* right;
	};
	// fill in private member data here
	// If you need to declare private functions, do so here too.
	Node* root;
	size_t tree_size;

	


public:
	MyAVLTree();

	// The destructor is, however, required. 
	~MyAVLTree();
	void deleteNodes(Node* curr);
	// size() returns the number of distinct keys in the tree.
	size_t size() const noexcept;

	// isEmpty() returns true if and only if the tree has no values in it. 
	bool isEmpty() const noexcept;

	// contains() returns true if and only if there
	//  is a (key, value) pair in the tree
	//	that has the given key as its key.
	bool contains(const Key & k) const; 

	// find returns the value associated with the given key
	// If !contains(k), this will throw an ElementNotFoundException
	// There needs to be a version for const and non-const MyAVLTrees.
	Value & find(const Key & k);
	const Value & find(const Key & k) const;

	// Inserts the given key-value pair into 
	// the tree and performs the AVL re-balance
	// operation, as described in lecture. 
	// If the key already exists in the tree, 
	// you may do as you please (no test cases in
	// the grading script will deal with this situation)
	void insert(const Key & k, const Value & v);

	// in general, a "remove" function would be here
	// It's a little trickier with an AVL tree
	// and I am not requiring it for this quarter's ICS 46.
	// You should still read about the remove operation
	// in your textbook. 

	// The following three functions all return
	// the set of keys in the tree as a standard vector.
	// Each returns them in a different order.
	std::vector<Key> inOrder() const;
	std::vector<Key> preOrder() const;
	std::vector<Key> postOrder() const;


};


template<typename Key, typename Value>
MyAVLTree<Key,Value>::MyAVLTree()
{
	root = nullptr;
	tree_size = 0;
}

template<typename Key, typename Value>
MyAVLTree<Key,Value>::~MyAVLTree()
{
	deleteNodes(root);
}

template<typename Key, typename Value>
void MyAVLTree<Key,Value>::deleteNodes(Node* curr)
{
	if (curr == nullptr)
		return;
	deleteNodes(curr->left);
	deleteNodes(curr->right);
	delete curr;
}


template<typename Key, typename Value>
size_t MyAVLTree<Key, Value>::size() const noexcept
{
	return tree_size;
}

template<typename Key, typename Value>
bool MyAVLTree<Key, Value>::isEmpty() const noexcept
{
	if (tree_size == 0)
		return true;
	else
		return false;
}


template<typename Key, typename Value>
bool MyAVLTree<Key, Value>::contains(const Key &k) const
{
	Node* curr = root;
	
	while (true)
	{
		if (curr == nullptr)
		{
			return false;
		}
		if (k == curr->key)
			return true;
		else if (k < curr->key)
			curr = curr->left;
		else
			curr = curr->right;
	}
}



template<typename Key, typename Value>
Value & MyAVLTree<Key, Value>::find(const Key & k)
{
	Node* curr = root;
	
	while (true)
	{
		if (curr == nullptr)
			throw ElementNotFoundException("Key is not in the AVLTree.");
		if (k == curr->key)
			return curr->value;
		else if (k < curr->key)
			curr = curr->left;
		else
			curr = curr->right;
	}
}

template<typename Key, typename Value>
const Value & MyAVLTree<Key, Value>::find(const Key & k) const
{
	Node* curr = root;
	
	while (true)
	{
		if (curr == nullptr)
			throw ElementNotFoundException("Key is not in the AVLTree.");
		if (k == curr->key)
			return curr->value;
		else if (k < curr->key)
			curr = curr->left;
		else
			curr = curr->right;
	}
}

template<typename Key, typename Value>
void MyAVLTree<Key, Value>::insert(const Key & k, const Value & v)
{
	Node* new_node = new Node;
	new_node->key = k;
	new_node->value = v;
	new_node->left = nullptr;
	new_node->right = nullptr;
	tree_size++;
	Node* curr = root;
	Node* parent;
	bool left;
	if (root == nullptr)
	{
		root = new_node;
		return;
	}

	while (true)
	{
		if (curr == nullptr)
		{
			if (left)
				parent->left = new_node;
			else
				parent->right = new_node;			
			return;
		}
		parent = curr;
		if (k < curr->key)
		{
			curr = curr->left;
			left = true;
		}
		else
		{
			curr = curr->right;
			left = false;
		}
	}
}




template<typename Key, typename Value>
std::vector<Key> MyAVLTree<Key, Value>::inOrder() const
{
	std::vector<Key> foo;
	return foo; 
}


template<typename Key, typename Value>
std::vector<Key> MyAVLTree<Key, Value>::preOrder() const
{
	std::vector<Key> foo;
	return foo; 
}


template<typename Key, typename Value>
std::vector<Key> MyAVLTree<Key, Value>::postOrder() const
{
	std::vector<Key> foo;
	return foo; 
}







#endif 