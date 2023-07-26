from collections import Counter

N = list(map(str, input()))
N.sort()

cnt = Counter(N)
odd = 0
c_word = ""

for i in cnt:
    if cnt[i] % 2 == 1:
        odd += 1
        c_word += i
        N.remove(i)

    if odd > 1:
        print("I'm Sorry Hansoo")
        break

result = ""

if odd == 1:
    words = ""
    for i in range(0, len(N), 2):
        words += N[i]
    result = words + c_word + words[::-1]

print(result)