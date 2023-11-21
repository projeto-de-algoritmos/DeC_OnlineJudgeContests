#include <bits/stdc++.h>
using namespace std;

class Solution
{
public:
    double findMedianSortedArrays(vector<int> &nums1, vector<int> &nums2)
    {
        // Define o vetor que recebera o merge e os indices para atravessar os outros vetores
        vector<int> array;
        int i = 0, j = 0;

        // Enquanto nenhum dos dois vetores acabam
        while (i < nums1.size() && j < nums2.size())
        {
            // Verifica qual valor eh menor e o adiciona no array
            if (nums1[i] <= nums2[j])
                array.push_back(nums1[i++]);
            else
                array.push_back(nums2[j++]);
        }

        // Termina de copiar qualquer um dos vetores que ainda nao foi copiado
        while (i < nums1.size())
            array.push_back(nums1[i++]);
        while (j < nums2.size())
            array.push_back(nums2[j++]);

        int totalSize = nums1.size() + nums2.size();

        // Verifica se a soma dos tamanhos dos vetores eh impar ou nao para calcular a mediana apropriadamente
        if (totalSize % 2 == 0)
            return (array[totalSize / 2 - 1] + array[totalSize / 2]) / 2.0;
        else
            return array[totalSize / 2];
    }
};