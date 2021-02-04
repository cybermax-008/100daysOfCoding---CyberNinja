def func(a):
    m_lst ={}
    for i in range(len(a)):
        mean = sum(a[i])/len(a[i])
        if mean in m_lst:
            m_lst[mean].append(i)
        else:
            m_lst[mean]=[i]

    final_list = list(m_lst.values())
    return final_list


a = [[3,3,4,2], [4,4],[4,0,3,3],[2,3],[3,3,3]]
print(func(a))

