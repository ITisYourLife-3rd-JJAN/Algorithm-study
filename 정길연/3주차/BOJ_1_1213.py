from collections import Counter

name_list = list(input())
names = Counter(name_list)

name_list.sort()

cnt = 0
for item in names:
    if names[item] % 2 == 1:
        cnt += 1
        center = item
        name_list.remove(item)
    if cnt > 1:
        break

if cnt > 1:
    print("I'm Sorry Hansoo")
else:
    ans = ""
    for i in range(0, len(name_list), 2):
        ans += name_list[i]
        
    print (ans + center + ans[::-1])
    



