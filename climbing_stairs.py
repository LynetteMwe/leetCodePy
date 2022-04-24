# Understand fibonacci

# ## Top-down with time-limit exceeded. TLE. *******DONE******
# class Solution1:
#     def climbStairs1(self, n):
#         if n == 1:
#             return 1
#         if n == 2:
#             return 2
#         return self.climbStairs1(n-1) + self.climbStairs1(n-2)
# y = Solution1()
# z = y.climbStairs1(3)
# print(z)
# Time = O(2^n)

### Top-down (Memoization) -- Dict

# class Solution2:
#     def __init__(self):
#         self.dic = {1:1, 2:2}
    
#     def climbStairs(self, n):
#         if n not in self.dic:
#             self.dic[n] = self.climbStairs(n-1) + self.climbStairs(n-2)
#         return self.dic[n]

# first = Solution2()
# x = first.climbStairs(3)
# print(x)

# ### Bottom-up with O(n) space ******************DONE
# class Solution3:
#     def climbStairs(self, n):
#         if n == 1:
#             return 1
#         result = [0 for i in range(n)]
#         result[0], result[1] = 1,2
#         for i in range(2, n):
#             result[i] = result[i-1] + result[i-2]
#         return result[-1]

# x = Solution3()
# y = x.climbStairs(3)
# print(y)

# Time - O(n)


# ###### Bottom up with constant space*************DONE
class Solution4:
    def climbStairs(self, n):
        if n == 1:
            return 1
        a, b = 1, 2

        for i in range(2,n):
            c = a+b
            a = b
            b = c
        return b

x = Solution4()
y = x.climbStairs(3)
print(y)

# Time complexity - O(n)
# Space = O(1)