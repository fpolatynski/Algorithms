class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def balanceBST(self, root: TreeNode) -> TreeNode:
        sorted_tree = self.inorder_traversal(root)
        return self.create_tree(sorted_tree)


    def inorder_traversal(self, root: TreeNode):
        if root is None:
            return []
        else:
            return self.inorder_traversal(root.left) + [root.val] + self.inorder_traversal(root.right)
            
    def create_tree(self, sorted_tree: List):
        n = len(sorted_tree)
        mid = n // 2
        if n == 0:
            return None
        else:
            return TreeNode(sorted_tree[mid], self.create_tree(sorted_tree[:mid]), self.create_tree(sorted_tree[mid+1:]))
    