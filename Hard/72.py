"""
runtime too long
"""

class Solution(object):
    table = {}
    def minDistance(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        minTable = []
        if word1 == word2:
            return 0
        elif word1 == "":
            return len(word2)
        elif word2 == "":
            return len(word1)
        elif len(word1) == 1 and len(word2) == 1:
            return 1
        else:
            bestCount = self.table.get((word1, word2))
            print(bestCount)
            if bestCount == None:
                for i in range(0, len(word1)):
                    for j in range(0, len(word2)):
                        left = self.table.get((word1[:i], word2[:j]))
                        if left == None:
                            left = self.minDistance(word1[:i], word2[:j])
                        
                        mid = self.table.get((word1[i], word2[j]))
                        if mid == None:
                            mid = self.minDistance(word1[i], word2[j])

                        right = self.table.get((word1[i+1:], word2[j+1:]))
                        if right == None:
                            right = self.minDistance(word1[i+1:], word2[j+1:])
                        minTable.append(left + mid + right)
                bestCount = min(minTable)
                self.table[(word1, word2)] = bestCount
                return bestCount
            else:
                return bestCount

input()
soemthing = Solution()
num = soemthing.minDistance("horsehorse", "ros")
print(num)

