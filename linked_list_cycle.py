#### Optimal solution.
## Fast and slow pointers

class Solution:
	def linkedListCycle(self, head: ListNode):
		slow, fast = head, head

		while fast and fast.next:
			slow = slow.next
			fast = fast.next.next

			if slow == fast:
				return True
		return False

