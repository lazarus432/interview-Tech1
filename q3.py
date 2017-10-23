# utility function to find set of an element i using path compression technique
def find(parent, i):
    if parent[i] == i:
        return i
    return find(parent, parent[i])

# function to connect two sets of x and y
def union(parent, rank, x, y):
    xroot = find(parent,x)
    yroot = find(parent, y)

    # attach smaller rank tree under root of higher rank tree
    if rank[xroot] < rank[yroot]:
        parent[xroot] = yroot
    elif rank[xroot] > rank[yroot]:
        parent[yroot] = xroot
    else:
        # if ranks are same, make one root and add one
        parent[yroot] = xroot
        rank[xroot] += 1

def KruskalMST(graph, v, inv_dict):
    result = []

    # sort all edges in non-decreasing order of weight.
    graph = sorted(graph, key=lambda item: item[2])

    parent = [] ; rank = []

    # create v subsets with single elements
    for node in range(v):
        parent.append(node)
        rank.append(0)

    i = 0
    e = 0
    while(e < v -1):
        # pick smallest edge and increment index
        u, v, w = graph[i]
        i += 1
        x = find(parent, u)
        y = find(parent, v)

        # if not cycle include in result
        if x != y:
            e = e + 1
            result.append([u,v,w])
            union(parent, rank, x, y)

    # create results to be printed
    temp = []
    final_result = {}
    for u,v,weight in result:
        temp = [(inv_dict[v], weight)]
        if inv_dict[u] not in final_result:
            final_result[inv_dict[u]] = temp
        else:
            final_result[inv_dict[u]] = final_result[inv_dict[u]].append(temp)

    return final_result

def question3(g):
    temp = {}
    inv_dict = {}
    count = 0
    u, v, w  = None, None, None
    graph = []
    for i in g:
        temp[i] = count
        inv_dict[count] = i
        count += 1

    for i in g:
        for j in g[i]:
            u, v, w = temp[i], temp[j[0]], j[1]
            graph.append([u,v,w])

    return KruskalMST(graph, count, inv_dict)


g1 = {'A': [('B', 5)],
      'B': [('A', 5), ('C', 7)],
      'C': [('B', 7), ('D', 2)],
      'D': [('C', 2)]}

g2 = {'A': [('B', 5)],
      'B': [('A', 5), ('C', 1)],
      'C': [('B', 1), ('D', 2)],
      'D': [('C', 2)]}

g3 = {}

print question3(g1) # Result {'C' : [('D', 2)]}
#print question3(g2) # Result {'C' : [('B', 1)]}
#print question3(g3) # Result {}


    
