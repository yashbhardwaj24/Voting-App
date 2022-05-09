from collections import Counter
s = "hello how are you hello how"
s1 = s.split()
Counter = Counter(s1)
# s2=Counter.most_common()
print(Counter.most_common())
