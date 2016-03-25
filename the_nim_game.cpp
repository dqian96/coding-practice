/*

Problem: The Nim Game
(https://leetcode.com/problems/nim-game/)

Informal Proof:

Let A and B denote the two players playing the Nim Game. Player A goes first. 
Let n0 denote the number of stones in the pile, initially. 

Theorem: Player A will lose if the number of stones in the pile is a multiple of 4 (n0 % 4 == 0).

Let’s look at the base cases:
For n0 = 1, A wins
For n0 = 2, A wins
For n0 = 3, A wins
For n0 = 4, A loses. 
Following this, A wins for 5,6,7 and loses for 8. 
We therefore know that n0 = 4 is the BASE losing case.

For n0>4, there are two cases n0 = 4a or n0 != 4a, for some integer a > 1. 

Case 1, n0 = 4a, a > 1:

If n0 = 4a, then no matter how many stones player A chooses to take, player B can take a number of stones such that n1, the number of stones left in the pile after both players A and B make their moves, is a multiple of 4. This is because after both players make their moves, the sum of the stones taken away can be equal to 4. Therefore, the number of stones left after both players A and B make their moves is a multiple of 4, where A has to pick from the pile. Eventually, the number of stones will decrease by 4’s until there are 4 stones left for A’s turn to pick. Trivially, we know A then loses the game.

More formally,
Let ni be the number of stones left in the ith “cycle” of turns (i >= 0), where each cycle denotes the event where A and B take their respective stones (i.e. it is A’s turn to pick again from n(i+1)).

Let ji be the number of stones player A takes in the ith cycle and ki be the number of stones player B takes in the ith cycle.

ni+1 = ni - (ji + ki), where A has to pick from ni+1 

We know that for any ji player A could pick (ji = 1, 2, or 3), there exists ki such that ji + ki = 4.

Therefore,
ni+1 = ni - 4, where A has to pick.

We know that n0 = 4a (inductive hypothesis). Assuming that np = 4b, for some integer b > 1, prove np+1 is a multiple of 4:
np+1 = np - 4 from above
np+1 = 4b - 4
np+1 = 4c for some c > 0.

Therefore, if there are a multiple of stones in the pth cycle, there will be a multiple of stones left in the p+1 cycle.

As np+1 < np and both are multiples of 4, we can affirm that the number of stones in the pile after every cycle is a multiple of 4 and is smaller in number than the previous cycle. 

Eventually, for sufficient p, np+1 = 4 for player A to pick. Trivially, A loses the game.

Case 2, n0 = 4a + b, a > 1, 1 <= b <= 3:

It is initially A’s turn to pick. If A picks b stones in this first turn, B will be left with a number of stones that is a multiple of 4. This is identical to case 1 but instead for B. Therefore, we know by the logic from case 1 that B loses.

Therefore, we can see that if n = 4a for any integer a > 1, player A will always win if A plays optimally. 

*/

#include <iostream>

using namespace std;

bool canWinNim(int n) {
    return (n % 4);
}

int main() {

}