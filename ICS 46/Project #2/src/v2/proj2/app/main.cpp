#include <iostream>
#include <string>
#include <vector>
#include "LLQueue.hpp"




int main()
{
    LLQueue<int> q1;
	q1.enqueue(1);
	q1.enqueue(2);
	q1.enqueue(3);
	q1.enqueue(4);
	q1.enqueue(5);

	// LLQueue<int> q2 = q1;
	// q2.dequeue();


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

