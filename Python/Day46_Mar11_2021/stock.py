# given stock prices for the next 30 days
# [20, 10, 19, 50, ...]

# max profit 
# buy at most once
# sale at most once
# sale after you buy

# [10, 20, 30, 40]
# buy at 0 day
# sale at day 3

# [40, 30, 20, 10]
# cannot buy - return -1, -1

# [40, 10, 20, 30]
# buy at day 1
# sale at day 3

# [30, 40, 2, 29]
# buy at day 2
# sale at day 3

# return buy and sale day

        
# [10, 40, 2, 15]
# [2, 50, 100, 5, 200]
def stock(arr):
    buy_pt = 0
    for i in range(arr):
        if arr[i] < arr[i+1]:
            buy_pt = i
            break
    if i==len(arr)-1:
        profit = arr[len(arr)-1] - arr[buy_pt]
        if profit>0:
            return buy_pt,len(arr)-1
        else:
            return -1,-1
    sell_pt = arr[buy_pt+1]
    for i in range(arr[buy_pt+1:]):
        if arr[sell_pt] < arr[i]:
            sell_pt = i
            
    return buy_pt,sell_pt
            
            
            
            
        


# write a program to find the minimum of 3 integers (x,y,z)

def min_3(x,y,z):
    final_min = x
    if final_min > y:
        final_min = y
    if final_min > z:
        final_min = z
    
    return final_min
    
# second largest in an array of integers

def sec_largest(my_arr):
    
    largest = 0
    sec_largest = 0
    
    for ele in my_arr:
        if ele > largest:
            sec_largest = largest
            largest = ele
        elif ele > sec_largest and ele <largest:
            sec_largest = ele
        else:
           pass
    return sec_largest
    
my_arr = [0,10,1,9,10]