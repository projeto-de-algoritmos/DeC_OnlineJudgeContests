#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    TreeNode* sortedArrayToBST(vector<int>& nums)
    {
        return createTree(nums, 0, nums.size() - 1);
    }

    TreeNode* createTree(vector<int>& nums, int left, int right)
    {
        if (left > right) return nullptr;
        int median = (right + left) / 2;
        TreeNode *root =  new TreeNode(nums[median]);

        root->left = createTree(nums, left, median - 1);
        root->right = createTree(nums, median + 1, right);

        return root;
    }
};