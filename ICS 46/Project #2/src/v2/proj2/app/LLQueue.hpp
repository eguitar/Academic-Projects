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
	struct Node* next;
};


template<typename Object>
class LLQueue
{
private:
	Node<Object> *front_q, *rear_q;
	size_t size_q;

public:
	LLQueue();
	LLQueue(const LLQueue & st);
	LLQueue & operator=(const LLQueue & st);
	~LLQueue();

	size_t size() const noexcept;
	bool isEmpty() const noexcept;

	Object & front();
	const Object & front() const;

	void enqueue(const Object & elem);

	void dequeue();

	Node<Object>* front_node();
	Node<Object>* front_node() const;
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
	Node<Object>* current = st.front_node();
	while (current != nullptr)
	{
		Object elem = current -> item;
		enqueue(elem);



		current = current -> next;
	}
	
}

template<typename Object>
LLQueue<Object>& LLQueue<Object>::operator=(const LLQueue & st)
{
	
	
	return *this;
}

template<typename Object>
LLQueue<Object>::~LLQueue()
{
	Node<Object>* current;
	Node<Object>* temp = front_q;
	while (temp != nullptr)
	{
		current = temp;
		temp = temp -> next;
		delete current;
	}
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
		throw QueueEmptyException("Attempt to return front item of empty queue");
	else
		return front_q -> item;
}


template<typename Object>
const Object& LLQueue<Object>::front() const
{
	if (size_q == 0)
		throw QueueEmptyException("Attempt to return front item of empty queue");
	else
		return front_q -> item;
}


template<typename Object>
void LLQueue<Object>::enqueue(const Object & elem)
{
	Node<Object>* n = new Node<Object>;
	n -> item = elem;

	if (front_q == nullptr && rear_q == nullptr)
		front_q = n;
	else
		rear_q -> next = n;

	rear_q = n;
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
		front_q = rear_q = nullptr;
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


template<typename Object>
Node<Object>* LLQueue<Object>::front_node()
{
	if (size_q == 0)
		return nullptr;
	else
		return front_q;
}


template<typename Object>
Node<Object>* LLQueue<Object>::front_node() const
{
	if (size_q == 0)
		return nullptr;
	else
		return front_q;
}

#endif 