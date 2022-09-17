#include "gtest/gtest.h"
#include "LLQueue.hpp"
#include "proj2.hpp"


namespace{


// NOTE:  these are not intended as exhaustive tests.
	// This should get you started testing.
	// You should make your own additional tests for both queue
	// and for the social network question.
	// VERY IMPORTANT:  if your LLQueue is not templated, or if 
	//		it is not linked-list based, your score for this project
	//		will be zero.  Be sure your LLQueue compiles and runs 
	// 		with non-numeric data types. 

TEST(QueueTest, QueueTest1)
{
	LLQueue<int> a;
	a.enqueue(5);
	EXPECT_TRUE( a.front() == 5 );
}

TEST(QueueTest, QueueTest2)
{
	LLQueue<int> a;
	a.enqueue(5);
	a.enqueue(3);
	EXPECT_TRUE( a.front() == 5 );
}


TEST(QueueTest, QueueTest3)
{
	LLQueue<int> a;
	a.enqueue(5);
	a.enqueue(3);
	a.dequeue();
	EXPECT_TRUE( a.front() == 3 );
}

TEST(QueueTest, QueueTest4)
{
	LLQueue<int> q1;
	q1.enqueue(1);
	q1.enqueue(2);
	q1.enqueue(3);
	q1.enqueue(4);
	q1.enqueue(5);

	LLQueue<int> q2 = q1;
	q2.dequeue();

	EXPECT_TRUE(q1.front() == 1 );

	EXPECT_TRUE(q2.front() == 2 );
}

// TEST(GraphTest, GraphTest1)
// {
// 	std::vector< std::vector<unsigned> > g1 = {
// 		{1,2}, {0,3}, {0,3}, {1,2}
// 	};
// 		std::vector<unsigned> pathLengths(4);
// 	std::vector<unsigned> numShortestPaths(4);
	
// 	countPaths(g1, 0, pathLengths, numShortestPaths);

// 	std::vector<unsigned> expPathLengths = {0, 1, 1, 2};
// 	std::vector<unsigned> expNumSP = {1, 1, 1, 2};

// 	EXPECT_TRUE(pathLengths == expPathLengths && expNumSP == numShortestPaths);

// }


// TEST(GraphTest, GraphTest2)
// {
// 	std::vector< std::vector<unsigned> > g1 = {
// 		{1, 2, 4}, {0,3}, {0,3}, {1,2,5}, {0, 5}, {3, 4}
// 	};
	
// 	std::vector<unsigned> pathLengths(6);
// 	std::vector<unsigned> numShortestPaths(6);
	
// 	countPaths(g1, 0, pathLengths, numShortestPaths);

// 	std::vector<unsigned> expPathLengths = {0, 1, 1, 2, 1, 2};
// 	std::vector<unsigned> expNumSP = {1, 1, 1, 2, 1, 1};

// 	EXPECT_TRUE(pathLengths == expPathLengths && expNumSP == numShortestPaths);
// }

// TEST(GraphTest, GraphTest3)
// {
// 	std::vector< std::vector<unsigned> > g1 = {
// 		{1, 2, 4}, {0,3}, {0,3}, {1,2,5, 7}, {0, 5, 6}, {3, 4}, {4, 7}, {3, 6},
// 	};
	
// 	std::vector<unsigned> pathLengths(8);
// 	std::vector<unsigned> numShortestPaths(8);
	
// 	countPaths(g1, 0, pathLengths, numShortestPaths);

// 	std::vector<unsigned> expPathLengths = {0, 1, 1, 2, 1, 2, 2, 3};
// 	std::vector<unsigned> expNumSP = {1, 1, 1, 2, 1, 1, 1, 3};

// 	EXPECT_TRUE(pathLengths == expPathLengths && expNumSP == numShortestPaths);

// }

// TEST(GraphTest, GraphTest1K) //sample test case taken from class discussion
// {
//   unsigned k{1000};
//   std::vector<std::vector<unsigned> > g1 = {{999,1}};
//   for(unsigned i=1;i<k;++i){
//     std::vector<unsigned> v = {(i-1)%k,(i+1)%k};
//     g1.push_back(v);
//   }
//   std::vector<unsigned> pathLengths(k);
//   std::vector<unsigned> numShortestPaths(k);

//   countPaths(g1, 0, pathLengths, numShortestPaths);

//   std::vector<unsigned> expPathLengths;
//   for(unsigned i=0;i<500;++i){
//     expPathLengths.push_back(i);
//   }
//   for(unsigned i=500;i>0;--i){
//     expPathLengths.push_back(i);
//   }
//   std::vector<unsigned> expNumSP(k,1);
//   expNumSP[500] = 2;
  
//   EXPECT_TRUE(pathLengths == expPathLengths && expNumSP == numShortestPaths);
// }

}
