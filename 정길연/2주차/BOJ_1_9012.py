T = int(input())

for i in range(T):
    stack = []
    braket = input()
    for b in braket:
        if b == '(':
            stack.append(j)
        elif b == ')':
            if stack:
                stack.pop()
            else:
                print("NO")
                break   # 끝 > 다음 input으로 넘어감
    else: 
        if not stack: # 스택이 비어있다면 알맞은 괄호
            print("YES")
        else:   
            print("NO")