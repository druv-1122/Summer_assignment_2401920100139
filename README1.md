# Summer_Assignment_2401920100139

## LeetCode Solutions

### 1. Two Sum

**Problem:** Two Sum

**Approach:** Brute Force

**Time Complexity:** O(n²)

**Space Complexity:** O(1)

```python
class Solution:
    def twoSum(self, nums, target):
        n = len(nums)

        for i in range(n):
            for j in range(i + 1, n):
                if nums[i] + nums[j] == target:
                    return [i, j]
