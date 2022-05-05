'''
list1 = [1,2,3]
list2 = [1,2,4,7,8]
-> [1,1,2,2,3,4,7,8]
'''
class Solution:
	def mergeTwoSortedLists(self, list1, list2):
		dummy = ListNode()
		tail = dummy

		while list1 and list2:
			if list1.val < list2.val:
				tail.next = list1.val
				list1 = list1.next
			else:
				tail.next = list2.val
				list2 = list2.next


		if list1:
			tail.next = list1
		if list2:
			tail.next = list2

		return dummy.next

testCase = Solution()
print(testCase.mergeTwoSortedLists([1,2,3], [1,2,4,7,8]))




