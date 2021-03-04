# Brute Force method
def productExceptSelf_1(arr):
    out = []
    n = len(arr)
    for i in range(n):
        temp_product = 1
        for j in range(n):
            if i !=j:
                temp_product*=arr[j]
        out.append(temp_product)

    return out

# Two pass method with division. But this doesnt cover the edge case of having 0 in the array.
# If more than one zero, the result will have all zeroes. But if the array has One zero, we will have finite value for one element.
def productExceptSelf_2(arr):
    n = len(arr)
    temp_product = 1
    for i in range(n):
        temp_product*=arr[i]
    
    for i in range(n):
        arr[i]=temp_product//arr[i]
    
    return arr

def productExceptSelf_3(arr):
    n = len(arr)
    temp_product =1
    countZero = 0
    for i in range(n):
        if arr[i]==0:
            countZero+=1
        else:
            temp_product*=arr[i]
    if countZero>1:
        return [0]*n
    for i in range(n):
        if countZero>0:
            if arr[i]==0:
                arr[i] = temp_product
            else:
                arr[i]=0
        else:
            arr[i]=temp_product//arr[i]
    return arr
    
arr1 = [1,2,3,4]
print(productExceptSelf_1(arr1))
print(productExceptSelf_2(arr1))
print(productExceptSelf_3(arr1))
