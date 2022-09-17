#include "Wordset.hpp"
#include <string>
#include <queue>
#include <iostream>

// returns s, as a number in the given base, mod the given modulus
unsigned polynomialHashFunction(const std::string & s, unsigned base, unsigned mod)
{
	std::queue<char> c;
	unsigned temp;
	unsigned mult;
	unsigned sum = 0;
	
	for (auto a = s.end() - 1; a != s.begin() - 1; --a)
    {
        c.push(*a);
    }
    
    unsigned num = c.size();
	for (unsigned i = 0; i < num; ++i)
	{
	    mult = 1;
		temp = int(c.front()) - int('a') + 1;
		c.pop();
		
		for (unsigned j = 0; j < i; ++j)
		    mult *= base;
		
		sum += temp*mult;
	}
	return sum % mod;
}

bool isEmpty(const std::string & s)
{
	return s == "";
}

unsigned nextCapacity(unsigned n)
{
    unsigned prime = n * 2 + 1;
    bool primed;
    while (true)
    {   
        primed = true;
        for (unsigned i = 2; i < prime; ++i)
        {
            if (prime % i == 0)
            {
                primed = false;
                break;
            }
        }
        if (primed)
            return prime;
        else
            prime += 2;
    }
}



void WordSet::print()
{
	std::cout << "TABLE1:" << std::endl;
	for (int i = 0; i < capacity; i++)
	{
		std::cout << i << " ";
		if (isEmpty(table1[i]))
			std::cout << "__" << std::endl;
		else
			std::cout << table1[i] << std::endl;
	}

	std::cout << std::endl;

	std::cout << "TABLE2:" << std::endl;
	for (int i = 0; i < capacity; i++)
	{
		std::cout << i << " ";
		if (isEmpty(table2[i]))
			std::cout << "__" << std::endl;
		else
			std::cout << table2[i] << std::endl;
	}
	std::cout << "##############################" << std::endl;
}



WordSet::WordSet(unsigned initialCapacity, unsigned evictionThreshold)
{
	table1 = new std::string[initialCapacity];
	table2 = new std::string[initialCapacity];
	size = 0;
	capacity = initialCapacity;
	threshold = evictionThreshold;
}

WordSet::~WordSet()
{
	delete[] table1;
	delete[] table2;
}

void WordSet::insert(const std::string & s)
{
	unsigned count = 0;
	unsigned index1 = polynomialHashFunction(s, BASE_H1, capacity);
	if (isEmpty(table1[index1]))
	{
		table1[index1] = s;
		size++;
		return;
	}
	unsigned index2 = polynomialHashFunction(s, BASE_H2, capacity);
	if (isEmpty(table2[index2]))
	{
		table2[index2] = s;
		size++;
		return;
	}
	else
	{
		std::string evicted = table2[index2];
		table2[index2] = s;
		count++;

		while (true)
		{
			// table2 eviction
			index1 = polynomialHashFunction(evicted, BASE_H1, capacity);
			if (isEmpty(table1[index1]))
			{
				table1[index1] = evicted;
				size++;
				return;
			}
			else
			{
				std::swap(evicted,table1[index1]);
				count++;
			}
			
			// table1 eviction
			index2 = polynomialHashFunction(evicted, BASE_H2, capacity);
			if (isEmpty(table2[index2]))
			{
				table2[index2] = evicted;
				size++;
				return;
			}
			else
			{
				std::swap(evicted,table2[index2]);
				count++;
			}

			// RESIZING AND REHASHING
			if (count == threshold)
			{
				unsigned new_capacity = nextCapacity(capacity);
				unsigned old_capacity = capacity;
				capacity = new_capacity;
				size = 0;
				std::string* old_t_1 = table1;
				std::string* old_t_2 = table2;
				table1 = new std::string[new_capacity];
				table2 = new std::string[new_capacity];			
				WordSet::insert(evicted);
				for (unsigned a = 0; a < old_capacity; ++a)
					if (!isEmpty(old_t_1[a]))
						WordSet::insert(old_t_1[a]);
				for (unsigned a = 0; a < old_capacity; ++a)
					if (!isEmpty(old_t_2[a]))
						WordSet::insert(old_t_2[a]);
				delete[] old_t_1;
				delete[] old_t_2;
				return;
			}
		}
	}
}


bool WordSet::contains(const std::string & s) const
{
	unsigned index1 = polynomialHashFunction(s, BASE_H1, capacity);
	if (table1[index1] == s)
		return true;
	unsigned index2 = polynomialHashFunction(s, BASE_H2, capacity);
	if (table2[index2] == s)
		return true;
	return false;
}

// return how many distinct strings are in the set
unsigned WordSet::getCount() const
{
	return size;
}

// return how large the underlying array is.
unsigned WordSet::getCapacity() const
{
	return capacity;
}
