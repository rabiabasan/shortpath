import itertools

graph = [ 
    [0, 10, float('inf'), float('inf'), float('inf'), 6],
    [10, 0, 19, float('inf'), 7, float('inf')],
    [float('inf'), 19, 0, 22, float('inf'), 25],
    [float('inf'), float('inf'), 22, 0, 5, float('inf')],
    [float('inf'), 7, float('inf'), 5, 0, 12],
    [6, float('inf'), 25, float('inf'), 12, 0],
]

def calculate_path_cost(graph, path):
    cost = 0
    for i in range(len(path) - 1):
        cost += graph[path[i]][path[i + 1]]
    cost += graph[path[-1]][path[0]]  
    return cost

def traveling_salesman(graph):
    n = len(graph)
    cities = range(n)
    min_cost = float('inf')
    best_path = []

    for perm in itertools.permutations(cities):
        cost = calculate_path_cost(graph, perm)
        if cost < min_cost:
            min_cost = cost
            best_path = perm

    return best_path, min_cost

best_path, min_cost = traveling_salesman(graph)

print("Shortest path:", best_path)
print("Shortest cost:", min_cost)
