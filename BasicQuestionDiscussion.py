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
# a = 9978965
# b = str(a)
# sum = 0
# for i in range(0, len(b), 1):
#     sum = int(b[i]) + sum
# print(sum)


# 11. Display Power (Exponent)
# n=int(input("enter"))
# n1=int(input("power="))
# p=1
# while n1 > 0:
#     p=p*n
#     n1=n1-1
# print(p)


# 12. Factorial (Using loop and recurssion)
# def factorial(n):
#     if(n == 1):
#         return n
    
#     return factorial(n-1) * n

# print(factorial(5))



# 17. Armstrong Number
# Power Function
# def power(dig, n):
#     return int(dig) ** n

# no = 153
# noStr = str(no)
# totalDigits = len(str(no))

# armstrong = 0
# for i in range((totalDigits)):
#     armstrong = power(noStr[i], totalDigits) + armstrong

# if(armstrong == no):
#     print("Valid armstrong")
# else:
#     print("Invalid armstrong")


# Fibonacci Series
# def fibonacci(n):
#     if(n == 0 or n == 1):
#         return n
#     return fibonacci(n-1) + fibonacci(n-2)

# print(fibonacci(4))

# LCM
# n1 = 2
# n2 = 7


# def getGreater(n1, n2):
#     if(n1 > n2):
#         return n1
#     else:
#         return n2
    
# def getSmaller(n1, n2):
#     if(n1 < n2):
#         return n1
#     else:
#         return n2

# greater = getGreater(n1,n2)
# small = getSmaller(n1,n2)

# n2 = greater

# while True:
#     if(greater % small == 0):
#         print(greater)
#         break
#     else:
#         greater = greater + n2

# HCF || GCD


