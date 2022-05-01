#### SOLUTION 1
# #### TLE
# class Solution:
#     def isAnagram(self, s: str, t: str) -> bool:
#         hashmS = {}
#         hashmT = {}
#         no = 0
#         no_t = 0
        
#         while len(s) == len(t):
#             for _ in s:
#                 n = s.count(_)
#                 no += n 
#                 hashmS[_] = n
#             for i in t:
#                 num = t.count(_)
#                 no_t += num
#                 hashmT[i] = num
#             # while s[_] == t[i]:
#             #     if n == num
#             if hashmS[_] == hashmT[i]:
#                 return True
#         return False

# test_case = Solution()
# print(test_case.isAnagram('rat', 'nagaram'))


#### SOLUTION 2
# #### COUNTER SOLUTION
# from collections import Counter
# class Solution:
#     def isAnagram(self, s: str, t: str) -> bool:
#         return Counter(s) == Counter(t)

# test_case = Solution()
# print(test_case.isAnagram('rat', 'nagaram'))


# ########## SOLUTION 3

# # Space - O(s+t)
# # Time - O(s+t)
# class Solution:
#     def isAnagram(self, s: str, t: str) -> bool:
        
#         if len(s) != len(t):
#             return False
#         hashS, hashT = {}, {}

#         for i in range(len(s)):
#             # hashmS[s[i]] = 0
#             # hashmT[t[i]] = 0
#             hashS[s[i]] = 1 + hashS.get(s[i], 0)
#             hashT[t[i]] = 1 + hashT.get(t[i], 0)
#         for c in hashS:
#             if hashS[c] != hashT.get(c, 0):
#                 return False
#         return True

# test_case = Solution()
# print(test_case.isAnagram('rat', 'nagaram'))


################# SOLUTION 4

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        return sorted(s) == sorted(t)

test_case = Solution()
print(test_case.isAnagram('rat', 'nagaram'))  

