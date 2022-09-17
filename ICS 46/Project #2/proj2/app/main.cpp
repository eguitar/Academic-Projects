#include "proj2.hpp"
#include <iostream>
#include <vector>


int main()
{
	
	std::vector<std::vector<unsigned> > g1 = {{1,2},{0,3,6},{0,3,4,5},{1,2,5,7},{2,6,8},{2,3,7},{1,4,8,9},{3,5,10},{4,6,9,11},{6,8,10,11},{7,9},{8,9}};
	std::vector<unsigned> pathLengths(12);
	std::vector<unsigned> numShortestPaths(12);

	countPaths(g1, 0, pathLengths, numShortestPaths);

	std::vector<unsigned> expPathLengths = {0,1,1,2,2,2,2,3,3,3,4,4};
	std::vector<unsigned> expNumSP = {1,1,1,2,1,1,1,3,2,1,4,3};

    // for (unsigned i : pathLengths){
    //     std::cout << i << std::endl;
    // }  

    // std::cout << std::endl;

    // for (unsigned i : numShortestPaths){
    //     std::cout << i << std::endl;
    // }



// {1,1,1,2,1,1,1,3,2,1,4,3};
	bool x = pathLengths == expPathLengths;
	std::cout << "SUCCESS1 ???? " << x << std::endl;

	bool y = numShortestPaths == expNumSP;
	std::cout << "SUCCESS2 ???? " << y << std::endl;
}

