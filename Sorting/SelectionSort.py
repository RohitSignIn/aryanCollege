def selectionSort(a, size):
    for i in range(size):
        min_indx = i
        for j in range(i+1, size):
            if a[j] < a[min_indx]:
                min_indx = j

        a[i], a[min_indx] = a[min_indx], a[i]
    return a

a = [2,3,4,1,2,4]
print(selectionSort(a, len(a)))