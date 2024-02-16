from typing import Optional, List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        ans = []
        q = []
        count = 0

        if root:
            q.append(root)

        while q:
            temp = []
            qlen = len(q)

            for _ in range(qlen):
                cur = q.pop(0)

                if cur.left:
                    q.append(cur.left)
                if cur.right:
                    q.append(cur.right)
                temp.append(cur.val)

            count += 1

            if count % 2 != 0:
                ans.append(temp)
            else:
                ans.append(temp[::-1])

        return ans


root = [3, 9, 20, None, None, 15, 7]
root_obj = TreeNode()
root_obj.val = TreeNode(3)
root_obj.val.left = TreeNode(9)
root_obj.val.right = TreeNode(20)
root_obj.val.right.left = TreeNode(15)
root_obj.val.right.right = TreeNode(7)

view = Solution()
print(view.zigzagLevelOrder(root=root_obj.val))
