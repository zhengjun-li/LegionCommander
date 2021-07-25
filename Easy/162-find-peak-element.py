'''
O(N)
However, question wanted O(logN) solution. Idk how to get that yet
'''
class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 0
        elif nums[1] < nums[0]:
            return 0
        else:
            for i in range(len(nums) - 1):
                if nums[i] > nums[i+1]:
                    return i
            return len(nums) - 1
         
'''
O(NlogN)
Uses binary search to find the peak. At index mid, peak will either be left, mid, or right.
So we can use binary search to find it.
'''
class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        high = len(nums) - 1
        low = 0  
        while high != low:
            mid = int((high - low) / 2 + low)
            print(f'{low}, {mid}, {high}')
            if nums[mid] < nums[mid+1]:
                # peak on right
                low = mid + 1
            elif mid == 0:
                #edge case handler
                return 0
            elif nums[mid-1] > nums[mid]:
                # peak on left
                high = mid - 1
            else:
                # at peak
                return mid
        return low #when low == high, it is peak, simply return
        