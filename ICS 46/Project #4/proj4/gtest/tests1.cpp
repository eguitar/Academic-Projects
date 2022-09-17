#include "gtest/gtest.h"
#include "MyAVLTree.hpp"
#include "proj4.hpp"
#include <string>
#include <sstream>
#include <vector>

namespace{



TEST(CheckPoint, CheckPoint_FindTheRoot)
{
	MyAVLTree<int, std::string> tree;
	tree.insert(5, "foo");

	EXPECT_TRUE( tree.contains(5) );
}

TEST(CheckPoint, CheckPoint_FindOneHop)
{
	MyAVLTree<int, std::string> tree;
	tree.insert(5, "foo");
	tree.insert(10, "bar");

	EXPECT_TRUE( tree.contains(10) );
}

TEST(CheckPoint, CheckPoint_FindTwoHops)
{
	MyAVLTree<int, std::string> tree;
	tree.insert(5, "foo");
	tree.insert(3, "sna");
	tree.insert(10, "bar");
	tree.insert(12, "twelve");

	EXPECT_TRUE( tree.contains(12) );
}



TEST(CheckPoint, CheckPoint_Add5)
{
	MyAVLTree<int, std::string> tree;
	tree.insert(5, "foo");
	tree.insert(3, "sna");
	tree.insert(10, "bar");
	tree.insert(12, "twelve");
	tree.insert(15, "fifteen");

	EXPECT_TRUE( tree.size() == 5 );
}



TEST(PostCheckPoint, InOrderTraversal)
{
	MyAVLTree<int, std::string> tree;
	tree.insert(5, "foo");
	tree.insert(3, "sna");
	tree.insert(10, "bar");
	tree.insert(12, "twelve");
	tree.insert(15, "fifteen");

	std::vector<int> trav = tree.inOrder();
	std::vector<int> expected = {3, 5, 10, 12, 15};
	EXPECT_TRUE( trav == expected );
}

TEST(PostCheckPoint, PreOrderTraversal1)
{
	MyAVLTree<int, std::string> tree;
	tree.insert(6, "");
	tree.insert(4, "");
	tree.insert(8, "");
	tree.insert(3, "");
	tree.insert(5, "");
	tree.insert(7, "");
	tree.insert(9, "");

	std::vector<int> trav = tree.preOrder();
	std::vector<int> expected = {6,4,3,5,8,7,9};
	EXPECT_TRUE( trav == expected );
}

TEST(PostCheckPoint, InOrderTraversal1)
{
	MyAVLTree<int, std::string> tree;
	tree.insert(6, "");
	tree.insert(4, "");
	tree.insert(8, "");
	tree.insert(3, "");
	tree.insert(5, "");
	tree.insert(7, "");
	tree.insert(9, "");

	std::vector<int> trav = tree.inOrder();
	std::vector<int> expected = {3,4,5,6,7,8,9};
	EXPECT_TRUE( trav == expected );
}

TEST(PostCheckPoint, PostOrderTraversal1)
{
	MyAVLTree<int, std::string> tree;
	tree.insert(6, "");
	tree.insert(4, "");
	tree.insert(8, "");
	tree.insert(3, "");
	tree.insert(5, "");
	tree.insert(7, "");
	tree.insert(9, "");

	std::vector<int> trav = tree.postOrder();
	std::vector<int> expected = {3,5,4,7,9,8,6};
	EXPECT_TRUE( trav == expected );
}


TEST(PostCheckPoint, JackSparrow)
{
	std::string quote = "I'm dishonest, and a dishonest man you can ";
	quote += "always trust to be dishonest. Honestly. It's the honest ";
	quote += "ones you want to watch out for, because you can never ";
	quote += "predict when they're going to do something incredibly... stupid.";

	std::istringstream stream( quote );

	MyAVLTree<std::string, unsigned> tree;

	countWords(stream, tree);
	EXPECT_TRUE(tree.find("dishonest") == 3);
}

TEST(PostCheckPoint, Simple)
{
	std::string quote = "a a a a a a a a a a b c d e e ";

	std::istringstream stream( quote );

	MyAVLTree<std::string, unsigned> tree;

	countWords(stream, tree);
	EXPECT_TRUE(tree.find("a") == 10);
	EXPECT_TRUE(tree.find("b") == 1);
	EXPECT_TRUE(tree.find("c") == 1);
	EXPECT_TRUE(tree.find("d") == 1);
	EXPECT_TRUE(tree.find("e") == 2);
}

}