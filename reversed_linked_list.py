'''
Iteratively. Optimal solution.
1->2->3->4	to	4->3->2->1
'''
# class Solution:
# 	def reversedLinkedList(self, head: ListNode):
# 		prev, curr = None, head

# 		while curr:
# 			tmp = curr.next
# 			curr.next = prev
# 			prev = curr
# 			curr = tmp

# 		return prev

# testCase = Solution()
# print(testCase.reversedLinkedList([1,2,3,4])) 

'''
Recursively
'''

class Solution:
	def reversedLinkedList(self, head: ListNode):
		if not head:
			return None

		newHead = head
		if head.next:
			newHead = self.reversedLinkedList(head.next)
			head.next.next = head

		head.next = None

		return newHead


testCase = Solution()
print(testCase.reversedLinkedList([1,2,3,4])) 