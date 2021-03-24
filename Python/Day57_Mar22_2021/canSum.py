def canSum(targetSum,arr):
    if targetSum == 0:
        return True
    if targetSum <0:
        return False
    
    for i in arr:
        new_target = targetSum - i
        if canSum(new_target,arr):
            return True

    return False

def canSum_d(targetSum,arr,memo={}):
    if targetSum in memo:
        return memo[targetSum]
    if targetSum == 0:
        return True
    if targetSum <0:
        return False
    
    for i in arr:
        new_target = targetSum - i
        if canSum_d(new_target,arr):
            memo[targetSum] = True
            return True
    memo[targetSum] = False
    return False

print(canSum_d(300,[14,7]))