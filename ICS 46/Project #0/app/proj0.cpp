#include <unordered_map>
#include <string>
#include <iostream>
#include "proj0.hpp"

unsigned convertToNum(std::string s, const std::unordered_map<char, unsigned> & mapping);

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