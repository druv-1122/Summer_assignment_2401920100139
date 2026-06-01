# Best Time to Buy and Sell Stock

## Approach: Brute Force

For each day, consider it as the buying day and check all future days as possible selling days. Calculate the profit for every buy-sell pair and keep track of the maximum profit.

### Algorithm
1. Iterate through each day as the buying day.
2. For every buying day, check all subsequent days as selling days.
3. Calculate profit = selling price - buying price.
4. Update the maximum profit if a larger profit is found.
5. Return the maximum profit.

### Complexity Analysis
- Time Complexity: O(n²)
- Space Complexity: O(1)

### Python Code
```python
class Solution:
    def maxProfit(self, prices):
        n = len(prices)
        max_profit = 0

        for i in range(n):
            for j in range(i + 1, n):
                max_profit = max(max_profit, prices[j] - prices[i])

        return max_profit
```
