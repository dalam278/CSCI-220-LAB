# Discrete Structures (CSCI 220)
# Winter 2023
# Assignment 1 - Propositional Logic and Truth Tables
# Didarul Alam

# Acknowledgements:
# I worked with the class
# I used the following sites ... (if applicable)

def ff(func, n):
    pass


def call_and_print(func, n, desc):
    print(func.__name__, desc, "for n =", n, "is", ff(func, n))



from itertools import chain, combinations


def get_function_type(func, domain_of_func, codomain_of_func):
    func_type = "partial "
    total = True
    one_to_one = True
    range_of_func = []
    for x in domain_of_func:
        y = func(x)
        if y not in codomain_of_func:
            total = False
        if y in range_of_func:
            one_to_one = False
        else:
            range_of_func.append(y)
    onto = set(range_of_func) == codomain_of_func
    if total:
        func_type += "total "
    if onto:
        func_type += "surjection(onto) "
    if one_to_one:
        func_type += "Injection (one-to-one) "
    if onto and one_to_one:
        func_type += "Bijection (onto and one-to-one) "
    return func_type


def f_successor(n):
    return n + 1


def f_predecessor(n):
    return n - 1


def f_double(n):
    return n * 2


def f_half(n):
    return int(n / 2)


def f_identity(n):
    return n


# sum_geometric_series(a, r, n) = a + ar + ar^2 + … + ar^n
def sum_geometric_series(a, r, n):
    return sum([a * r ** i for i in range(n + 1)])


def formula_geometric_series(a, r, n):
    return a * ((r ** (n + 1) - 1) / (r - 1))


# sum_arithmetic_series(n, a, d) = a + ad + 2ad + … + nad
def sum_arithmetic_series(a, d, n):
    return sum([a + d * i for i in range(n + 1)])


def formula_arithmetic_series(a, d, n):
    return a * (n + 1) + d * n * (n + 1) / 2


# sum_counting(n) = 1 + 2 + … + n
def sum_counting(n):
    return sum([i for i in range(n + 1)])


def formula_counting(n):
    return n * (n + 1) / 2


# sum_squares(n) = 1^2 + 2^2 + 3^2 + … + n^2
def sum_squares(n):
    return sum([i ** 2 for i in range(n + 1)])


def formula_squares(n):
    return n * (n + 1) * (2 * n + 1) / 6


# sum_cubes(n) = 1^3 + 2^3 + 3^3 + … + n^3
def sum_cubes(n):
    return sum([i ** 3 for i in range(n + 1)])


def formula_cubes(n):
    return (n * (n + 1) / 2) ** 2


def generate_binary_number(binary_numbers):
    return "0." + "".join([bin_inv(binary_numbers[i][2 + i]) for i in range(len(binary_numbers))])


def bin_inv(b):
    return "0" if b == "1" else "1"


# set_union(set1, set2) : X ∪ Y
def set_union(set1, set2):
    return set1.union(set2)


# set_intersection(set1, set2): X ∩ Y
def set_intersection(set1, set2):
    return set1.intersection(set2)


# set_difference(set1, set2): X − Y
def set_difference(set1, set2):
    return set1.difference(set2)


# set_symmetric_difference(set1, set2):  X ∆  Y
def set_symmetric_difference(set1, set2):
    return set1.symmetric_difference(set2)


# set_cartesian_product(set1, set2): X x Y
def set_cartesian_product(set1, set2):
    return [(s1, s2) for s1 in set1 for s2 in set2]


# set_power_set(set1):  P(X)
def set_power_set(set1):
    s = list(set1)
    return list(chain.from_iterable(combinations(s, r) for r in range(len(s) + 1)))


def do_question(num, func):
    print("Question", num)
    func()


def question4():
    list_b = ["0.010011", "0.101010", "0.111000", "0.000111", "0.111111", "0.111000"]
    print(list_b,"new:", generate_binary_number(list_b))
    print()


def question3():
    print('geometric series', sum_geometric_series(1, 2, 3), formula_geometric_series(1, 2, 3))
    print('geometric series', sum_geometric_series(6,5,4), formula_geometric_series(6,5,4))
    print('arithmetic series', sum_arithmetic_series(1, 2, 3), formula_arithmetic_series(1, 2, 3))
    print('arithmetic series', sum_arithmetic_series(4, 5, 6), formula_arithmetic_series(4, 5, 6))
    print('sum of natural numbers', sum_counting(6), formula_counting(6))
    print('sum of natural numbers', sum_counting(9), formula_counting(9))
    print('sum of square', sum_squares(6), formula_squares(6))
    print('sum of square', sum_squares(9), formula_squares(9))
    print('sum of cubes', sum_cubes(9), formula_cubes(9))
    print()


def question2():
    set1 = {"a", "ab", "abc", "abcd"}
    set2 = {"a", "bb", "ccc", "dddd"}
    print("Set1", set1)
    print("Set2", set2)
    print("set_union", set_union(set1, set2))
    print("set_intersection", set_intersection(set1, set2))
    print("set_difference", set_difference(set1, set2))
    print("set_symmetric_difference", set_symmetric_difference(set1, set2))
    print("set_cartesian_product", set_cartesian_product(set1, set2))
    print("power set of set", set_power_set(set1))
    print()


def question1():
    domain_func = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    codomain_func = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    print("Domain: ", domain_func)
    print("CoDomain: ", codomain_func)
    for func in [f_identity, f_double, f_half, f_predecessor, f_successor]:
        print(func.__name__, get_function_type(func, domain_func, codomain_func))
    print()

def main():
    questions = [question1, question2, question3, question4]
    for i in range(len(questions)):
        do_question(i+1, questions[i])


if __name__ == "__main__":
    main()