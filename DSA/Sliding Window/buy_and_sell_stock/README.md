**Problem Name**: Best Time to Buy and Sell Stock

**Source**: https://leetcode.com/problems/best-time-to-buy-and-sell-stock/description/

**Difficulty**: Easy

**Pattern**: Sliding Window

**Problem Type**: Array


**Core Idea (2–3 lines)**:
Update the min price on the fly, along with calculating the max profit

**Approach**:

1. Store the 0th element from prices as min price of the stock
2. For each element starting from 1st index, check if it smaller than the min price
3. If yes, update the min_price with current value and move to the next iteration
4. If not, calculate the profit and update the max profit

**Time Complexity**: O(n)
**Space Complexity**: O(1)

**Edge Cases**:
- Decrementing price
- Lowest value in the middle of the array

**Common Mistakes**:
- Didn't do any mistake, however make sure that you skip the iteration after updating the min price

**Trigger Keywords (for interviews)**:
min_price, update profit, skip iteration

**Revision Hint (1 line)**:
Check for the min_price in the stock, keep on updating the max_profit.