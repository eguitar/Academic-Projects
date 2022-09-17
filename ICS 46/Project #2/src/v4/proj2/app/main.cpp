#include <iostream>
#include <string>
#include <vector>
#include "LLQueue.hpp"
#include "proj2.hpp"




int main()
{
    
    std::vector< std::vector<unsigned> > g1 = {
		{1,2}, {0,3}, {0,3}, {1,2}
	};
		std::vector<unsigned> pathLengths(4);
	std::vector<unsigned> numShortestPaths(4);
	
	countPaths(g1, 0, pathLengths, numShortestPaths);

	// for (unsigned i : pathLengths)
    //     std::cout << i << std::endl;

    for (unsigned i : numShortestPaths)
        std::cout << i << std::endl;


    // // std::vector< std::vector<unsigned> > g1 = {{1, 2, 4}, {0,3}, {0,3}, {1,2,5}, {0, 5}, {3, 4}};
    // std::vector< std::vector<unsigned> > g1 = {
    // {1, 2, 4}, {0,3}, {0,3}, {1,2,5, 7}, {0, 5, 6}, {3, 4}, {4, 7}, {3, 6},
	// };
    // std::vector<unsigned> path;
    // std::vector<unsigned> sum;

    // countPaths(g1,0,path,sum);

    // for (unsigned i : path)
    //     std::cout << i << std::endl;

    // std::cout << std::endl;

    // for (unsigned i : sum)
    //     std::cout << i << std::endl;

    // std::cout << minPath(0,0,g1) << std::endl;
    // std::cout << minPath(0,1,g1) << std::endl;
    // std::cout << minPath(0,2,g1) << std::endl;
    // std::cout << minPath(0,3,g1) << std::endl;
    // std::cout << minPath(0,4,g1) << std::endl;
    // std::cout << minPath(0,5,g1) << std::endl;
    
    
    // LLQueue<std::string> q1;
	// q1.enqueue("asdf");
	// q1.enqueue("qwer");
	// q1.enqueue("zxcv");
	// q1.enqueue("poiu");
	// q1.enqueue(";lkj");

	// LLQueue<std::string> q2 = q1;
	
    // // q2.dequeue();

    // q1.dequeue();
	// std::cout << q1.front() << std::endl;
    // q1.dequeue();
	// std::cout << q1.front() << std::endl;
    // q1.dequeue();
	// std::cout << q1.front() << std::endl;
    // q1.dequeue();
	// std::cout << q1.front() << std::endl;
    // q1.dequeue();
	// std::cout << q1.size() << std::endl;

	// std::cout << q2.front() << std::endl;



    // LLQueue<std::string> q2;
    

    // if (q2.size() == 0)
    //     std::cout << "YAY" << std::endl;

    // q2.enqueue("asdf");




    // LLQueue<std::string> q3;
    

    // if (q3.size() == 0)
    //     std::cout << "YAY" << std::endl;

    // q3.enqueue("asdf");


    // try {
    // q.front();
    // }

    // catch(QueueEmptyException& e){
    //     std::cerr << e << std::endl;
    // }

    return 0;
}

