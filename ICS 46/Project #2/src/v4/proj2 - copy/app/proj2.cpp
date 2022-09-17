#include "proj2.hpp"
#include "LLQueue.hpp"
#include <vector>
#include <iostream>

unsigned minPath(unsigned start, unsigned end, const std::vector<std::vector<unsigned>>& friends);

unsigned numPath(unsigned start, unsigned end, unsigned min, const std::vector< std::vector<unsigned> > & friends);

void countPaths(const std::vector<std::vector<unsigned>>& friends, unsigned start, std::vector<unsigned>& pathLengths, std::vector<unsigned>& numShortestPaths)
{
    pathLengths.clear();
    numShortestPaths.clear();
    for (unsigned i = 0; i < friends.size(); ++i)
    {
        unsigned x = minPath(start,i,friends);
        pathLengths.push_back(x);
        numShortestPaths.push_back(numPath(start,i,x,friends));
    }
}


unsigned minPath(unsigned start, unsigned end, const std::vector<std::vector<unsigned>>& friends)
{
    if (start == end)
        return 0;
    unsigned temp;
    LLQueue<unsigned> q;
    q.enqueue(start);
    for (unsigned i = 1; i <= friends.size(); ++i)
    {
        int s = q.size();
        for (int j = 0; j < s; ++j)
        {
            temp = q.front();
            q.dequeue();
            for (unsigned a : friends[temp])
            {
                if (a == end)
                    return i;
                else
                {
                    q.enqueue(a);
                }
            }
        }
    }
    return -1;
}

unsigned numPath(unsigned start, unsigned end, unsigned min, const std::vector< std::vector<unsigned> > & friends)
{
    if (start == end)
        return 1;
    unsigned count = 0;    
    unsigned temp;
    LLQueue<unsigned> q;
    q.enqueue(start);
    for (unsigned i = 0; i < min; ++i)
    {
        unsigned s = q.size();
        for (unsigned j = 0; j < s; ++j)
        {
            temp = q.front();
            q.dequeue();
            for (unsigned a : friends[temp])
            {
                if (a == end)
                {
                    count++;
                }
                else
                {
                    q.enqueue(a);
                }
            }
        }
    }
    return count;
}