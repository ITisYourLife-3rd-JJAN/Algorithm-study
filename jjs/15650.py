# itertools 모듈 사용하여 손쉽게 구하기
# 근데 이해는 잘 안감
from itertools import combinations

n, m = map(int, input().split())

lst = combinations(range(1, n+1), m)

for i in lst:
    print(*i)

# 스터디 아니고 그냥 푸는거였다면
# 아마 dfs로 풀었을 듯,,
# 나중에 dfs 주차에 다른 방법으로 풀어보기 해도 좋을듯