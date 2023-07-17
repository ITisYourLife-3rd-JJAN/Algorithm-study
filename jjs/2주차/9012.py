N = int(input())

for _ in range(N):
    t = input()
    lst = list(t)
    cnt = 0

    for i in lst:
        if i == "(":
            cnt += 1
        elif i == ")":
            cnt -= 1

        # 만약 ()순서로 나오다가 )가 먼저 나왔을 경우
        if cnt < 0:
            print("NO")
            # break

    if cnt > 0:
        print("NO")
    elif cnt == 0:
        print("YES")