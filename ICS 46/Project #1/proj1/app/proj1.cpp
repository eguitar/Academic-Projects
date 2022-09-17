#include "proj1.hpp"
#include <unordered_map>
#include <string>
#include <vector>
#include <algorithm>


unsigned convertToNum(std::string s, const std::unordered_map<char, unsigned> & mapping);

bool verifySolution(std::string s1, std::string s2, std::string s3, const std::unordered_map<char, unsigned> & mapping);

std::vector<char> findCharacters(std::string s1, std::string s2, std::string s3);

std::vector<char> remainingChar(std::string s1, std::string s2, std::string s3, std::unordered_map<char, unsigned> & mapping);

std::vector<unsigned> getValues(const std::unordered_map<char, unsigned> & mapping);

bool vector_contains(std::vector<unsigned>& num_vector, unsigned n);

bool vector_contains(std::vector<char>& char_vector, char c);



bool puzzleSolver(std::string s1, std::string s2, std::string s3, std::unordered_map<char, unsigned> & mapping)
{
	
	std::vector<char> char_remaining = remainingChar(s1,s2,s3,mapping);
	std::vector<unsigned> num_assigned = getValues(mapping);
	if (char_remaining.size() == 0)
		return verifySolution(s1,s2,s3,mapping);

	for (int i = 0; i < 10; i++)
	{
		if (!vector_contains(num_assigned,i))
		{
			char c = char_remaining.front();
			mapping[c] = i;
			if (puzzleSolver(s1,s2,s3,mapping))
				return true;
			auto temp = mapping.find(c);
			mapping.erase(temp);
		}
	}

	return false;
}


bool verifySolution(std::string s1, std::string s2, std::string s3, const std::unordered_map<char, unsigned> & mapping)
{
    unsigned n1 = convertToNum(s1,mapping);
    unsigned n2 = convertToNum(s2,mapping);
    unsigned n3 = convertToNum(s3,mapping);
    if (n1 + n2 == n3)
    {
        return true;
    }
    else
    {
        return false;
    }
}

unsigned convertToNum(std::string s, const std::unordered_map<char, unsigned> & mapping)
{
    unsigned sum = 0;
    unsigned temp = 0;
    unsigned size = s.length();
    unsigned index = 0;
    for (int i = 0; i < size; i++)
    {
        index = size - i - 1;
        temp = mapping.at(s[index]);
        for (int j = 0; j < i; j++)
        {
            temp = temp * 10;
        }
        sum += temp;
    }
    return sum;
}

std::vector<char> findCharacters(std::string s1, std::string s2, std::string s3)
{
    std::vector<char> ch;
    for (int i = 0; i < s1.size(); i++)
    {
        bool a = std::find(ch.begin(),ch.end(),s1[i]) == ch.end();
        if (a)
        {
            ch.push_back(s1[i]);
        }
    }
    for (int i = 0; i < s2.size(); i++)
    {
        bool b = std::find(ch.begin(),ch.end(),s2[i]) == ch.end();
        if (b)
        {
            ch.push_back(s2[i]);
        }
    }
	for (int i = 0; i < s3.size(); i++)
    {
        bool c = std::find(ch.begin(),ch.end(),s3[i]) == ch.end();
        if (c)
        {
            ch.push_back(s3[i]);
        }
    }
    return ch;
}

std::vector<char> remainingChar(std::string s1, std::string s2, std::string s3, std::unordered_map<char, unsigned> & mapping)
{
	std::vector<char> char_vector = findCharacters(s1,s2,s3);
	std::vector<char> output;
	for (auto i = char_vector.begin(); i != char_vector.end(); i++)
		if (!mapping.count((*i)))
			output.push_back((*i));
	return output;
}

std::vector<unsigned> getValues(const std::unordered_map<char, unsigned> & mapping)
{	
	std::vector<unsigned> num_vector;
	for (auto it = mapping.begin(); it != mapping.end(); it++)
	{
		num_vector.push_back(it->second);
	}
	return num_vector;
}

bool vector_contains(std::vector<unsigned>& num_vector, unsigned n)
{
	auto temp = std::find(num_vector.begin(),num_vector.end(),n);
	return temp != num_vector.end();
}

bool vector_contains(std::vector<char>& char_vector, char c)
{
	auto temp = std::find(char_vector.begin(),char_vector.end(),c);
	return temp != char_vector.end();
}