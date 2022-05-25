from timer import timer_func_with_result

@timer_func_with_result
def tsp_greedy():
    n = 0
    distance = []
    visited = []
    length = 0
    solution = []

    with open("input.txt", "r") as file:
        n = int(file.readline())
        visited = [False] * n
        distance = [[0] * n for i in range(n)]

        for i in range(n * (n - 1) // 2):
            u, v, w = map(lambda x: int(x), file.readline().split())
            distance[u - 1][v - 1] = w
            distance[v - 1][u - 1] = w

    last = 0
    solution.append(0)
    visited[0] = True

    while len(solution) != n:
        min_cost = -1
        next_city = -1

        for city in range(n):
            if not visited[city]:
                if min_cost == -1 or min_cost > distance[last][city]:
                    min_cost = distance[last][city]
                    next_city = city
        
        if min_cost == -1:
            break

        last = next_city
        solution.append(next_city)
        visited[next_city] = True
        length = length + min_cost

    length = length + distance[last][0]
    solution.append(0)

    return length
    # print(' '.join(map(lambda x: str(x + 1), solution)))
