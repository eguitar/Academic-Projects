#ifndef __PROJ2_QUEUE_HPP
#define __PROJ2_QUEUE_HPP

#include "runtimeexcept.hpp"

class QueueEmptyException : public RuntimeException 
{
public:
	QueueEmptyException(const std::string & err) : RuntimeException(err) {}
};

template<typename Object>
struct Node
{
	Object item;
	Node* next;
};

template<typename Object>
class LLQueue
{
private:
	size_t size_q;
	Node<Object> *front_q, *back_q;

public:
	LLQueue();
	LLQueue(const LLQueue & st);
	LLQueue<Object> & operator=(const LLQueue<Object> & st);
	~LLQueue();

	size_t size() const noexcept;
	bool isEmpty() const noexcept;

	Object & front();
	const Object & front() const;

	void enqueue(const Object & elem);

	void dequeue();
};

template<typename Object>
LLQueue<Object>::LLQueue()
{
	front_q = back_q = nullptr;
	size_q = 0;
}

template<typename Object>
LLQueue<Object>::LLQueue(const LLQueue & st)
{
	
}

template<typename Object>
LLQueue<Object> & LLQueue<Object>::operator=(const LLQueue<Object> & st)
{
	
}

template<typename Object>
LLQueue<Object>::~LLQueue()
{
	
}


template<typename Object>
size_t LLQueue<Object>::size() const noexcept
{
	return size_q;
}

template<typename Object>
bool LLQueue<Object>::isEmpty() const noexcept
{
	if (size_q == 0)
		return true;
	else
		return false;
}


template<typename Object>
Object & LLQueue<Object>::front()
{
	if (size_q == 0)
		throw QueueEmptyException("Attempt to return front item of empty queue");
	else
		return front_q -> item;
}

template<typename Object>
const Object & LLQueue<Object>::front() const
{
	if (size_q == 0)
		throw QueueEmptyException("Attempt to return front item of empty queue");
	else
		return front_q -> item;
}


template<typename Object>
void LLQueue<Object>::enqueue(const Object & elem)
{
	Node<Object>* node = new Node<Object>;
	node -> item = elem;

	if (back_q == nullptr)
		front_q = node;
	else
		back_q -> next = node;	

	back_q = node;
	size_q++;
	return;
}


template<typename Object>
void LLQueue<Object>::dequeue()
{
	if (size_q == 0)
		throw QueueEmptyException("Attempt to dequeue empty queue");
	if (size_q == 1)
	{
		delete front_q;
		front_q = back_q = nullptr;
	}
	else
	{
		Node<Object>* temp = front_q;
		front_q = front_q -> next;
		delete temp;
	}
	size_q--;
	return;
}




#endif 
