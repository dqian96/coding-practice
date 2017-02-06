def preferEachOther(prefListMen, prefListWomen, possibleInstability, manCurrentMatch, womanCurrentMatch):
    man = possibleInstability[0]
    woman = possibleInstability[1]

    manPrefs = prefListMen[man]
    womanPrefs = prefListWomen[woman]

    if manPrefs.index(woman) < manPrefs.index(manCurrentMatch):
        if womanPrefs.index(man) < womanPrefs.index(womanCurrentMatch):
            return True

    return False


def findInstabilities(matching, numPeople, prefListMen, prefListWomen):
    instabilities = []
    for man in range(0, numPeople):
        for woman in range(0, numPeople):
            possibleInstability = (man, woman)

            for match in matching:
                if match[0] == man:
                    manCurrentMatch = match[1]
                if match[1] == woman:
                    womanCurrentMatch = match[0]

            if manCurrentMatch == woman:
                continue

            if preferEachOther(prefListMen, prefListWomen, possibleInstability, manCurrentMatch, womanCurrentMatch):
                instabilities.append((man, woman))

    print instabilities


numPeople = 3
prefListMen = [[0, 1, 2], [0, 2, 1], [2, 1, 0]]
prefListWomen = [[1, 0, 2], [1, 2, 0], [0, 1, 2]]
matching = [(0, 1), (1, 0), (2, 2)]

findInstabilities(matching, numPeople, prefListMen, prefListWomen)
