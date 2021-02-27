from collections import deque
gg = [3,3,4,19,7,2,5,11]

s = deque()
for ele in gg:
    if ele%2 !=0:
        s.appendleft(ele)
    else:
        o = s.popleft()
        if o>ele:
            s.appendleft(ele)
    print(len(s))