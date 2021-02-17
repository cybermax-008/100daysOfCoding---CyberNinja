# CCC 2016
# Problem J3: Hidden Palindrome

def hiddenPalindrome(s):
    n = len(s)

    if n==1:
        return s
    max_len =1
    #banana
    for i in range(n-1):
        for j in range(i+1,n):
            subStr = s[i:j+1]
            # print("The substring is:",subStr)
            if len(subStr)%2==0:
                # print(subStr[:len(subStr)//2],subStr[len(subStr)//2:][::-1])
                if subStr[:len(subStr)//2] == subStr[len(subStr)//2:][::-1]:
                    if len(subStr)>max_len:
                        max_len = len(subStr)
            else:
                # print(subStr[:len(subStr)//2+1],subStr[len(subStr)//2:][::-1])
                if subStr[:len(subStr)//2+1] == subStr[len(subStr)//2:][::-1]:
                    if len(subStr)>max_len:
                        max_len = len(subStr)  
    return max_len

print(hiddenPalindrome('abracadabra'))