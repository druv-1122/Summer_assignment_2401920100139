# Remove Duplicates from Sorted Array

**LeetCode Problem:** Remove Duplicates from Sorted Array

## Approach
- Traverse the sorted array.
- If two adjacent elements are equal, remove the duplicate using `pop()`.
- Otherwise, move to the next index.

## Solution

```python
class Solution:
    def removeDuplicates(self, nums):
        i = 0
        while i < len(nums) - 1:
            if nums[i] == nums[i + 1]:
                nums.pop(i)
            else:
                i += 1
        return len(nums)
```

## Complexity
- Time: O(n²)
- Space: O(1)
