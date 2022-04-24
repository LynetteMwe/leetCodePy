# ****************
def isPalindrome(s):
    st =''
    for i in s:
        st = i + st
    return st.lower() == s.lower()	# makes the implementation case insensitive


x = isPalindrome('anna,')
print(x)

# # Test cases
# 1. Lyn
# 2. 2222
# 3. Elle
# 4. anna,
# Time Complexity is O(n)
# Space Complexity is O(n)



# # ****************
# def reverse(s):
#     return s[::-1]

# y = reverse('Lyn')
# print(y)

# Time Complexity is O()
# Space Complexity is O(1)
