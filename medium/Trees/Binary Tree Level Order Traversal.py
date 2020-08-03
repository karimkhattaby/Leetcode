# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        
        to_visit = deque()
        to_visit.append(root)
        
        res = []
        
        while to_visit:
            temp_queue = deque()
            current_level = []
            while to_visit:
                cnode = to_visit.popleft()
                if not cnode:
                    continue
                current_level.append(cnode.val)
                if cnode.left:
                    temp_queue.append(cnode.left)
                if cnode.right:
                    temp_queue.append(cnode.right)
            to_visit = temp_queue
            res.append(current_level)
        
        return res