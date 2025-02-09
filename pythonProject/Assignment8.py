# Discrete Structures (CSCI 220)
# Winter 2023
# Assignment 8- Graphs and MST Algorithms
# Didarul Alam

# Acknowledgements:
# I worked with the class & classmate
# I used the following sites ... (if applicable)
import random
import numpy as np

SIZE = 10
MAX_COST = 9999
INF = MAX_COST + 1


def print_matrix(matrix):
    print(np.array(matrix))
    print()


def random_weighted_graph(size, max_cost):
    matrix = [[0] * size for _ in range(size)]
    for i in range(size):
        matrix[i][i] = INF
        for j in range(i + 1, size):
            matrix[i][j] = random.randint(1, max_cost)
            matrix[j][i] = matrix[i][j]
    return matrix


def min_key(key, mst_set):
    mn = INF
    for v in range(SIZE):
        if key[v] < mn and not mst_set[v]:
            mn = key[v]
            min_index = v
    return min_index


def prim_mst(matrix):
    print("Prim MST")
    key = [INF] * SIZE
    parent = [None] * SIZE
    mst = [False] * SIZE
    key[0] = 0
    parent[0] = -1
    for i in range(SIZE):
        u = min_key(key, mst)
        mst[u] = True
        for v in range(SIZE):
            if matrix[u][v] < INF and not mst[v] and key[v] > matrix[u][v]:
                key[v] = matrix[u][v]
                parent[v] = u

    cost = 0
    print("Edge \t Weight")
    for i in range(1, SIZE):
        cost += matrix[i][parent[i]]
        print(parent[i], '-', i, '\t', matrix[i][parent[i]])
    print("Total cost for", SIZE - 1, "edges is ", cost)


def find(parent, i):
    while parent[i] != i:
        i = parent[i]
    return i


def union(parent, i, j):
    a = find(parent, i)
    b = find(parent, j)
    parent[a] = b


def kruskal_mst(matrix):
    print("\nKruskal MST")
    parent = [i for i in range(SIZE)]
    min_cost = 0
    for i in range(SIZE):
        parent[i] = i
    edge_count = 0
    while edge_count < SIZE - 1:
        mn = INF
        a = -1
        b = -1
        for i in range(SIZE):
            for j in range(SIZE):
                if find(parent, i) != find(parent, j) and matrix[i][j] < mn:
                    mn = matrix[i][j]
                    a = i
                    b = j
        union(parent, a, b)
        print(a, '-', b, mn)
        edge_count += 1
        min_cost += mn
    print("Total cost for", SIZE - 1, "edges is ", min_cost)


def main():
    for i in range(10):
        matrix = random_weighted_graph(SIZE, MAX_COST)
        print_matrix(matrix)
        prim_mst(matrix)
        kruskal_mst(matrix)


if __name__ == "__main__":
    main()
