def possible_subsets(arr):
    for i in range(1<<len(arr)):
        for j in range(len(arr)):
            if i & (1<<j):
                print(arr[j],end="")
        print()


possible_subsets(['a','b','c'])

