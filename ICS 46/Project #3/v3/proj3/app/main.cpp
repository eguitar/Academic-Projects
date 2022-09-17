#include <iostream>
#include <fstream>
#include "Wordset.hpp"
#include "convert.hpp"

int main()
{
	WordSet words(11);
	std::ifstream in("words.txt");
	loadWordsIntoTable(words, in);


 	std::vector< std::string > r  = convert("ant", "eat", words);

 	// // this was a success if r was a valid conversion of length 2.
	// std::ifstream in2("words.txt");
    




}

