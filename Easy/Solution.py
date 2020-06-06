from typing import List


def twoSum(nums: List[int], target: int) -> List[int]:
        negList = []
        posList = []
        for i in range(len(nums) - 1):
            number = target - nums[i]
            print(number)
            if number < 0:
                if number > len(negList):
                    negList.extend([0] * (number - len(negList) + 1))
                negList[number] = 1
            elif number >= 0:
                if number > len(negList):
                    posList.extend([0] * (number - len(posList) + 1))
                posList[number] = 1
        print(negList)
        print(posList)

test = [5, 6, 9, 3, 6,2 , 6]
twoSum(test, 6)






