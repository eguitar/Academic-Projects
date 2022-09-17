#include "Wordset.hpp"
#include <string>
#include <queue>

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

WordSet::WordSet(unsigned initialCapacity, unsigned evictionThreshold)
{
	std::string* table1 = new std::string[initialCapacity];
	std::string* table2 = new std::string[initialCapacity];
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
	unsigned index1 = polynomialHashFunction(s, BASE_H1, capacity);
	if (table1[index1] == "")
	{
		table1[index1] = s;
		size++;
		return;
	}
	else
	{
		{/* code */}
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
