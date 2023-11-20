# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        if not nums: return None
        middle = len(nums)//2
        return TreeNode(
            val=nums[middle],
            left=self.sortedArrayToBST(nums[:middle]),
            right=self.sortedArrayToBST(nums[middle + 1:])
        )
