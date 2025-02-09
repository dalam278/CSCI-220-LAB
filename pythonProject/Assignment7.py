# Discrete Structures (CSCI 220)
# Winter 2023
# Assignment 7- "Relations and Graphs"
# Didarul Alam

# Acknowledgements:
# I worked with the class & classmate
# I used the following sites ... (if applicable)

import random
import numpy as np
import texttable

PROB_EDGE = .5
SIZE = 10


def print_data(headers, data):
    tt = texttable.Texttable()
    tt.set_cols_align(["c"] * len(headers))
    tt.set_cols_dtype(["t"] * len(headers))
    tt.add_rows([headers] + data)
    print(tt.draw())
    print()


def random_graph(size, p_edge):
    matrix = [[0] * size for _ in range(size)]
    for i in range(size):
        for j in range(size):
            if i != j:
                if random.random() < p_edge:
                    matrix[i][j] = 1
    return matrix


def to_table(matrix):
    n = len(matrix)
    table = [[] for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if matrix[i][j] == 1:
                table[i].append(j)
    return table


def print_matrix(matrix):
    print(np.array(matrix))
    print()


def print_table(table):
    n = len(table)
    for i in range(n):
        print(i, table[i])
    print()


def is_reflexive(matrix):
    reflexive = True
    for i in range(len(matrix)):
        if matrix[i][i] == 0:
            reflexive = False
    return reflexive


def is_anti_reflexive(matrix):
    anti_reflexive = True
    for i in range(len(matrix)):
        if matrix[i][i] == 1:
            anti_reflexive = False
    return anti_reflexive


def is_irreflextive(matrix):
    return not is_reflexive(matrix) and not is_anti_reflexive(matrix)


def is_symmetric(matrix):
    symmetric = True
    for i in range(len(matrix)):
        for j in range(len(matrix)):
            if matrix[i][j] != matrix[j][i]:
                symmetric = False
    return symmetric


def is_anti_symmetric(matrix):
    anti_symmetric = True
    for i in range(len(matrix)):
        for j in range(len(matrix)):
            if i != j and matrix[i][j] == matrix[j][i]:
                anti_symmetric = False
    return anti_symmetric


def is_transitive(matrix):
    transitive = True
    n = len(matrix)
    for i in range(n):
        for j in range(n):
            for k in range(n):
                if matrix[i][j] == 1 and matrix[j][k] == 1 and matrix[i][k] == 0:
                    transitive = False
    return transitive


def is_eulerian_circuit(matrix):
    n = len(matrix)
    for i in range(n):
        degree = 0
        for j in range(n):
            degree += matrix[i][j]
        if degree % 2 == 1:
            return False
    return True


def is_complete(matrix):
    n = len(matrix)
    for i in range(n):
        degree = 0
        for j in range(n):
            degree += matrix[i][j]
        if degree != n - 1:
            return False
    return True


def is_star(matrix):
    vertexD1 = 0
    vertexDn_1 = 0
    if SIZE == 1:
        return matrix[0][0] == 0
    elif SIZE == 2:
        return matrix[0][0] == 0 and matrix[0][1] == 1 and matrix[1][0] == 1 and matrix[1][1] == 0
    else:
        for i in range(SIZE):
            degreeI = 0
            for j in range(SIZE):
                degreeI += matrix[i][j]
            if degreeI == 1:
                vertexD1 += 1
            else:
                vertexDn_1 += 1
    return vertexD1 == SIZE - 1 and vertexDn_1 == 1


def is_connected(matrix):
    visited = set()
    results = []
    dfs_util(results, 0, visited, matrix)
    return len(results) == SIZE


def is_cyclic_util(matrix, v, visited, stack):
    visited[v] = True
    stack[v] = True
    for j in range(SIZE):
        if matrix[v][j] == 1 and not visited[j]:
            if is_cyclic_util(matrix, j, visited, stack):
                return True
        elif matrix[v][j] == 1 and stack[j]:
            return True
    stack[v] = False
    return False


def is_cyclic(matrix):
    visited = [False] * (SIZE + 1)
    stack = [False] * (SIZE + 1)
    for node in range(SIZE):
        if not visited[node]:
            if is_cyclic_util(matrix, node, visited, stack):
                return True
    return False


def find_degrees_neighbors(matrix):
    n = len(matrix)
    in_degrees = [0] * n
    out_degrees = [0] * n
    neighbors = [[] for _ in range(n)]
    for i in range(n):
        for j in range(n):
            in_degrees[i] += matrix[j][i]
            out_degrees[i] += matrix[i][j]
            if matrix[i][j] == 1:
                neighbors[i].append(j)
    return in_degrees, out_degrees, neighbors


def add_totals(data, cols):
    totals = ["Totals"] + [""] * (len(data[0]) - 1)
    for k in range(len(cols)):
        col = cols[k]
        totals[col] = 0
        for i in range(len(data)):
            totals[col] += data[i][col]
    data.append(totals)


def target_probability_edge(matrix):
    return PROB_EDGE


def implied_probability_edge(matrix):
    n = len(matrix)
    n_edges = 0
    for i in range(n):
        for j in range(n):
            n_edges += matrix[i][j]
    return round(n_edges / (n ** 2 - n), 4)


def dfs_util(results, u, visited, matrix):
    visited.add(u)
    results.append(u)
    for v in range(len(matrix[u])):
        if matrix[u][v] == 1 and v not in visited:
            dfs_util(results, v, visited, matrix)


def dfs(matrix):
    visited = set()
    results = []
    for u in range(len(matrix)):
        if u not in visited:
            dfs_util(results, u, visited, matrix)
    return results


def bfs_util(results, u, visited, matrix):
    queue = [u]
    visited.add(u)
    while queue:
        u = queue.pop(0)
        results.append(u)
        for v in range(len(matrix[u])):
            if matrix[u][v] == 1 and v not in visited:
                queue.append(v)
                visited.add(v)


def bfs(matrix):
    visited = set()
    results = []
    for u in range(len(matrix)):
        if u not in visited:
            bfs_util(results, u, visited, matrix)
    return results


def num_vertices(matrix):
    return len(matrix)


def num_edges(matrix):
    return sum([sum(matrix[i]) for i in range(len(matrix))])


def main():
    matrix = random_graph(SIZE, PROB_EDGE)
    table = to_table(matrix)
    print_matrix(matrix)
    print_table(table)

    headers = ["Vertex", "In-degree", "Out-degree", "Neighbors"]
    in_degrees, out_degrees, neighbors = find_degrees_neighbors(matrix)
    data = [[i, in_degrees[i], out_degrees[i], neighbors[i]] for i in range(SIZE)]
    add_totals(data, [1, 2])
    print_data(headers, data)

    headers = ["Property", "Value"]
    data = []
    for f in [num_vertices, num_edges, target_probability_edge,
              implied_probability_edge, dfs, bfs,
              is_reflexive, is_anti_reflexive, is_reflexive,
              is_symmetric, is_anti_symmetric, is_transitive,
              is_eulerian_circuit, is_complete, is_star,
              is_connected, is_cyclic]:
        data.append([f.__name__, f(matrix)])
    print_data(headers, data)


if __name__ == "__main__":
    main()