# itertools 모듈 사용하여 손쉽게 구하기
from itertools import combinations_with_replacement

n, m = map(int, input().split())

lst = list(map(int, input().split()))
lst.sort() # 증가하는 순으로 뽑기 위해 정렬

lst = list(set(combinations_with_replacement(lst, m))) #리스트에서 m개 추출, 중복된 순열은 set으로 제거
lst.sort() # set으로 중복을 제거 해 줬으므로 다시 정렬

for i in lst:
    print(*i)



# n, m = map(int, input().split())
#
# lst = list(map(int, input().split()))
# lst.sort()
# temp = []
#
# def dfs(s):
#     if len(temp) == m:
#         print(*temp)
#         return
#     result = 0
#
#     for i in range(s, n):
#         if result != lst[i]:
#             temp.append(lst[i])
#             result = lst[i]
#             dfs(i)
#             temp.pop()
#
# dfs(0)
