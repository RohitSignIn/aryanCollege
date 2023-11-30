def bubble(a):
    for i in range(len(a),1,-1):
        for j in range(0,i-1):
            if a[j]>a[j+1]:
                a[j],a[j+1]=a[j+1],a[j]


    return a

a = [2,1,4,8,6,1,4]
print(bubble(a))


# Inplace Sorting - YES
# Stable sorting - YES
# TC = O(nSq)

