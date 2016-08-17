#Given a random list of integers e.g. [9, 95, 99, 23, 4] return the concatenation of all the elements that is the largest possible number

# SOLUTION:

# Method: Sort the list of integers using a custom comparision function. Iterate
# through the sorted list and concatenate the integers in-order for the final solution.
# To compare integers a and b, we check which order of concatenation results
# in a larger numerical value. For example, if a = 478 and b = 47, then
# concat(a, b) = 47847, concat(b,a) = 47478. Thus, a < b ( a should
# be placed before b) in the sorted list. Using this comparision function,
# all the values in the list will be placed in an order that maxmizes
# the concatenation value. 

# This is an O(knlogn + kn) = O(knlogn) solution, where n is the
# length of the integer list and k is the average number length (for string conversions).

# comparision function
def greater(a, b):
    stringA = str(a)
    stringB = str(b)
    if int(stringA + stringB) > int(stringB + stringA):
        return -1
    return 1

# concatenate the integers in the sorted list and return it
def largestPermutation(integers):
    integers = sorted(integers, cmp=greater)
    finalNum = ""
    for num in integers:
        finalNum += str(num)
    return finalNum

# test
def main():
    integers = [9, 95, 99, 23, 4]
    print(largestPermutation(integers))


if __name__ == "__main__":
    main()
    
  
    
    
    