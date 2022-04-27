# *****************************CONTAINS DUPLICATES I. SOLVED***************************
# Returns  true when the numbers in the list have duplicates and false otherwise

# ## BRUTE FORCE
# # Time - O(n^2)
# # Space - O(1)
# class Solution:
#     def containsDuplicate(self, nums):
#         for i in range(len(nums)):
#             for j in range(i+1, len(nums)):
#                 if nums[i] == nums[j]:
#                     return True
                
#         return False
# x = []
# for num in input('Enter your list with values separated by space: ').split():
#     x.append(int(num))

# test = Solution()
# y = test.containsDuplicate(x)
# print(y)


# ########### OPTIMIZED SOLUTION. Using hashsets
# Time- O(n)
# Space - O(n)

# class  Solution:
#     def containsDuplicate(self, nums):
#         hashset = set()

#         for n in nums:
#             if n in hashset:
#                 return True
#             hashset.add(n)
#         return False

# x = []
# for num in input('Enter your list with values separated by space: ').split():
#     x.append(int(num))

# test = Solution()
# y = test.containsDuplicate(x)
# print(y)






# ########### METHOD 3

# class Solution:
#     def containsDuplicate(self, nums):
# #       
#         return len(nums) != len(set(nums))

# x = []

# for n in input('Enter the numbers separated with space: ').split():
#     x.append(int(n))

# test = Solution()
# y = test.containsDuplicate(x)
# print(y)

# Time = O()
# Space = O()
        
# *****************************CONTAINS DUPLICATES II. 
# ### BRUTE FORCE ******** DONE ********

# class Solution:
#     def containsNearbyDuplicate(self, nums, k):
        
#         for i in range(len(nums)):
#             for j in range(i+1, len(nums)):                
#                 if nums[i] == nums[j] and abs(i-j) <= k:
#                     return True
#         return False

# x = Solution()
# print(x.containsNearbyDuplicate([1,2,3,1], 3))

#### OPTIMIZED ******** NOT DONE ********
class Solution:
    def containsDuplicates(self, nums, k):
        adict = {}  # value:index
        for i, n in enumerate(nums):
            if n in adict and abs(i - adict[n])<=k:
                return True
            adict[n] = i
        return False
x = Solution()
print(x.containsDuplicates([1,2,3,4,4], 1))


# *****************************CONTAINS DUPLICATES III. Not SOLVED***************************







