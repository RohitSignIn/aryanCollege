def insertionSort(a, size):
    for i in range(1, size):
        key = a[i]
        j = i-1
        while(j >= 0 and a[j] > key):
            a[j+1] = a[j]
            j-=1
        
        a[j+1] = key

    return a
    
a = [2,48,1,1,2,0,4,2,0]
print(insertionSort(a, len(a)))