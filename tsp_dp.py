import functools
distance = []
n = 0
V = 0
power2 = {}

@functools.lru_cache(maxsize=None)
def calculate_f(S, u):
    S -= (1 << u)

    if not S:
        return distance[u][0]

    result = 0
    temp = S
    while temp:
        v = temp & (-temp)
        temp -= v
        if not result:
            result = calculate_f(S, power2[v]) + distance[u][power2[v]]
        else:
            result = min(result, calculate_f(S, power2[v]) + distance[u][power2[v]])

    return result


with open("input.txt", "r") as file:
    n = int(file.readline())
    V = (1 << n) - 1
    solution = [0] * n
    distance = [[0] * n for i in range(n)]

    for i in range(n):
        power2[1 << i] = i

    for i in range(n * (n - 1) // 2):
        u, v, w = map(lambda x: int(x), file.readline().split())
        distance[u - 1][v - 1] = w
        distance[v - 1][u - 1] = w


result = 0
V = V - 1
temp = V
while temp:
    city = temp & (-temp)
    temp -= city
    if not result:
        result = calculate_f(V, power2[city]) + distance[0][power2[city]]
    else:
        result = min(result, calculate_f(V, power2[city]) + distance[0][power2[city]])

print(result)
