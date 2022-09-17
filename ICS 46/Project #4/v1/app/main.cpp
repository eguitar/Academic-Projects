#include <fstream>
#include <iostream>
#include "MyAVLTree.hpp"

int main()
{
    MyAVLTree<int, std::string> tree;
	tree.insert(5, "foo");
	tree.insert(10, "bar");
    std::cout << tree.contains(10);
    return 0;
}

