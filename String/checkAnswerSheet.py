a = ["aba", "aya", "bb", "aa", "aa"]

count = 0
for i in range(0, len(a)-1):
    if(a[i][0] == a[i+1][0] and a[i][-1] == a[i+1][-1]):
        count += 1

print(count)