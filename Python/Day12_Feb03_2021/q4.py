query_types = ['insert','addToValue','get','insert','addToKey','addToValue','get']
query = [[1,2],[2],[1],[2,3],[1],[-1],[3]]
hashMap = {}
sum_res=0
def insert(x,y):
    hashMap[x]=y

def addToValue(x):
    for k,v in hashMap.items():
        hashMap[k] = v+x

def addToKey(x):
    new_dict ={}
    global hashMap
    for k,v in hashMap.items():
        new_dict[k+x]=v
    hashMap=new_dict

def get(x):
    return hashMap[x]

for t,q in zip(query_types,query):
    if t=='insert':
        insert(q[0],q[1])
        # print(hashMap)
    if t=='addToValue':
        addToValue(q[0])
        # print(hashMap)
    if t=='addToKey':
        addToKey(q[0])
        # print(hashMap)
    if t=='get':
        f=get(q[0])
        sum_res+=f
        # print(f)
print(sum_res)
