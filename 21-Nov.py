# 1. SUM of all Entered Numbers
# sum = 0
# for i in [2,3,4,1,3,4,5]:
#     sum = sum + i

# print(sum)

# 2. Count of Even No & Count of Odd Numbers
# evenCnt = 0
# oddCnt = 0

# for i in [2,3,4,1,3,4,5]:
#     if(i % 2 == 0):
#         evenCnt = evenCnt+1
#     else: 
#         oddCnt = oddCnt+1

# print(evenCnt)
# print(oddCnt)

# 3. First Even No || First Odd No
# for i in [1,3,4,1,3,4,5]:
#     if(i%2 == 0):
#         print(i)
#         break

# 8. Display First Even without skipping the rest
# gotEven = False
# for i in [1,3,4,1,3,4,5]:
#     if(i%2 == 0):
#         gotEven = True
#     if(gotEven):
#         print(i)


# 4. Maximum Number
# a = [1,2,3,4,5,6]
# max = a[0]
# b = len(a)

# for i in range(1, b, 1):
#     if(max < a[i]):
#         max = a[i]

# print(max)

# 6. Count +ve, -ve and zeros
# 0 = negative count
# 1 = zeros count
# 2 = positive count
# a = [0, 0, 0]
# for i in [-1,-1,-1,-1,-1,0,1,2,3,4,0,0,0]:
#     if(i == 0):
#         a[1] = a[1]+1
#     elif(i < 0):
#         a[0] = a[0]+1
#     if(i > 0):
#         a[2] = a[2]+1

# print(a[0], a[1], a[2])


# 7. Display sum of all two digits and three digits Number
a = 9978965
b = str(a)
sum = 0
for i in range(0, len(b), 1):
    sum = int(b[i]) + sum
print(sum)




