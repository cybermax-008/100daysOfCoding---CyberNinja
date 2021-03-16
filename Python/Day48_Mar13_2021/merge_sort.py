def merge_sort(array):
    if len(array)<2:
        return array
    mid = len(array)//2
    return merge(merge_sort(array[:mid]),
                merge_sort(array[mid:]))


def merge(left_half, right_half):
    if len(left_half)<1:
        return right_half
    if len(right_half)<1:
        return left_half

    result = []
    index_left = index_right = 0

    while len(result) < len(left_half) + len(right_half):
        if left_half[index_left] < right_half[index_right]:
            result.append(left_half[index_left])
            index_left+=1
        else:
            result.append(right_half[index_right])
            index_right+=1
        if index_left == len(left_half):
            result+=right_half[index_right:]
            break
        if index_right == len(right_half):
            result += left_half[index_left:]
            break

    return result


arr = [2,1,4,5,10,7,8,3,9,20]
print(merge_sort(arr))
        