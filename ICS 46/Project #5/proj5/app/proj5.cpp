#include "proj5.hpp"
#include "MyPriorityQueue.hpp"

bool mst_contains(unsigned num,std::vector<Edge> & mst)
{
	for (Edge e : mst)
		if (e.pt1 == num || e.pt2 == num)
			return true;

	return false;
}


// As a reminder, for this project, edges have positive cost, g[i][j] = 0 means no edge.
std::vector<Edge> compute_mst(const std::vector< std::vector<unsigned>> & graph)
{
	std::vector<Edge> mst;
	MyPriorityQueue<Edge> pq;
	Edge temp = Edge(0,0,0);

	unsigned n = graph.size();

	for (int i = 0; i < n; i++)
        if (graph[0][i] != 0)
            pq.insert(Edge(0,i,graph[0][i]));

	while (!pq.isEmpty())
	{
		temp = pq.min();
		pq.extractMin();
		if (!mst_contains(temp.pt2,mst))
		{
			
			mst.push_back(temp);
			for (int i = 0; i < n; i++)
			{
				if (graph[temp.pt2][i] != 0)
				{
					pq.insert(Edge(temp.pt2,i,graph[temp.pt2][i]));
				}
			}
		}
	}
	return mst;
}


// Returns the cost of the edges in the given vector,
// This does not confirm that it is a MST at all.  
unsigned mstCost(const std::vector<Edge> & vE) 
{
	unsigned sum =0;
	for(auto e: vE)
	{
		sum += e.weight;
	}
	return sum;
}
