"""
Given an array of integers `nums`, define a function that returns the "pivot" index of the array.

The "pivot" index is where the sum of all the numbers on the left of that index is equal to the sum of all the numbers on the right of that index.

If the input array does not have a "pivot" index, then the function should return `-1`. If there are more than one "pivot" indexes, then you should return the left-most "pivot" index.

Example 1:

Input: nums = [1,7,3,6,5,6]
Output: 3
Explanation:
The sum of the numbers to the left of index 3 (1 + 7 + 3 = 11) is equal to the sum of numbers to the right of index 3 (5 + 6 = 11).
Also, 3 is the first index where this occurs.

Example 2:

Input: nums = [1,2,3]
Output: -1
Explanation:
There is no index that satisfies the conditions in the problem statement.
"""
from typing import List

# def pivot_index(nums: List[int]) -> int:
#     # Your code here
            
            
# def pivot_index(nums: List[int]) -> int:
#     inequality = False
#     index = 0
#     sumleft = 0
#     sumright = sum(nums)
#     while(not inequality and index < len(nums)):
#         sumleft += nums[index]
#         sumright -= nums[len(nums) - 1 - index]
#         # print('\nsumright: ', sumright)
#         # print('sumleft', sumleft)
#         inequality = sumleft == sumright
#         # print('inequality', inequality)
#         if inequality:
#             return nums[index]
#         index += 1
#     return -1

def pivot_index(nums):
    # Your code here
    for i in range(i, len(nums) - 1):
        
        if (sum(nums[:i]) == sum(nums[i:])

        return i

print(pivot_index([1,7,3,6,5,6]))
