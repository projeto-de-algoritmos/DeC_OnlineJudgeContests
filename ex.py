# vector = [5,2,6,1]
vector = [1,3,2,3,1]
# vector = [2,4,3,5,1]

def mergeAndCount(a, b):
    print("merging a and b:", a, b)
    aux = []
    counts, pointerA, pointerB = 0, 0, 0
    lenA, lenB = len(a), len(b)
    while pointerA < lenA and pointerB < lenB:
        print(f"comparing a->{a[pointerA]} and b->{b[pointerB]}")
        if a[pointerA] > 2 * b[pointerB] or b[pointerB] > 2 * a[pointerA]: counts += 1
        if a[pointerA] < b[pointerB]:
            aux.append(a[pointerA])
            pointerA += 1
        else:
            aux.append(b[pointerB])
            # counts += (lenA - pointerA)
            pointerB += 1
    while pointerA < lenA:
        aux.append(a[pointerA])
        pointerA += 1
    while pointerB < lenB:
        aux.append(b[pointerB])
        pointerB += 1
    return counts, aux

def sortAndCount(v):
    n = len(v)
    if n == 1: return 0, v
    middle = n//2
    a, b = v[:middle], v[middle:]
    ra, a = sortAndCount(a)
    rb, b = sortAndCount(b)
    r, v = mergeAndCount(a, b)
    return r + ra + rb, v

print(sortAndCount(vector))