# CCC 2018
# Problem J3: Are we there yet?

distance_pairs = [int(i) for i in input().split()]

distance_dict = {}

for i in range(len(distance_pairs)+1):
    city = 'city{}'.format(i+1) # city1
    for j in range(len(distance_pairs)+1):
        if i == j:
            dist = 0
        else:
            if i<j:
                dist = sum(distance_pairs[i:j])
            else:
                dist = sum(distance_pairs[j:i])
        if city not in distance_dict:
            distance_dict[city]= [dist]
        else:
            distance_dict[city].append(dist)
# print(distance_dict)
for row in distance_dict.values():
    for ele in row:
        print(ele,end=' ')
    print()