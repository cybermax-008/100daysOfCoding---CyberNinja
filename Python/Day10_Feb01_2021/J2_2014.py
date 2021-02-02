# CCC 2014
# Problem J2: Vote Count

total_votes  = int(input())
votes = input()
vote_A = 0
vote_B = 0

for i in range(total_votes):
    vote = votes[i]
    if vote == 'A':
        vote_A+=1
    else:
        vote_B+=1
if vote_A>vote_B:
    print('A')
elif vote_A<vote_B:
    print('B')
else:
    print('Tie')