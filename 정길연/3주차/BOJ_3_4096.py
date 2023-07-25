# 000456 -> 44 -> 000500
# 숫자를 얼마나 더할 것인가가 핵심 
#   -> 0이 앞에 있을 때는 문자열이지만 계산은 숫자

# 1. 팰린드롬 판별
# 문자열 길이를 반으로 나눠서 비교 [::-1]

# 2. 팰린드롬이 되기 위한 최소거리 
#  문자열을 반으로 나눴을 때 앞부분이 0일 경우엔, 00600과 같은 형태로 만들어야함    <= 하려다 실패
#  앞부분에 숫자가 있을 경우 0010922 -> 0010100 

from math import ceil

def is_Pal(str) :
    for i in range(len(str) // 2):
        if T[i] != T[-i-1]:
            return False
    return True         # str == str[::-1] 해도 되지만,, 위에 쓴게 더 시간에 영향을 주지 않을까?


while True:
    T = input()
    T_lenght = len(T)
    if T == '0':
        break

    ans = 0

    while not is_Pal(T):
        T = str(int(T) + 1).zfill(T_lenght)
        ans += 1
    
    print(ans)
    

