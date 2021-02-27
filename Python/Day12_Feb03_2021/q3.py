from collections import defaultdict
def func(a):
    m_lst =defaultdict(list)
    for i in range(len(a)):
        mean = sum(a[i])/len(a[i])
        m_lst[mean].append(i)

    final_list = m_lst.values()
    return final_list


a = [[3,3,4,2], [4,4],[4,0,3,3],[2,3],[3,3,3]]
print(func(a))

