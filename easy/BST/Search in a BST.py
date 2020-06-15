# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
def searchBST(self, root: TreeNode, val: int) -> TreeNode:
    # Base case 1
    # if we reach the end of a path, then the target doesn't exist
    if not root:
        return None

    # Base case 2
    # if the current node value matches our target, we simply return it
    if root.val == val:
        return root
        
    # Recursive cases 1 and 2
    # if the value is less than the current node we go left, otherwise we go right
    return self.searchBST(root.left, val) if val < root.val else self.searchBST(root.right, val)