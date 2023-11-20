# vector = [-2,1,-3,4,-1,2,1,-5,4]
vector = [-2,1,-3,4,-1,2,1,-5,4]

def mergeAndCount(a, b):
    aux = []
    pA, pB = 0, 0
    while pA < len(a) and pB < len(b):
        if a[pA] < b[pB]:
            aux.append(a[pA])
            pA += 1
        else:
            aux.append(b[pB])
            pB += 1
    while pA < len(a):
        aux.append(a[pA])
        pA += 1
    while pB < len(b):
        aux.append(b[pB])
        pB +=1
    return sum(aux), aux


def mergesort(nums):
    print(nums)
    if len(nums) == 0: return 0, []
    if len(nums) == 1: return nums[0], nums
    middle = len(nums)//2

    sumL, left = mergesort(nums[:middle])
    sumR, right = mergesort(nums[middle:])
    sumRe, result = mergeAndCount(left, right)
    return max(sumL, sumR, sumRe), result

print(mergesort(vector))