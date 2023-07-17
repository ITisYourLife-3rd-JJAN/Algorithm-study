# def minimumTreePath(n, edges, visitNodes):
#     graph = [ [-1] * (n+1) for _ in range(n+1) ]
#     for e in edges:
#         graph[e[0]][e[1]] = 0
#         graph[e[1]][e[0]] = 0

#     node_visited = [0] * len(visitNodes)
#     visited = [0] * (len(edges)+2)
#     visited[0] = 1
#     return bfs(1, graph, visitNodes, node_visited, 0, visited)



# def bfs(start, graph, visitNodes, node_visited, ans, visited) :
#     q = [start]

#     while q:
#         now = q.pop(0)
#         visited[now] = 1
#         ans += 1
#         for i in range(len(graph[start])):
#             if 0 in node_visited:
#                 for j in range(len(visitNodes)):
#                     if graph[now][i] == 0 and i == visitNodes[j] and node_visited[j] == 0 :
#                         node_visited[j] = 1
#                         visited[i] = 1
#                         q.append(i)
#                         break
#             else : 
#                 if graph[now][i] == 0 :
#                     q.append(i)
#                     visited[i] = 1
#         if 0 not in visited:
#             break
    
#     return ans
    
ans = -1    
def minimumTreePath(n, edges, visitNodes):           
    graph = [ [-1] * (n+1) for _ in range(n+1) ]
    for e in edges:
        graph[e[0]][e[1]] = 0
        graph[e[1]][e[0]] = 0       
    visited = [0] * (len(edges)+2)
    visited[0] = 1
    node_visited = [0] * len(visitNodes)

    dfs(1, graph, visited, visitNodes, node_visited)
    return ans

def dfs(start, graph, visited, visitNodes, node_visited):
    global ans
    visited[start] = 1
    ans += 1
    for i in range(len(graph[start])):
        if graph[start][i] == 0 and i in visitNodes and node_visited[visitNodes.index(i)] == 0 :
            visited[i] = 1
            node_visited[visitNodes.index(i)] = 1
            dfs(i,  graph, visited, visitNodes, node_visited)
        elif graph[start][i] == 0 and visited[i] == 0 :
            visited[i] = 1
            dfs(i,  graph, visited, visitNodes, node_visited)
    



print(minimumTreePath(3, [[1, 2], [1, 3]], [1,2]))