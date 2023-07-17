n, m = map(int, input().split())

li = list(map(int, input().split()))

li = list(set(li))      # 중복제거 
li.sort()               # 오름차순 1 7 9

def dfs(num, start, ans): 
    if len(ans) == num:
        for i in ans:
            print(li[i], end=' ')
        print()
        
        return
    
    for i in range(start, len(li)):  
        dfs(num, i, ans+[i])

for i in range( len(li) ):
    dfs(m, i, [i])    