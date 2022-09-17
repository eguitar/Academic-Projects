#ifndef __PROJ2_QUEUE_HPP
#define __PROJ2_QUEUE_HPP

#include "runtimeexcept.hpp"

class QueueEmptyException : public RuntimeException 
{
public:
	QueueEmptyException(const std::string & err) : RuntimeException(err) {}
};


template<typename Object>
class LLQueue
{
private:
	// fill in private member data here
	Object *front_q, *rear_q;
	size_t size_q;

public:
	LLQueue();
	LLQueue(const LLQueue & st);
	LLQueue & operator=(const LLQueue & st);
	~LLQueue()
	{
		// You need to implement the destructor also.
	}

	size_t size() const noexcept;
	bool isEmpty() const noexcept;

	// We have two front() for the same reason the Stack in lecture week 2 had two top() functions.
	// If you do not know why there are two, your FIRST step needs to be to review your notes from that lecture.

	Object & front();
	const Object & front() const;

	void enqueue(const Object & elem);

// does not return anything.  Just removes. 
	void dequeue();
};

// TODO:  Fill in the functions here. 



template<typename Object>
LLQueue<Object>::LLQueue()
{
	front_q = rear_q = nullptr;
	size_q = 0;
}


template<typename Object>
LLQueue<Object>::LLQueue(const LLQueue & st)
{

}

template<typename Object>
LLQueue<Object>& LLQueue<Object>::operator=(const LLQueue & st)
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
Object& LLQueue<Object>::front()
{
	if (size_q == 0)
	{
		throw QueueEmptyException("Attempt to return front item of empty queue");
	}
	return *front_q;
}


template<typename Object>
const Object& LLQueue<Object>::front() const
{
	if (size_q == 0)
	{
		throw QueueEmptyException("Attempt to return front item of empty queue");
	}
	return *front_q;
}


template<typename Object>
void LLQueue<Object>::enqueue(const Object & elem)
{
	return;
}


template<typename Object>
void LLQueue<Object>::dequeue()
{
	if (size_q == 0)
	{
		throw QueueEmptyException("Attempt to dequeue empty queue");
	}
	return;
}

#endif 
