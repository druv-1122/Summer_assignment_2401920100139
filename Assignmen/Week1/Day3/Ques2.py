class Solution:
    def sortedSquares(self, nums):
        n = len(nums)
        result = [0] * n

        left, right = 0, n - 1
        pos = n - 1
