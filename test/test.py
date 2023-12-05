def checkRotation(s1, s2):
    if(len(s1) != len(s2)):
        return False
    
    isRotation = False
    for i in range(len(s1)):
        if(s1 == s2):
            isRotation = True      
        else:
            s2 = s2[1:] + s2[0]

    return isRotation

s1="abc"
s2="cay"
if(checkRotation(s1, s2)):
    print("Rotation of S1")
else:
    print("Not a rotation of S1")