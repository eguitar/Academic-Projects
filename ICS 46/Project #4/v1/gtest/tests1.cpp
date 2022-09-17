#include "gtest/gtest.h"
#include "MyAVLTree.hpp"
#include "proj4.hpp"
#include <string>
#include <sstream>
#include <vector>

namespace{


// NOTE:  these are not intended as exhaustive tests.
// This should get you started testing.

// The four tests marked "CheckPoint" are going to be run
// on your submission for the checkpoint code.
// This is worth one-sixth of your grade on the assignment
// and is due at the time marked "checkpoint"


// None of the "checkpoint" tests require you to have
// AVL functionality OR the counting of words.
// Implementing your tree as a plain binary search
// tree is more than enough to pass these tests.

// Of course, you are expected to implement AVL functionality
// for the full project.

// BE SURE TO FULLY TEST YOUR CODE.
// This means making sure your templating is not hard-coding for 
// a specific type, that every function is called somewhere in 
// your test cases, etc. 
// There will NOT be a project 2 style redo for this;  if your 
//  code does not compile, your score will be a zero. 


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

TEST(CheckPoint, CheckPoint_AddMany)
{
	MyAVLTree<int, std::string> tree;
	tree.insert(5, "foo");
	tree.insert(3, "sna");
	tree.insert(10, "bar");
	tree.insert(12, "twelve");
	tree.insert(15, "fifteen");
	tree.insert(123, "foo");
	tree.insert(23, "sna");
	tree.insert(34, "bar");
	tree.insert(56, "twelve");
	tree.insert(34, "fifteen");

	EXPECT_TRUE( tree.size() == 10 );
	EXPECT_TRUE( tree.contains(34) );
}



// TEST(PostCheckPoint, InOrderTraversal)
// {
// 	MyAVLTree<int, std::string> tree;
// 	tree.insert(5, "foo");
// 	tree.insert(3, "sna");
// 	tree.insert(10, "bar");
// 	tree.insert(12, "twelve");
// 	tree.insert(15, "fifteen");

// 	std::vector<int> trav = tree.inOrder();
// 	std::vector<int> expected = {3, 5, 10, 12, 15};
// 	EXPECT_TRUE( trav == expected );
// }



// TEST(PostCheckPoint, JackSparrow)
// {
// 	std::string quote = "I'm dishonest, and a dishonest man you can ";
// 	quote += "always trust to be dishonest. Honestly. It's the honest ";
// 	quote += "ones you want to watch out for, because you can never ";
// 	quote += "predict when they're going to do something incredibly... stupid.";

// 	std::istringstream stream( quote );

// 	MyAVLTree<std::string, unsigned> tree;

// 	countWords(stream, tree);
// 	EXPECT_TRUE(tree.find("dishonest") == 3);
// }

}