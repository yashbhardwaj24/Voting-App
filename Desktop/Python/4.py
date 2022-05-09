from collections import defaultdict
list=['how are you hello hello']
dict1=defaultdict(int)
for i in list :
    for j in i.split():
        dict1[j]+=1
ans=max(dict1,key=dict1.get)
print(str(ans))
