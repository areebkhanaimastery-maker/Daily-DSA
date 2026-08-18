# You are given an array of integers nums and an integer target, return indices of the two numbers such that 
# they add up to target.
# You may assume that each input would have exactly one solution, and you may not use the same element twice.
#  You can return the answer in any order.

# ==============================Solution using Brute Force====================================

def twoSum(nums,target):
    for i in range(len(nums)):
        for j in range(i+1 , len(nums)):
            if target == nums[i] + nums[j]:
                return[i , j]

a = [3,5,8,11,15,17,19]
b = 13



# ======================================The one-pass hash map idea======================================

for i , j in enumerate(a):
    print(i , j)