def helper(arr, target):
    if len(arr)==1:
        if target + arr[0] ==0:
            return '+'
        elif target - arr[0] == 0:
            return '-'
        else:
            return 'not possible'

    combination2 =  helper(arr[1:],target - arr[0])
    if combination2 != 'not possible':
        return '-'+combination2

    combination1 =  helper(arr[1:],target + arr[0])
    if combination1 != 'not possible':
        return '+'+combination1

    return 'not possible'

def PlusMinus(num):
    num_str = list(str(num))
    num_arr = [int(i) for i in num_str]
    if len(num_arr)<2:  
        return "not possible"
    return helper(num_arr[1:],num_arr[0])





num=int(input())
print(PlusMinus(num))