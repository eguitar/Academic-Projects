#ifndef __PROJ5_PRIORITY_QUEUE_HPP
#define __PROJ5_PRIORITY_QUEUE_HPP

#include "runtimeexcept.hpp"
#include <vector>
#include <algorithm>
#include <iostream>


class PriorityQueueEmptyException : public RuntimeException 
{
public:
	PriorityQueueEmptyException(const std::string & err) : RuntimeException(err) {}
};


template<typename Object>
class MyPriorityQueue
{
private:
	std::vector<Object> queue;
	size_t tree_size;


public:
	MyPriorityQueue();

	~MyPriorityQueue();

 	size_t size() const noexcept;
	bool isEmpty() const noexcept;

	void insert(const Object & elem);

	const Object & min() const; 

	void extractMin(); 
};


template<typename Object>
MyPriorityQueue<Object>::MyPriorityQueue()
{
	tree_size = 0;
}

template<typename Object>
MyPriorityQueue<Object>::~MyPriorityQueue()
{
}

template<typename Object>
size_t MyPriorityQueue<Object>::size() const noexcept
{
	return tree_size;
}

template<typename Object>
bool MyPriorityQueue<Object>::isEmpty() const noexcept
{
	if (tree_size == 0)
		return true;
	else
		return false;	
}

template<typename Object>
void MyPriorityQueue<Object>::insert(const Object & elem) 
{
	queue.push_back(elem);
	tree_size++;

	unsigned cur = tree_size;
	unsigned par = (tree_size / 2);

	while (cur > 1)
	{
		if (queue[par-1] < queue[cur-1])
			break;
		std::swap(queue[cur-1],queue[par-1]);
		cur = par;
		par = cur / 2;
	}
}

template<typename Object>
const Object & MyPriorityQueue<Object>::min() const
{
	if (this->isEmpty())
		throw PriorityQueueEmptyException("PQ is empty.");
	else
		return queue[0];
}

template<typename Object>
void MyPriorityQueue<Object>::extractMin() 
{
	if (this->isEmpty())
		throw PriorityQueueEmptyException("PQ is empty.");

	std::swap(queue[0],queue[tree_size-1]);
	queue.pop_back();
	tree_size--;

	unsigned cur = 1;
	unsigned temp;
	unsigned left;
	unsigned right;

	while (true)
	{
		temp = cur;
		left = 2 * cur;
		right = 2 * cur + 1;
		
		if (left <= tree_size && queue[left-1] < queue[temp-1])
			temp = left;

		if (right <= tree_size && queue[right-1] < queue[temp-1])
			temp = right;

		if (temp != cur)
		{
			std::swap(queue[cur-1],queue[temp-1]);
			cur = temp;
		}
		else
		{
			break;
		}
	}
}

#endif 
