from typing import Optional, List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        ans = []
        q = []
        if root:
            q.append(root)

        while q:
            temp = []
            qlen = len(q)

            for _ in range(qlen):
                cur = q.pop(0)

                if cur:
                    temp.append(cur.val)
                    q.append(cur.left)
                    q.append(cur.right)

            if temp:
                ans.append(temp)

        return ans


root = [3, 9, 20, None, None, 15, 7]
root_obj = TreeNode()
root_obj.val = TreeNode(3)
root_obj.val.left = TreeNode(9)
root_obj.val.right = TreeNode(20)
root_obj.val.right.left = TreeNode(15)
root_obj.val.right.right = TreeNode(7)

view = Solution()
print(view.levelOrder(root=root_obj.val))
