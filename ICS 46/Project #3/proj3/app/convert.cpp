#include "convert.hpp"
#include "Wordset.hpp"
#include <iostream>
#include <set>
#include <sstream>
#include <map>
#include <stack>
#include <queue>
#include <vector>

// You should not need to change this function.
void loadWordsIntoTable(WordSet & words, std::istream & in)
{
	std::string line, word;
	std::stringstream ss;

	while(	getline(in, line) )
	{
		ss.clear();
		ss << line;
		while( ss >> word )
		{
			words.insert( word );
		}
	}

}


std::queue<std::string> generateWords(const std::string & s)
{
    std::queue<std::string> words;
    std::vector<char> abc = {'a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z'};
    std::string temp;
    for (unsigned i = 0; i < s.size(); ++i)
    {
        for (unsigned j = 0; j < 26; ++j)
        {
            temp = s;
            if (s[i] != abc[j])
            {
                temp[i] = abc[j];
                words.push(temp);
            }
        }
    }
    return words;
}


// You probably want to change this function.
std::vector< std::string > convert(const std::string & s1, const std::string & s2, const WordSet & words)
{
	std::vector< std::string > path;
	std::map< std::string, std::string > map;
    std::queue<std::string> search;
    search.push(s1);
    
    std::queue<std::string> word_queue;
    std::string current;
    std::string temp;
    bool found = false;

    if (s1 == s2)
    {
        path.push_back(s1);
        path.push_back(s2);
        return path;
    }

    while (!found)
    {
        int q_size = search.size();
        if (q_size == 0)
            return path;
        for (int k = 0; k < q_size; ++k)
        {
            current = search.front();
            search.pop();
            word_queue = generateWords(current);
            while (word_queue.size() != 0 && !found)
            {
                temp = word_queue.front();
                word_queue.pop();
                if (words.contains(temp) && map[temp] == "")
                {
                    search.push(temp);
                    map[temp] = current;
                    
                    if (temp == s2)
                        found = true;
                }
            }
            if (found)
                break;
        }
    }

    std::stack<std::string> word_stack;
    word_stack.push(s2);
    temp = s2;
    while (true)
    {
        temp = map[temp];
        word_stack.push(temp);\
        if (temp == s1)
            break;
    }

    while (word_stack.size() != 0)
    {
        path.push_back(word_stack.top());
        word_stack.pop();
    }
	return path;
}
