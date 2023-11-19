# vector = [1, 5, 4, 8, 10, 2, 6, 9, 12, 11, 3, 7]
vector = [5,2,6,1]
v_dict = {x:0 for x in vector}
print(v_dict)

def mergeAndCount(a, b):
    aux = []
    counts = 0
    pointerA = 0
    pointerB = 0
    lenA = len(a)
    lenB = len(b)
    while pointerA < lenA and pointerB < lenB:
        print("comparing", a[pointerA], b[pointerB])
        if a[pointerA] < b[pointerB]:
            aux.append(a[pointerA])
            pointerA += 1
        else:
            aux.append(b[pointerB])
            v_dict[a[pointerA]] += 1
            counts += (lenA - pointerA)
            pointerB += 1
    print(v_dict)
    print("pointerA, pointerB = ", pointerA, pointerB)
    while pointerA < lenA:
        print("while1")
        aux.append(a[pointerA])
        pointerA += 1
    while pointerB < lenB:
        print("wwhile2")
        aux.append(b[pointerB])
        pointerB += 1
    return (counts, aux)

def sortAndCount(v):
    n = len(v)
    if n == 1: return (0, v)
    middle = n//2
    a, b = v[:middle], v[middle:]
    ra, a = sortAndCount(a)
    rb, b = sortAndCount(b)
    r, v = mergeAndCount(a, b)
    return (r + ra + rb, v)


print(sortAndCount(vector))
# print(v_dict)