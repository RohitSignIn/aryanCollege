s1="abc"
s2="def"
result="efabcd"
t=s1+s2
k=0
print(t)
if len(t)==len(result):
    while(k<len(t)):
        c=0
        for j in range(0,len(t)):
            if t[k]==result[j]:
                c+=1
        if c!=1:
            break
    if(i==len(t)):
       print("right")
else:
    print("not right")