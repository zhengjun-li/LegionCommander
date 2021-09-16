import math

class Solution:
    mem = dict()
    def coinChange(self, coins, amount: int) -> int:
        self.mem = { }
        coins.sort(reverse=True)
        returnVal = self.coinsNeeded(coins, amount, math.inf, 0)
        if returnVal == math.inf:
            return -1
        else:
            return returnVal

    def coinsNeeded(self, coins, amount, knownMin, currentDepth):
        if amount == 17:
            print('wat')

        #print(f'testing amount {amount}')
        #break cases
        if amount in self.mem:
            return self.mem[amount]
        elif amount == 0:
            return 0
        elif currentDepth >= knownMin:
            return currentDepth
        #else calculate new value, store it and return it

        minCount = math.inf
        minKey = None

        for coin in coins:
            if coin > amount:
                continue
            if coin == amount:
                self.mem[amount] = 1
                return 1
            if amount - coin in self.mem:
                returnVal = self.mem[amount - coin]
                #print(f'used for {amount - coin}')
            else:
                returnVal = self.coinsNeeded(coins, amount - coin, minCount, currentDepth + 1)
            if returnVal < minCount:
                minCount = returnVal
                minKey = amount - coin
            if returnVal == 1:
                break
                
        self.mem[minKey] = minCount + 1
        return minCount + 1


coins = [2,5,10,1]
amount = 27
a = Solution()
print(a.coinChange(coins, amount))
