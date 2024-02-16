from typing import Optional, List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def rightSideView(self, root: Optional[TreeNode]):
        ans = []
        q = []
        if root:
            q.append(root)

        while q:
            for _ in range(len(q)):
                cur = q.pop(0)
                if cur.left:
                    q.append(cur.left)
                if cur.right:
                    q.append(cur.right)

            ans.append(cur.val)
        return ans


root = [1, 2, 3, None, 5, None, 4]
root_obj = TreeNode()
# root_obj.val = TreeNode(1)
# root_obj.val.left = TreeNode(2)
# root_obj.val.right = TreeNode(3)
# root_obj.val.left.right = TreeNode(5)
# root_obj.val.right.right = TreeNode(4)

view = Solution()
print(view.rightSideView(root=root_obj.val))
