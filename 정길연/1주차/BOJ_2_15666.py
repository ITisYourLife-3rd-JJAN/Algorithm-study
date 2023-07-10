n, m = map(int, input().split())

li = list(map(int, input().split()))
dup_check=[]


def dfs(num, start, ans):
    if len(ans) == num:
        for i in ans:
            print(li[i],end=' ')
        print()
        
        return
    
    for i in range(start, len(li)):
        dfs(num,i,ans+[i])

li = list(set(li))
li.sort()

for i in range( len(li) ):
    dfs(m, i, [i])