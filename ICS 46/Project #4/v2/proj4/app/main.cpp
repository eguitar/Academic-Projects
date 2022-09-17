#include "MyAVLTree.hpp"
#include "proj4.hpp"
#include <string>
#include <sstream>
#include <vector>

int main()
{

    std::string quote = "I'm dishonest, and a dishonest man you can ";
	quote += "always trust to be dishonest. Honestly. It's the honest ";
	quote += "ones you want to watch out for, because you can never ";
	quote += "predict when they're going to do something incredibly... stupid.";

	std::istringstream stream( quote );

	MyAVLTree<std::string, unsigned> tree;

	countWords(stream, tree);
}

