# How to Kick Ass in Interviews

## Interview soft skills:

1. Think out loud
    * Pretend that you are not talking to someone, but rather that you're talking to yourself
    * Say every thought you have in your mind, no matter what

2. Take your time
    * **There's no need to rush**
    * A metholodical, detailed thought process is better than half-assing it
    * But don't spend too much time on unnecessary explanations; be aware of your time budget

3. Keep calm and be confident
    * **You can do it**
    * Calm yourself down by taking a deep breath before your interview
    * Pep talk yourself
    * It's not the end of the world if you don't get it
    * Be tenacious

4. Ask questions
    * **Ask to confirm your ideas - bounce them**
    * Ask clarification questions
    * Ask for hints, and pay attention to the hints!

5. Don't hesitate to back-track
    * If you get stuck for a few minutes, it's time to **back-track**!
    * Do not **tunnel-vision**. Try to look for different methods and missed details.

## Strategy to solve problems:

1. Understand the question fully, and ask questions to clarify
    * Write down input & output
    * Write down the important details of the question
    * **Read the question thoroughly**
    * Discuss uncertainties

2. Write out some example cases (i.e. input-output)
    * Try to find patterns

3. Give a naive/trivial solution

4. Describe why the naive solution is bad
    * Space/time complexity
    * Redundant computation
    * Doesn't take advantage of pre-existing patterns (i.e array is sorted)

5. Try to come up with a better solution (problem solving and communication skills)
    * Categorize the problem (i.e. graph)
    * Come up with a design strategy (i.e. DFS)
    * Write out examples and try to find patterns
    * Break the problem down into several cases
        * Base case
        * Edge case
        * Normal case
    * Find some way to model the problem (i.e. esp useful for graphs)
    * Decompose the problem (i.e. to solve x, I need y... to solve y, I need z...etc.)
        * Break the problem down to get mini-objectives
        * Find solutions to mini-objectives
        * Combine solutions
    * Determine tautologies and patterns
    * Determine how the naive solution can be improved (i.e. caching, preventing duplicate work)
    * Discuss tradeoffs, uncertainties, access patterns

6. Write down the steps to the algorithm (i.e. first, second, third)
    * Like actually write it down
    * Use precise names to describe some variable/state/system/value/point of interest, as names
       give something power
    * **Completely run through examples and be explicit about the details of your algo**
    * Ask if your solution makes sense

7. Start coding and talk about your implementation (highlight software engineering practices)
    * Use clear and understandable variable names
    * Stub methods (top-down programming) in order to get the high level flow down first
    * Comment and chunk code (i.e. add new lines between logically seperate blocks)
    * Practice modularity by using helper methods generously
        * This allows you to update/improve implementation of components without affecting the
           rest of the code (constant interface)
        * **Unit test individual components** to reduce difficulty in debugging 
    * Adhere to agile methodology - develop iteratively
        * **Premature optimization is the root of all evil**
        * You can implement a trivial algorithm to start, and iteratively improve on it later
        * Assuming your implementation is modular, iteratively improving your code should be trivial (little code to change)
        * A solution is better than no solution
        
8. Run through an example test case (trace through the program) to make sure it works
    * Do this before actually running the code
    * Completely run through the example
    * Don't forget edge cases

9. Analyze your solution (time and space complexity)

10. Check if it can be improved
    * Discuss tradeoffs (i.e. time v.s. space)


Problem Types:

1. Bit Manipulation
    * Bit shifts
    * Boolean operators (AND, OR, XOR, etc.)
    * XOR (x ^ x = 0, 0 ^ x = x)
    * Tries, as a binary number is just a string of 1's and 0's

2. Dynamic Programming
    * Optimization problems
    * Memoization (top-down)
    * DP (bottom-up)
    * Runtime is size of table (set of unique subproblems solved repeatedly)
    * Recurrence relation (the "last" problem)
    * Problem can be split up into several subproblems; can combine the subproblems' solutions to solve the main problem
    * Tautologies (i.e. the end of the longest palindromic substring must be at ONE of the string's characters)
        i.e. what's the LPS that ends at index i, and how can I use that to solve the LPS for index i + 1
        i.e. 'last' analysis; the last partition/jump/etc. can only be one of the following choices

3. Greedy Algorithms
    * Optimization problems
    * Heuristic
    * Short-sighted (local, not global, optimum)

4. Backtracking
    a. Constraint satisfaction problems (i.e. combination sum)
    b. Incrementally builds candidates to solutions - abandon candidate (node/subtree) immediately when it is discovered that it cannot be valid
    c. Build candidates on edges (each node has one edge for each possible "choice")
    d. Evaluation of state of solution on nodes
    e. i.e. combination sum using [1,3], target = 2
                ---s=0----
               / (1)  (3) \
              s=1       s=3(STOP)
             /(1)
        s=2 (SOLN & STOP) 

5. Strings
    a. Tries
    b. Suffix Trees (allows us to solve longest common substring in O(n))
    c. Usually combined with another type of problem (i.e. DP, hash table)
    d. Sliding windows

6. Math
    a. Less programming
    b. Equations
    c. Patterns
    d. Unique factorization theorem
        i. All numbers > 1 are either prime or composite
        ii. If a number is composite, then it is the product of prime numbers
        iii. Furthermore, the prime factorization for each composite number is unique
        iv. This also implies that the product of a set of prime numbers is unique

7. Array
    a. Two pointers
    b. Comapare and swap
    c. The INDEX encodes information - it can be used to store/represent information
        i.e. if i in A, then A[i] = i
    d. Sorted arrays heavily imply binary search
    e. Sorting is a common preprocessing step where order is not important
    f. Sort to "group" together common elements
    g. Easy to compare sorted arrays
    h. Sorting introduces order and expectation
    i. Sliding window
    j. Bucket sort

8. Hash table
    a. Commonly used with string and array questions
    b. Fast lookup; good for "checking"
    c. Common preprocessing step

9. Stack/Queue
    a. FIFO
    b. LIFO
    c. Parenthesis matching
    d. Nested structures (i.e mathematical expressions)

10. Divide and Conquer
    a. Uncommon
    b. Recursive in nature (problems with recursive properties)
    c. Divide problem into subproblems -> solve each subproblem recursively -> combine solutions to solve the problem

10. Trees
    a. DFS (stack, recursion-favored)
    b. BFS (queue, iteration-favored)
    c. DFS can become depth aware by keeping an extra variable in the recursion
    d. No cycles
    e. Shortest path -> BFS

11. Graph
    a. Represents things (nodes) and relationships (edges)
    b. DFS/BFS search algorithms
    c. Set required to keep track of visited nodes
    d. Have cycles
    e. Topological Sort
    f. Connected components
        i.e. Friend Circles
    g. One-way vs two-way edges
    h. Adjacent list
        Less space intensive at the cost of slower lookup
        Good for sparse graphs
    i. Adjacency matrix
        Fast lookup at the expense of more space
        Good for dense graphs
    j. Important to model the question properly
        Node values
        Edge weights
    k. Shortest path -> Dijkstra's or BFS
    l. Minimum Spanning Tree
    
12. Heap
    a. Useful for keeping track of the largest/smallest element in a data structure


Strategies:

1. Brute Force
    a. Enumerate all possibilities
    b. Better than nothing
    c. Start with this - can help with finding better solutions

2. Pre-structuring
    a. Pre-arrange data for faster processing
    b. Sorting when order doesn't matter

3. Problem Reduction/Transformation
    a. Transform/reduce the problem to another
    b. i.e. if problem A reduces to B, then the solution to B can be used to solve A
    b. i.e. Decision and optimizaiton problems

4. Input Enhancement
    a. Pre-calculate results for certain inputs or cache partial results, so the actual run is faster
    b. A hash map is a good data structure to cache results
    c. Multiple passes as an alternative to a worse run-time

5. Non-deterministic methods
    a. Las Vegas
        i. Generate possible solutions non-deterministically
        ii. Produces correct answer
        iii. No gurantees in space and time complexity
    b. Monte Carlo
        i. Generate possible solutions non-deterministically
        ii. Has time and space gurantees
        iii. Small probability of giving the wrong answer
        iv. Run longer -> probability of wrong answer reduced
    c. Hill Climbing
        i. Solve (possibly approximately) optimization problems
        ii. Generate candidate solutions that are improvements over the previous candidate

// source: http://i.imgur.com/JbVwvxo.jpg
