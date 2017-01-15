# Problem: Merge sorted arrays
# Merge k sorted arrays into one array in O(nlog(k))

import random

def merge(arrayList):
    if len(arrayList) != 1:
        mergedLeftHalf = merge(arrayList[:(len(arrayList)/2 - 1) + 1])
        mergedRightHalf = merge(arrayList[len(arrayList)/2:])
        l = 0
        r = 0
        m = []
        while l < len(mergedLeftHalf) and r < len(mergedRightHalf):
            if mergedLeftHalf[l] <= mergedRightHalf[r]:
                m.append(mergedLeftHalf[l])
                l += 1
            else:
                m.append(mergedRightHalf[r])
                r += 1
        if l < len(mergedLeftHalf):
            m.extend(mergedLeftHalf[l:])
        elif r < len(mergedRightHalf):
            m.extend(mergedRightHalf[r:])
        return m
    return arrayList[0]

def testMerge():
    k = 2**(random.randint(0, 8))
    arrayList = []
    for i in range(0, k):
        size = random.randint(1, 40)
        arrayList.append(sorted([random.randint(-1000, 1000) for x in range(0, size)]))
    res = merge(arrayList)
    if res == sorted(res):
        return True
    return False

if __name__ == "__main__":
    for i in range(0, 500):
        if testMerge() == False:
            print False
            break
    print True
