/*
Problem: Number of Islands
(https://leetcode.com/problems/number-of-islands/)

Below you will find 2 implementations:
1. Implentation 1 is a DFS in place of the array. It is much more efficient.
2. Implementation 2 is a DFS where I rip the graph out, and recreate it using
dynamic memory nodes.

*/

#include <iostream>
#include <string>
#include <vector>
#include <sstream>
#include <unordered_map>
using namespace std;

/*
struct Node {
	int row;
	int column;
	bool alreadyTraversed = false;
	//left, right, up, down
	vector<Node*> connections;
};

void deleteIsland(Node* island) {
	island->alreadyTraversed = true;
	for (int childIsland = 0; childIsland < island->connections.size(); childIsland++) {
		if (island->connections[childIsland] != NULL && island->connections[childIsland]->alreadyTraversed == false) {
			deleteIsland(island->connections[childIsland]);
		}
	}
}
int numIslands(vector< vector<char> >& grid) {
	unordered_map<string, Node*> islands;
    for (int rows = 0; rows < grid.size(); rows++) {
    	for (int columns = 0; columns < grid[rows].size(); columns++) {
    		if (grid[rows][columns] !=  '0') {
	    		Node* island = new Node();
	    		island->row = rows;
	    		island->column = columns;
	    		island->connections.push_back(NULL);
	    		island->connections.push_back(NULL);
	    		island->connections.push_back(NULL);
	    		island->connections.push_back(NULL);
	    		if (rows !=  0) {	
	    			stringstream ss;
	    			ss << rows - 1 << "," << columns;
	    			string toFind = ss.str();
    				if (islands.count(toFind)) {
    					island->connections[2] = islands[toFind];
    					islands[toFind]->connections[3] = island;
    				}
	    		}
	    		if (columns !=  0) {	
	    			stringstream ss;
	    			ss << rows << "," << columns - 1;
	    			string toFind = ss.str();
    				if (islands.count(toFind)) {
    					island->connections[0] = islands[toFind];
    					islands[toFind]->connections[1] = island;
    				}
	    		}
	    		stringstream ss;
				ss << rows << "," << columns;
				string key = ss.str();
	    		islands[key] = island;
    		} 
    	}
	}
	int count = 0;
	for(unordered_map<string, Node*>::iterator iterator = islands.begin(); iterator != islands.end(); iterator++) {
		if (iterator->second->alreadyTraversed == false) {
			count++;
			deleteIsland(iterator->second);
		}
	}
	return count;
}
*/

void connectedOnesToZero(int i, int j, vector< vector<char> >* grid) {
	//Note: (*grid)[i][j] == '0' must be at the end of the condition tests 
	//due to the fact that it may try to access an unallocated memory location
	//if the values of i and/or j are invalid (i.e. the other conditions being satisfied).
	//Since C++ uses short-circuiting, it tests the  conditions in order and if
	//one condition is satisfied (for 'or') the rest are not tested.
	//Hence, if (*grid)[i][j] == '0' were placed at the end, it will only be tested/
	//memory location accessed if it exists (values of i and j are not
	//invalid, meaning the other conditions don't return true/satsified).
	if (i < 0 || j < 0 || i >= (*grid).size() || j >= (*grid)[i].size() || (*grid)[i][j] == '0') {
		return;
	}
	(*grid)[i][j] = '0';

	connectedOnesToZero(i-1, j, grid);
	connectedOnesToZero(i+1, j, grid);
	connectedOnesToZero(i, j-1, grid);
	connectedOnesToZero(i, j+1, grid);
}
int numIslands(vector< vector<char> >& grid) {
	int numberOfIslands = 0;
	for (int i = 0; i < grid.size(); i++) {
		for (int j = 0; j < grid[i].size(); j++) {
			if (grid[i][j] == '1') {
				numberOfIslands++;
				connectedOnesToZero(i, j, &grid);
			}
		}
	}
	return numberOfIslands;
}

int main() {
	vector < vector<char> > temp1;
	vector <char> temp2;
}