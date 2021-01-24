def solution(T, R):
    tt = [i[:-1]if i[-1].isalpha() else i for i in T]
    tt_uni = set(tt)
    failed = []
    for t,r in zip(tt,R):
        if t in failed:
            continue
        else:
            if r != 'OK':
                failed.append(t)
    score = (len(tt_uni)-len(failed))*100//len(tt_uni)
    return score
        
"""
Given List T and R which contains details testcase results. Find the score
of the test suite based on number of groups passed. 
"""

T = ['test1a','test2','test1b','test1c','test3']
R = ['Wrong answer','OK','Runtime error','OK','Time limit exceeded']
res = solution(T,R)
print(res)