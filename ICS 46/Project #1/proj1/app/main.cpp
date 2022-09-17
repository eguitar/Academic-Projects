// If you really want to make a program for the app, be my guest.
// You may prefer to do so in /exp instead.
// Or better yet, use gtest to automate your own test cases!
#include "proj1.hpp"
#include <iostream>


int main()
{
    std::unordered_map<char,unsigned> mp;
    bool A = puzzleSolver("UCI", "ALEX", "MIKE",mp);
    // bool A = puzzleSolver("AABBCCDDEEAABBCCDDEE", "FFGGHHIIJJFFGGHHIIJJ", "ABCDEFGHIJABCDEFGHIJ",mp);
    std::cout << A << std::endl;

    for (auto const &pair: mp)
        std::cout << "{" << pair.first << ": " << pair.second << "}";

    std::cout << std::endl;

    return 0;
}