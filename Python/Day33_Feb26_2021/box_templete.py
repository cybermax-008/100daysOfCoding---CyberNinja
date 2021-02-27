from collections import Counter
def count_invalid_boxes(box_templete_list):
    count = 0
    for item in box_templete_list:
        box = Counter(item[0])
        tem = Counter(item[1])
        if len(item[0]) != len(item[1]):
            count+=1
            continue
        elif len(box) != len(tem):
            count+=1
            continue
        elif set(item[0])!=set(item[1]):
            count+=1
            continue
        else:
            continue

    return count


b = [["cm","mc"],
     ["pm","mc"],
     ['ccm','mc'],
     ['c','mc']]

print(count_invalid_boxes(b))