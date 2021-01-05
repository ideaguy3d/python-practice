class Node(object):
	def __init__(self, val, left=None, right=None):
		self.val = val
		self.left = left
		self.right = right


class Solution(object):
	def _is_valid_bst_helper(self, n, low, high):
		if not n:
			return True
		val = n.val
		if ((low < val < high) and
				self._is_valid_bst_helper(n.left, low, n.val) and
				self._is_valid_bst_helper(n.right, n.val, high)):
			return True
		return False
	
	def is_valid_bst(self, n):
		return self._is_valid_bst_helper(n, float('-inf'), float('inf'))


node = Node(5)
node.left = Node(4)
node.right = Node(7)
# node.right.left = Node(2)
print(Solution().is_valid_bst(node))
