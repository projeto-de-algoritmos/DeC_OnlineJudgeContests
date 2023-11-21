#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    int mergeAndCount(vector<int> &nums, vector<int> &temp, int left, int mid, int right) {
        int i = left, j = mid + 1, k = left;
        int inv_count = 0;

        // Atravessa o array contando as inversoes
        while (i <= mid && j <= right) {
            if ((long long)nums[i] > 2LL * nums[j])
            { 
                inv_count += (mid - i + 1);
                j++;
            } 
            else 
            {
                i++;
            }
        }

        i = left, j = mid + 1, k = left;

       // Enquanto nenhuma das duas metades do vetor acabam
        while (i <= mid && j <= right)
        {
            // Verifica qual valor eh menor e o adiciona no array temporario
            if (nums[i] <= nums[j])
            {
                temp[k++] = nums[i++];
            } 
            else
            {
                temp[k++] = nums[j++];
            }
        }

        // Termina de copiar qualquer uma das partes que ainda nao foram copiadas
        while (i <= mid)
        {
            temp[k++] = nums[i++];
        }

        while (j <= right)
        {
            temp[k++] = nums[j++];
        }
        
        // Copia o vetor temporario de volta para o original
        for (i = left; i <= right; i++)
        {
            nums[i] = temp[i];
        }

        return inv_count;
    }

    int SortAndCount(vector<int>& nums, vector<int>& temp, int left, int right)
    {
        // Define a condição de parada quando o valor de left igualar ou ultrapassar right
        if (right <= left) return 0;

        // Calcula a mediana
        int mid = left + (right - left) / 2;
        int inv_count = 0;

        // Conta as inversoes para as duas metades doa array 
        inv_count += SortAndCount(nums, temp, left, mid);
        inv_count += SortAndCount(nums, temp, mid + 1, right);

        // Conta as inversoes do merge das duas metades
        inv_count += mergeAndCount(nums, temp, left, mid, right);
        return inv_count;
    }

    int reversePairs(vector<int>& nums) {
        vector<int> temp(nums.size());
        return SortAndCount(nums, temp, 0, nums.size() - 1);
    }
};