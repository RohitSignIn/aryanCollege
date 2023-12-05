# TC => O()
str= "abcd"
def getSubString(str):
    subStrings = []
    for i in range(0, len(str)):
        temp=""
        for j in range(i, len(str)):
                temp=temp+str[j]
                subStrings.append(temp)
    return subStrings


def checkPalindrome(str):
    i = 0
    j = len(str) - 1

    while(i<j):
        if(str[i]!=str[j]):
            return False
        i+=1
        j-=1
          
    return True


def getBiggestPalindrome(str):
    subStrings = getSubString(str)

    palindrome = ""
    for i in subStrings:
        if(checkPalindrome(i)):
            if(len(palindrome) < len(i)):
                palindrome = i

    return palindrome

print(getBiggestPalindrome("abaaabbaaefg"))