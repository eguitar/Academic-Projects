#include "proj2.hpp"
#include "LLQueue.hpp"
#include <vector>
#include <iostream>

bool vector_contains(std::vector<unsigned>& num, unsigned n);


void countPaths(const std::vector<std::vector<unsigned>>& friends, unsigned start, std::vector<unsigned>& pathLengths, std::vector<unsigned>& numShortestPaths)
{
    unsigned temp;
    unsigned length;
    unsigned count;
    unsigned i;
    bool found = false;

    std::vector<unsigned> discovered;

    for (unsigned j = 0; j < friends.size(); ++j)
    {
        if (start == j)
            continue;

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
                if (vector_contains(discovered,temp))
                    continue;
                for (unsigned a : friends[temp])
                {
                    if (a == j)
                    {
                        length = i;
                        found = true;
                    }
                    else if (!found)
                        q.enqueue(a);
                }
                discovered.push_back(temp);
            }
            i++;
        }
        pathLengths.at(j) = length;  
    }

    
    
    for (unsigned j = 0; j < friends.size(); ++j)
    {
        
        // std::cout << "END NODE ______________ " << j << std::endl;
        if (start == j)
        {
            numShortestPaths.at(start) = 1;
            // std::cout << numShortestPaths.at(j) << std::endl;
            continue;
        }
    
        count = 0;
        found = false;

        LLQueue<unsigned> q;
        q.enqueue(start);
        discovered.clear();
        // std::cout << "PATHLENGTH - " << pathLengths[j] << std::endl;
        for (unsigned z = 1; z <= pathLengths[j]; ++z)
        {
            if (found)
                break;
            int s = q.size();
            // std::cout << "z is  ---- " << z << std::endl;
            // std::cout << "q is  ---- " << s << std::endl;
            // std::cout << s << std::endl;
            for (int k = 0; k < s; ++k)
            {
                
                temp = q.front();
                q.dequeue();
                // std::cout << "Search - " << temp << std::endl;
                
                for (unsigned a : friends[temp])
                {
                    // std::cout << "Node " << a << std::endl;

                    if (pathLengths[temp] < pathLengths[a])
                    {
                        // std::cout << "yay" << std::endl;
                        if (a == j)
                        {
                            count++;
                            found = true;
                            // std::cout << "found     *" << std::endl;
                        }
                        else
                        {
                            q.enqueue(a);
                            // std::cout << "add" << std::endl;
                        }
                            
                    }
                } // through all adjacent vertices (going forward)
                // std::cout << std::endl;
            } // through queue
        } // each increment of BFS search
        numShortestPaths.at(j) = count;
        // std::cout << numShortestPaths.at(j) << std::endl;
    } // for (each num in graph)

    

    
}

bool vector_contains(std::vector<unsigned>& num, unsigned n)
{
    return std::count(num.begin(),num.end(),n) != 0;
}