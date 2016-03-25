/*
Problem: Number of Islands
(https://leetcode.com/problems/number-of-islands/)

Below you will find 2 implementations:
1. Implentation 1 is a DFS in place of the array. It is much more efficient.
2. Implementation 2 is a DFS where I rip the graph out, and recreate it using
nodes on the heap, for practice. 

*/

#include <iostream>
#include <string>
#include <vector>
#include <sstream>
#include <unordered_map>
using namespace std;
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



int main() {
	vector < vector<char> > temp1;
	vector <char> temp2;
}