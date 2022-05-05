##### Not returning anything once its
class Solution:
	def happyNumber(self, n):
		#### SOlution 1
		# visit = set()	# Memory - O(n), Time - O(n)
        
		# while n not in visit:
		# 	visit.add(n)
		# 	n = self.sumOfSquares(n)

		# 	if n == 1:
		# 		return True
		# return False

		#### Solution 2

        # M -> O(1), T -> O(n)  

		slow, fast = n, n

		while n:
			n = self.sumOfSquares(n)
			if n == 1:
				return True
			slow = slow.next
			fast = fast.next.next
			if slow == fast:
				return False
	def sumOfSquares(self, n):
	 	output = 0
	 	while n:
	 		tmp1 = (n % 10)**2
	 		tmp2 = (n // 10)**2
	 		output = tmp1 + tmp2
	 	return output

test_case = Solution()
print(test_case.happyNumber(19))
