## Recursion

class Solution():
	def theatreRow(self,n):
		if n == 1:
			return 1
		return self.theatreRow(n-1)+1

x = Solution()
y = x.theatreRow(15)
print(y)

