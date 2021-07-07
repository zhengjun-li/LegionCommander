class Solution:
    def intToRoman(self, num: int) -> str:
        (m, num) = divmod(num, 1000)
        (d, num) = divmod(num, 500)
        if d == 
        