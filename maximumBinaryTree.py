# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> Optional[TreeNode]:
        if not nums: return None
        middle = nums.index(max(nums))
        return TreeNode(
            val=nums[middle],
            left=self.constructMaximumBinaryTree(nums[:middle]),
            right=self.constructMaximumBinaryTree(nums[middle+1:])
        )