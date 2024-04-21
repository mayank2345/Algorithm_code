from collections import deque


def addEdge(adj, u, v):
    adj[u].append(v)
    adj[v].append(u)
def addEdgeDis(adj, u, v):
    adj[u].append(v)

def createAdjList(edges):
    E = len(edges)
    adj = [[] for _ in range(E)]
    for u, v in edges:
        addEdge(adj, u, v)
    return adj

def createAdjListDis(edges):
    E = len(edges)
    adj = [[] for _ in range(E)]
    for u, v in edges:
        addEdgeDis(adj, u, v)
    return adj

def bfs(adj):
    V = len(adj)
    vis = [False] * V
    q = deque()
    q.append(0)
    vis[0] = True
    res = []
    while q:
        s = q.popleft()
        res.append(s)
        for u in adj[s]:
            if not vis[u]:
                vis[u] = True
                q.append(u)
    return res


def dfs(adj):
    V = len(adj)
    vis = [False] * V
    res = []
    for i in range(V):
        if vis[i] == False:
            dfsRec(adj, vis, i, res)
    return res


def dfsRec(adj, vis, s, res):
    vis[s] = True
    res.append(s)
    for u in adj[s]:
        if not vis[u]:
            dfsRec(adj, vis, u, res)


# edges = [[0, 1], [0, 4], [1, 2], [2, 3], [4, 5], [4, 6], [5, 6], [7,8]]
# adj = createAdjList(edges)
edges = [[0,1],[1,0],[1,2],[2,0],[3,4]]
adj = createAdjListDis(edges)
print(adj)
print(dfs(adj))
