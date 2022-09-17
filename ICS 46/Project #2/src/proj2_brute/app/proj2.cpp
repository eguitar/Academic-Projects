#include "proj2.hpp"
#include "LLQueue.hpp"
#include <vector>
#include <iostream>

bool vector_contains(std::vector<unsigned>& num, unsigned n);

void countPaths(const std::vector<std::vector<unsigned>>& friends, unsigned start, std::vector<unsigned>& pathLengths, std::vector<unsigned>& numShortestPaths)
{
    pathLengths.clear();
    numShortestPaths.clear();

    unsigned temp;
    unsigned length;
    unsigned count;
    unsigned i;
    bool found = false;

    std::vector<unsigned> discovered;
    discovered.push_back(start);

    for (unsigned j = 0; j < friends.size(); ++j)
    {
        if (start == j)
        {
            pathLengths.push_back(0);
            numShortestPaths.push_back(1);
            continue;
        }

        length = 0;
        count = 0;
        found = false;
        i = 1;

        LLQueue<unsigned> q;
        q.enqueue(start);
        
        discovered.clear();

        while (!found)
        {
            int s = q.size();
            for (int k = 0; k < s; ++k)
            {
                temp = q.front();
                q.dequeue();
                for (unsigned a : friends[temp])
                {
                    if (!vector_contains(discovered,a))
                    {
                        if (a == j && !found)
                        {
                            length = i;
                            count++;
                            found = true;
                        }
                        else if (a == j)
                        {
                            count++;
                        }
                        else if (!found)
                        {
                            std::cout << a << std::endl;
                            q.enqueue(a);
                            discovered.push_back(a);
                        }
                    }
                }
            }
            i++;
        }
        std::cout << j << " " << length << " " << count << std::endl;
        
        pathLengths.push_back(length);
        numShortestPaths.push_back(count);
    }
}


bool vector_contains(std::vector<unsigned>& num, unsigned n)
{
    return std::count(num.begin(),num.end(),n) != 0;
}