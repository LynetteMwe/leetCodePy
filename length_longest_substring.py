### Without repeating characters
class Solution:
	def without_repeating_xters(self, s):
		charSet = set()
		l = 0
		res = 0

		for r in range(len(s)):
			if s[r] in charSet:
				charSet.remove(s[l])
				l += 1
			charSet.add(s[r])
			res = max(res, r-l+1)
		return res

test_case = Solution()
print(test_case.without_repeating_xters('abcabcbb'))

# class Solution:
#     def lengthOfLongestSubstring(self, s: str) -> int:
#         charS = set()
#         res = 0
#         l = 0
                  
#         for r in range(len(s)):
#             while s[r] in charS:
#                 charS.remove(s[l])
#                 l += 1
#             charS.add(s[r])
#             res = max(res, r-l+1)
        
                       
#         return res

# test_case = Solution()
# print(test_case.lengthOfLongestSubstring('abcabcbb'))
#                