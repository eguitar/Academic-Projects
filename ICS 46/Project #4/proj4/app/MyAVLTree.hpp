#ifndef __PROJ_FOUR_AVL_HPP
#define __PROJ_FOUR_AVL_HPP

#include "runtimeexcept.hpp"
#include <string>
#include <vector>

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
		unsigned height;
		Node* parent;
		Node* left;	
		Node* right;
	};

	Node* root;
	size_t tree_size;
	
	// Functions implemented according to the
	// algorithmns represented by the zyBook
	void updateHeight(Node* node);

	void setChild(Node* par, bool isLeft, Node* chi);

	void replaceChild(Node* par, Node* cur, Node* chi);

	unsigned getBalance(Node* node);

	void reBalance(Node* node);

	void rotateLeft(Node* node);

	void rotateRight(Node* node);

	void getPreOrder(Node* node, std::vector<Key>& map) const;

	void getInOrder(Node* node, std::vector<Key>& map) const;
	
	void getPostOrder(Node* node, std::vector<Key>& map) const;

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
	void insert(const Key & k, const Value & v);

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
	tree_size++;
	Node* node = new Node;
	node->key = k;
	node->value = v;
	node->left = nullptr;
	node->right = nullptr;
	node->parent = nullptr;
	node->height = 0;
		
	if (root == nullptr)
	{
		root = node;
		return;
	}

	Node* cur = root;
	while (cur != nullptr)
	{
		if (node->key < cur->key)
		{
			if (cur->left == nullptr)
			{
				cur->left = node;
				node->parent = cur;
				cur = nullptr;
			}
			else
			{
				cur = cur->left;
			}
		}
		else
		{
			if (cur->right == nullptr)
			{
				cur->right = node;
				node->parent = cur;
				cur = nullptr;
			}
			else
			{
				cur = cur->right;
			}
		}
	}

	node = node->parent;
	while (node != nullptr)
	{
		reBalance(node);
		node = node->parent;
	}
}




template<typename Key, typename Value>
std::vector<Key> MyAVLTree<Key, Value>::inOrder() const
{
	std::vector<Key> order;
	getInOrder(root,order);
	return order; 
}

template<typename Key, typename Value>
void MyAVLTree<Key, Value>::getInOrder(Node* node, std::vector<Key>& map) const
{
	if (node == nullptr)
		return;
	getInOrder(node->left,map);
	map.push_back(node->key);
	getInOrder(node->right,map);
}		

template<typename Key, typename Value>
std::vector<Key> MyAVLTree<Key, Value>::preOrder() const
{
	std::vector<Key> order;
	getPreOrder(root,order);
	return order; 
}

template<typename Key, typename Value>
void MyAVLTree<Key, Value>::getPreOrder(Node* node, std::vector<Key>& map) const
{
	if (node == nullptr)
		return;
	map.push_back(node->key);
	getPreOrder(node->left,map);
	getPreOrder(node->right,map);
}

template<typename Key, typename Value>
std::vector<Key> MyAVLTree<Key, Value>::postOrder() const
{
	std::vector<Key> order;
	getPostOrder(root,order);
	return order; 
}

template<typename Key, typename Value>
void MyAVLTree<Key, Value>::getPostOrder(Node* node, std::vector<Key>& map) const
{
	if (node == nullptr)
		return;
	getPostOrder(node->left,map);
	getPostOrder(node->right,map);
	map.push_back(node->key);
}



template<typename Key, typename Value>
void MyAVLTree<Key, Value>::updateHeight(Node* node)
{
	unsigned leftHeight = -1;
	if (node->left != nullptr)
	{
		leftHeight = node->left->height;
	}
	unsigned rightHeight = -1;
	if (node->right != nullptr)
	{
		rightHeight = node->right->height;
	}

	if (leftHeight >= rightHeight)
	{
		node->height = leftHeight + 1;
	}
	else
	{
		node->height = rightHeight + 1;
	}
}

template<typename Key, typename Value>
void MyAVLTree<Key, Value>::setChild(Node* par, bool isLeft, Node* chi)
{
	if (isLeft)
	{
		par->left = chi;
	}
	else
	{
		par->right = chi;
	}
	if (chi != nullptr)
	{
		chi->parent = par;
	}

	updateHeight(par);
}

template<typename Key, typename Value>
void MyAVLTree<Key, Value>::replaceChild(Node* par, Node* cur, Node* chi)
{
	if (par->left == cur)
	{
		setChild(par,true,chi);
	}
	else if (par->right == cur)
	{
		setChild(par,false,chi);
	}
}

template<typename Key, typename Value>
unsigned MyAVLTree<Key, Value>::getBalance(Node* node)
{
	unsigned leftHeight = -1;
	if (node->left != nullptr)
	{
		leftHeight = node->left->height;
	}
	unsigned rightHeight = -1;
	if (node->right != nullptr)
	{
		rightHeight = node->right->height;
	}
	return leftHeight - rightHeight;
}

template<typename Key, typename Value>
void MyAVLTree<Key, Value>::reBalance(Node* node)
{
	updateHeight(node);

	if (getBalance(node) == -2)
	{
		if (getBalance(node->right) == 1)
		{
			rotateRight(node->right);
		}
		rotateLeft(node);
	}
	else if (getBalance(node) == 2)
	{
		if (getBalance(node->left) == -1)
		{
			rotateLeft(node->left);
		}
		rotateRight(node);
	}
}

template<typename Key, typename Value>
void MyAVLTree<Key, Value>::rotateLeft(Node* node)
{
	Node* rightLeftChild = node->right->left;
	if (node->parent != nullptr)
	{
		replaceChild(node->parent,node,node->right);
	}
	else
	{
		root = node->right;
		root->parent = nullptr;
	}
	setChild(node->right,true,node);
	setChild(node,false,rightLeftChild);
}

template<typename Key, typename Value>
void MyAVLTree<Key, Value>::rotateRight(Node* node)
{
	Node* leftRightChild = node->left->right;
	if (node->parent != nullptr)
	{
		replaceChild(node->parent,node,node->left);
	}
	else
	{
		root = node->left;
		root->parent = nullptr;
	}
	setChild(node->left,false,node);
	setChild(node,true,leftRightChild);
}




#endif 