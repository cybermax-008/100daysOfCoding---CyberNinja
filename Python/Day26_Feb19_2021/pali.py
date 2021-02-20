
def palindrome(s):
    ordinals = [ord(c) for c in s]
    output = ordinals.copy()
    mid = len(ordinals)//2
    left = 0
    right = len(s)-1

    while(right-left>=0):
        if len(s)%2==0:
            if right==mid:
                if ordinals[left]>ordinals[right]:
                    output[right]=output[left]
                else:
                    output[left]=output[right]  
                if output[mid]>ordinals[mid-1]+1:
                    output[mid]-=1
                    output[mid-1]-=1
            if left ==0:
                output[right]=output[left]
            else:
                if ordinals[left]>ordinals[right]:
                    output[right]=output[left]
                elif 
                else:
                    if ordinals[left]==ordinals[right]==122:
                        output[left]= ord('a')
                        output[right] = ord('a')
                    output[left]=output[right]   

        else:
            if left==mid:
                if output[left]>output[left+1]:
                    output[left]+=1
            if left ==0:
                output[right]=output[left]
            else:
                if ordinals[right]>ordinals[left]:
                    output[right]=output[left]
                else:
                    output[left]=output[right]


        left+=1
        right-=1
    op = "".join([chr(i) for i in output])
    print(op)








s1 = "aazzzzba" #abaaaaba
s2 = "cbaba" #cbabc
s3 = "abcbc" #abdba
s4 = "aaaa" #aaaa
s5 = "xgdfcs" #xgeegx
s6 = "slejfldsglfe" #slejfllfjels

palindrome(s6)
