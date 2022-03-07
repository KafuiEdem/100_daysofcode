def getLongestPath(arr):
    if type(arr) == bool:
        return False
    if type(arr) == int:
        return [1, [arr]]
    if len(arr) == 0:
        return [0, arr]
    
    longest = 0
    longestPath = []
    for node in arr:
        if type(node) == bool:
            return False
        if type(node) == int:
            return [1, [node]]
        score = node[0]
        path = node[1]
        tmp = getLongestPath(path)
        if tmp != False:
            tmpLength = tmp[0]
            tmpPath = tmp[1]
            if tmpLength > longest:
                longest = tmpLength
                longestPath = [score] + tmpPath
            if tmpLength == longest:
                val1 = sum(longestPath)
                val2  = sum([score] + tmpPath)
                if val2 > val1:
                    longestPath = [score] + tmpPath

    if longest == 0:
        return False
    return [longest + 1, longestPath]


#example imput
tree = [[7, [3, [2]], [2, False]], [3, [7, False], 
[3, [3, [2]], [2, False]], [2, [3, False], [2, [7]]]], 
[2, [7, False], [3, [3, False], [2, False]], [2, [7, False], 
[3, False], [2, [2, False]]]]]

print(getLongestPath(tree))
