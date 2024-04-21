def printAdjacencyList(nodes, e, edges):
    adj = [[i] for i in range(nodes)]       # [[0],[1],[2]]
    for u,v in edges:
        adj[u].append(v)        # On uth index put v
        adj[v].append(u)        # On vth index put u

    return adj

def printAdjacencyMatrix(nodes, e, edges):
    adjMat = [[0]*nodes for _ in range(nodes)]  #[[0,0,0],[0,0,0],[0,0,0]]
    for u,v in edges:
        adjMat[u][v] = 1                        # at index u,v mark 1
        adjMat[v][u] = 1                        # at index v,u mark 1
    return adjMat


edges = [[2,1],[2,0]]
adjList = printAdjacencyList(3,2,edges)
adjMat = printAdjacencyMatrix(3,2,edges)
print(adjList)
print(adjMat)