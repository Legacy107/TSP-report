from timer import timer_func_with_result

@timer_func_with_result
def tsp_br(filename):
    length = 0
    cities = []
    minimum = 0
    solution = []
    distance = []
    visited = []
    n = 0

    def find_solution(index):
        nonlocal n, distance, cities, length, solution, minimum

        if index == n:
            length += distance[cities[0]][cities[n - 1]]

            if not minimum or length < minimum:
                minimum = length
                solution = cities[:]

            length -= distance[cities[0]][cities[n - 1]]
            return

        for city in range(n):
            if not visited[city]:
                visited[city] = True
                cities[index] = city
                length += distance[cities[index - 1]][cities[index]]
                find_solution(index + 1)
                visited[city] = False
                length -= distance[cities[index - 1]][cities[index]]


    with open(filename, "r") as file:
        n = int(file.readline())
        visited = [False] * n
        cities = [0] * n
        solution = [0] * n
        distance = [[0] * n for i in range(n)]

        for i in range(n * (n - 1) // 2):
            u, v, w = map(lambda x: int(x), file.readline().split())
            distance[u - 1][v - 1] = w
            distance[v - 1][u - 1] = w

    visited[0] = True    
    find_solution(1)
    return minimum
    # print(' '.join(map(lambda x: str(x + 1), solution)))
