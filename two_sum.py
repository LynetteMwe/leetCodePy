# #########BRUTE FORCE
# class Solution:
# 	def two_sum(self,nums, targ):
		
# 		for i in range(0, len(nums)):
# 			for j in range(i+1, len(nums)):
# 				if nums[i] + nums[j] == targ:
# 					return (i,j)

# 		return []



# sample = [1, 4, 3, 2]
# array = [1, 5, 7]
# array2 = [3,2,4]
# array3 = [8, 14]

# given_nums=[2,7,11,15]

# test_case = Solution()

# print(test_case.two_sum(sample, 4))
# print(test_case.two_sum(array, 6))
# print(test_case.two_sum(array2, 6))
# print(test_case.two_sum(array3, 6))

# print(test_case.two_sum(given_nums,9))


# Time = O(n^2)
# Space = O()

#########OPTIMIZED
class Solution:
	def two_sum(self,nums, targ):
		adict = {}	# val:index
		for i, n in enumerate(nums):
			diff = targ - n
			if diff in adict:
				return (adict[diff],i)

			adict[n] = i
		return []

sample = [1, 4, 3, 2]
array = [1, 5, 7]
array2 = [3, 2, 4]
given_nums=[2, 7, 11, 15]
array3 = [8, 14]

test_case = Solution()

print(test_case.two_sum(sample, 4))
print(test_case.two_sum(array, 6))
print(test_case.two_sum(array2, 6))
print(test_case.two_sum(array3, 6))

print(test_case.two_sum(given_nums,9))

# Time = O(n)
# Space = O(n)

