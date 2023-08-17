"""
Challenge as a review

Given a list of random numbers (nums) and a "pivot" number (pivot), return a list with three sections. The first contains numbers less than (pivot) in (nums), the second contains the numbers equal to (pivot) in (nums), and the third contains the numbers greater than (pivot) in (nums). 
Example:

pivot([5,1,3,5,9,8,10], 5) -> [1,3,5,5,9,8,10] # We want this.
-> [[1,3], [5,5], [9,8,10]] # We don't want this.

"""
def pivot_func(nums, pivot):
  less_pivot = []
  pivot_list = []
  more_pivot = []
  for num in nums:
    if num < pivot:
      less_pivot.append(num)
    elif num == pivot:
      pivot_list.append(num)
    elif num > pivot:
      more_pivot.append(num)
  # for num in pivot_list:
  #   less_pivot.append(num)
  # for num in more_pivot:
  #   less_pivot.append(num)
  return less_pivot + pivot_list + more_pivot
  
  


"""
for i in range(len(nums)): # indexes


for num in nums: # each number itself; enhanced / for each

"""




# print(pivot_func([5,1,3,5,9,8,10], 5))
"""

Given a positive integer n, find the smallest number of squared integers which sum to n.

For example, given n = 13, return 2 since 13 = 3^2 + 2^2 = 9 + 4.

Given n = 27, return 3 since 27 = 3^2 + 3^2 + 3^2 = 9 + 9 + 9

"""
from math import sqrt, floor
def square_ints(n): 
  num = n
  if n < 1:
    return 0
  nums = []
  while num > 0:
    highest = floor(sqrt(num))
    num = num - highest**2
    nums.append(highest)
  nums2 = []
  num = n
  secHighest = floor(sqrt(num)) - 1
  num = num - secHighest**2
  nums2.append(secHighest)
  while num > 0:
    highest = floor(sqrt(num))
    num = num - highest**2
    nums2.append(highest)
  if len(nums) < len(nums2):
    return len(nums), nums
  return len(nums2), nums2

# secHighest = floor(sqrt(num)) - 1
# num = num - secHighest**2
# secHighest = f(sqrt(secHighest))
# 15 - 3 = 12
# h = f(sqrt(12)) # 3

# highest = 3
# n - 9 = 15
# h = f(sqrt(15)) # 3
# 15 - 3 = 12
# h = f(sqrt(12)) # 3

print(square_ints(76)) # -> 3  (3,3,1), (4,1,1,1)
print(square_ints(29)) # -> 3  [4,2,2]
"""
# sqrt(19) -> 4.3....
# floor(sqrt(19)) -> 4
# floor(sqrt(24)) -> 4
# find the closest number (less than n) that can be square rooted using floor(sqrt(n)) and then subtract that from n 
HOMEWORK: finish this with second closest


n = 19
highest = floor(sqrt(19)) # highest = 4
n - highest^2 = 3
floor(sqrt(3)) = 1
3 - 1 = 2
floor(sqrt(2)) = 1
2 - 1 = 1
floor(sqrt(1)) = 1
1 - 1 = 0
STOP
List: [4,1,1,1]













n = 24
highest = floor(sqrt(24)) # 4
n - h^2 = 8
h = f(sqrt(8)) # 2
8 - 4 = 4
h = f(sqrt(4)) # 2
4 - 4 = 0
STOP 
List: [4,2,2]


highest = 3
n - 9 = 15
h = f(sqrt(15)) # 3
15 - 3 = 12
h = f(sqrt(12)) # 3



"""