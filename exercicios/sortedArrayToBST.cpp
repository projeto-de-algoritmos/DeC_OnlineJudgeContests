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
        // Define a condição de parada como o fim do vetor
        if (left > right) return nullptr;
        // Calcula a mediana
        int median = (right + left) / 2;
        // Define a mediana como a raiz da arvore atual
        TreeNode *root = new TreeNode(nums[median]);

        // Chama a funcao recursivamente para criar os filhos esquerdo e direito
        root->left = createTree(nums, left, median - 1);
        root->right = createTree(nums, median + 1, right);

        // Por fim, retorna a raiz
        return root;
    }
};