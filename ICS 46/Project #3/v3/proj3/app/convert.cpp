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

// bool isConnected(const std::string & s1, const std::string & s2)
// {
//     unsigned count = 0;
//     for (unsigned i = 0; i < s1.size(); ++i)
//     {
//         if (s1[i] != s2[i])
//         {
//             count++;
//             if (count >= 2)
//                 return false;
//         }
//     }
//     return true;
// }


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

    while (!found)
    {
        int q_size = search.size();
        for (int k = 0; k < q_size; ++k)
        {
            current = search.front();
            search.pop();
            std::cout << "WORD:      " << current << std::endl;
            word_queue = generateWords(current);

            while (word_queue.size() != 0 && !found)
            {
                temp = word_queue.front();
                word_queue.pop();
                if (words.contains(temp))
                {
                    std::cout << temp << std::endl;
                    
                    search.push(temp);
                    map[temp] = current;
                    
                    if (temp == s2)
                    {
                        found = true;
                    }
                }
            }
            if (found)
                break;
        }
    }
	return path;
}
