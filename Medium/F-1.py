def getBetweenSteps(n):
    x = math.floor(n / 2)
    sum = x*(x+1)
    if n % 2 != 0:
        sum += x + 1
    return sum

def getEdgeSteps(n):
    return n(n+1)/2

testCases = []
t = sys.stdin.readline()
for l in range(t):
    dist = 0
    n = sys.stdin.readline()
    s = sys.stdin.readline()
    i = 0
    while i < len(s):
        j = i
        while s[i] != '1' or i != len(s):
            i += 1
        if j == 0:
            # edge case for 0..1
            if i == 0:
                breaks
            dist += getEdgeSteps(i - j + 1)
        elif i == len(s): # ^v result for both if statements do same thing, come back to this
            # edge case for 10..
            dist += getEdgeSteps(i - j + 1)
        else:
            # normal case for 10..01
            dist += getBetweenSteps(i - j)
    print(f'Case #{l+1}: {dist}')
