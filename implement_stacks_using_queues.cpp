# Problem: Implement Stacks Using Queus
# (https://leetcode.com/problems/implement-stack-using-queues/description/)

#include <queue>

class MyStack {
    queue<int> q;
    
public:    
    /** Initialize your data structure here. */
    MyStack() {
        
    }
    
    /** Push element x onto stack. */
    void push(int x) {
        q.push(x);
    }
    
    /** Removes the element on top of the stack and returns that element. */
    int pop() {
        int counter = 0;
        while (counter < q.size() - 1) {
            q.push(q.front());
            q.pop();
            counter++;
        }
        int res = q.front();
        q.pop();
        return res;
    }
    
    /** Get the top element. */
    int top() {
       return q.back(); 
    }
    
    /** Returns whether the stack is empty. */
    bool empty() {
        return q.empty();
    }
};

/**
 * Your MyStack object will be instantiated and called as such:
 * MyStack obj = new MyStack();
 * obj.push(x);
 * int param_2 = obj.pop();
 * int param_3 = obj.top();
 * bool param_4 = obj.empty();
 */