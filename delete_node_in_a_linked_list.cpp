/*
Problem: Delete Node in a Linked List
(https://leetcode.com/problems/delete-node-in-a-linked-list/)

We are only given access to the node being deleted (NE).
Hence, we cannot free the memory of NE since we don't
have the reference to the node that points to NE and so the linked list would break
if we free NE.

As we don't have prior references, we are constrained to keeping NE allocated, and so 
we must shift the properties of the node NE points to, to NE. 
Delete the node NE pointed to since its existence is redundant, and we are done
in O(1) time.

*/


#include <iostream>


using namespace std;

//Definition for singly-linked list.
struct ListNode {
	int val;
	ListNode *next;
	ListNode(int x) : val(x), next(NULL) {}
};

void deleteNode(ListNode* node) {
	if (node->next == NULL) {
		delete node;
		return;
	}
	ListNode* temp = node -> next;
	//dereferencing to copy values
	*node = *temp;
	delete temp;
	return;
}
	

int main() {}