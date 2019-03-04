from 03_single_link_list import *
class ListNode(object):
	"""docstring for ListNode"""
	def __init__(self, x):
		self.val = x
		self.next = None
		
class Solution(object):
	"""docstring for Solution"""
	def mergetwosorted(self, l1,l2):
		curr =  dummy = ListNode(0)

		while l1 and l2:
			if l1.val < l2.val:
				curr.next = l1
				l1 = l1.next
			else:
				curr.next = l2
				l2 = l2.next
		curr.next = l1 or l2

