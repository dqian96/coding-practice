# Problem: Lego Blocks

"""

You are given four types of lego blocks: 1 x 1, 2 x 1, 3 x 1, 4 x 1 (x, y).
These lego blocks are horizontal, so they cannot be placed vertically, for example:
 _
|_|
 _ _
|_ _|

etc.

Using an infinite number of these blocks, you want to build a wall of
M X N, such that there are no holes in the wall and the wall must be structurally connected.
This means there is no vertical in the wall that would allow the wall to be seperated in two
without cutting at least one block.

Find the total number of these walls that can be built.

Input:

T (number of test cases)
N M (height and width of the wall to be built, or y, x)
...
...
...

Output:
Output the total number of walls that can be built for each test case.
Modulo the total number by 1,000,000,007.

1 <= T <= 100
1 <= N, M <= 1000

Solution:

Use DP based on the following equations:

#walls_with_no_seams_m_n = #total_walls_m_n - #walls_with_seams_m_n

#total_walls = #ways_to_layer_m^n

#ways_to_layer_m = #ways_to_layer_m-1 + #ways_to_layer_m-2 + #ways_to_layer_m-3 + #ways_to_layer_m-4

Based on the idea that the first block in the layer is either a 1-block, 2-block, 3-block, or 4-block,
and so, we just sum the # ways to layer the rest after the first block (recurrence)

#walls_with_seams_m_n = sum i from 1 to m-1 (#walls_with_no_seams_i_n * #total_walls_m-i_n)

Based on the idea that in a wall with seams, the first seam can either be after the first unit,
second unit,...,m-1 unit. If the first seam is at i, then the "first" ixn wall will have no seams,
and the "second" m-ixn wall can have or not have seams. Multiply the two by each other to get
the total number of walls with seams if the first seam is at i. Then sum all of the possible
seam locations up to get the total number of mxn walls with seams.

The solution implemented here is correct...but is not time nor space efficient.
Instead of using recursion + memoization, it would be a lot more efficient to
use DP tables.

"""

from sys import stdin
from collections import defaultdict

def calc_num_walls_with_seams(x, y, no_seams_mem, with_seams_mem, layers_mem):
    if x == 1:
        # base case...stack of 1's no seam
        return 0
    if (x, y) in with_seams_mem:
        return with_seams_mem[(x, y)]
    
    s = 0
    for first_seam in range(1, x):
        s += calc_num_walls_no_seams(first_seam, y, no_seams_mem, with_seams_mem, layers_mem) * calc_num_layers(x - first_seam, layers_mem) ** y
    
    with_seams_mem[(x, y)] = s
    return s

def calc_num_layers(x, mem):
    # calculate ways to build layer
    if x not in mem:
        # never before seen
        s = 0
        for i in range(1, 4 + 1):
            s += calc_num_layers(x - i, mem)  # calc number of ways to build rest of layer minus first block
        mem[x] = s
    return mem[x]
    
def calc_num_walls_no_seams(x, y, no_seams_mem, with_seams_mem, layers_mem):
    if x == 1:
        # base case...stack of 1's
        return 1
    if (x, y) in no_seams_mem:
        return no_seams_mem[(x, y)]
    num_total_walls = calc_num_layers(x, layers_mem) ** y
    num_walls_with_seams = calc_num_walls_with_seams(x, y, no_seams_mem, with_seams_mem, layers_mem)

    no_seams_mem[(x, y)] = num_total_walls - num_walls_with_seams
    return no_seams_mem[(x, y)]
    
def main():
    num_walls_no_seams_mem = defaultdict(tuple)         # (x, y) -> #walls
    num_walls_with_seams_mem = defaultdict(tuple)       # (x, y) -> #wall
    num_layers_mem = defaultdict(int)                   #  x -> #layers of length x
    num_layers_mem[1] = 1
    num_layers_mem[2] = 2
    num_layers_mem[3] = 4
    num_layers_mem[4] = 8

    num_cases = int(stdin.readline().strip('\n'))
    for i in range(num_cases):
        tokenizied_case = stdin.readline().strip('\n').split()
        y = int(tokenizied_case[0])
        x = int(tokenizied_case[1])
        res = calc_num_walls_no_seams(x, y, num_walls_no_seams_mem, num_walls_with_seams_mem, num_layers_mem) % 1000000007
        print(res)
        
main()
