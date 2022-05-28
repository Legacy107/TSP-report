from time import time
from timer import timer_func_with_result

def find_minimum_spanning_tree(n, edge_list):
    mst_adj_list = [[] * n for i in range(n)]
    parent = list(range(n))
    rank = [1] * n

    def get_group(u):
        nonlocal parent
        parent[u] = u if parent[u] == u else get_group(parent[u])
        return parent[u]

    def union(u, v):
        nonlocal rank
        group_u = get_group(u)
        group_v = get_group(v)

        if group_u == group_v:
            return False

        if rank[group_u] < rank[group_v]:
            parent[group_u] = group_v
        else:
            parent[group_u] = group_v
            if rank[group_u] == rank[group_v]:
                rank[group_v] += 1
        
        return True
    
    edge_list = sorted(edge_list)
    count = 0
    for edge in edge_list:
        if (union(edge[1][0], edge[1][1])):
            mst_adj_list[edge[1][0]].append(edge[1][1])
            mst_adj_list[edge[1][1]].append(edge[1][0])
            count += 1
            if count == n - 1:
                break
    
    return mst_adj_list

@timer_func_with_result
def tsp_mst(filename):
    n = 0
    distance = []
    visited = []
    length = 0
    solution = []
    edge_list = []

    with open(filename, "r") as file:
        n = int(file.readline())
        visited = [False] * n
        distance = [[0] * n for i in range(n)]

        for i in range(n * (n - 1) // 2):
            u, v, w = map(lambda x: int(x), file.readline().split())
            distance[u - 1][v - 1] = w
            distance[v - 1][u - 1] = w
            edge_list.append((w, (u - 1, v - 1)))

    mst_adj_list = find_minimum_spanning_tree(n, edge_list)

    def traverse_tree(current_node):
        nonlocal length, solution
        visited[current_node] = True
        for neighbor in mst_adj_list[current_node]:
            if not visited[neighbor]:
                length = length + distance[solution[-1]][neighbor]
                solution.append(neighbor)
                traverse_tree(neighbor)

    solution.append(0)
    traverse_tree(0)

    length = length + distance[solution[-1]][0]
    solution.append(0)

    return length
