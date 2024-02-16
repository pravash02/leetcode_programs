from typing import Optional, List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        q = []
        ans = []

        if root:
            q.append(root)

        while q:
            qlen = len(q)
            row_val = 0
            for _ in range(qlen):
                cur = q.pop(0)
                row_val += cur.val
                if cur.left:
                    q.append(cur.left)
                if cur.right:
                    q.append(cur.right)

            ans.append(row_val/qlen)
        return ans


root = [3, 9, 20, None, None, 15, 7]
root_obj = TreeNode()
root_obj.val = TreeNode(3)
root_obj.val.left = TreeNode(9)
root_obj.val.right = TreeNode(20)
root_obj.val.right.left = TreeNode(15)
root_obj.val.right.right = TreeNode(7)

view = Solution()
print(view.averageOfLevels(root=root_obj.val))
