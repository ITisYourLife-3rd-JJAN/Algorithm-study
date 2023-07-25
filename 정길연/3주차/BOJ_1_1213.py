from collections import Counter

name_list = list(input())
names = Counter(name_list)

names.sort()

cnt = 0
for item in names:
    if names[item] % 2 == 1:
        cnt += 1
        center = item
        name_list.remove(item)
    if cnt > 1:
        break

    

