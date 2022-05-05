#### S-> O(n) and O(1) without counting the output, T -> O(n^2)
class Solution:
	def spiralMatrix(self, matrix):
		res = []
		left, right = 0, len(matrix[0])
		top, bottom = 0, len(matrix)

		while left < right and top < bottom:
			# add values in top column
			for i in range(left, right):
				res.append(matrix[top][i])
			top += 1

			# add values in right column
			for i in range(top, bottom):
				res.append(matrix[i][right - 1])
			right -= 1

			if not left < right and top < bottom:
				break

			# add values in bottom row
			for i in range(right - 1, left - 1, -1):
				res.append(matrix[bottom - 1][i])
			bottom -= 1

			# add values in left column
			for i in range(bottom - 1, top - 1, -1):
				res.append(matrix[i][left])
			left += 1
		return res


testCase = Solution()
print(testCase.spiralMatrix([[1,2,3],[4,5,6],[7,8,9]]))
