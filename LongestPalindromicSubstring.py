class Solution:
	def LongestPalindromicSubstring(self, s):
		res = ''
		resLen = 0

		for i in s:
			# if string has odd number of characters
			l, r = i,i
			while l >= 0 and r < len(nums) and s[l] == s[r]:
				if (r-l+1) > resLen:
					res = s[l:r+1]
					resLen = r-l+1
				l -= 1
				r += 1

			# if string has even number of characters
			l, r = i, i+1
			while l >= 0 and r < len(nums) and s[l] == s[r]:
				if (r-l+1) > resLen:
					res = s[l:r+1]
					resLen = r-l+1
				l -= 1
				r += 1 
			return res

x = Solution()
print(x.LongestPalindromicSubstring('ababd'))