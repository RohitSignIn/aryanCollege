s1="abb"
s2="def"
result="efabbd"
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
        k+=1
    if(k==len(t)):
       print("right")
else:
    print("not right")