# Discrete Structures (CSCI 220)
# Winter 2023
# Assignment 5 - "Estimating, Evaluating, and Solving  Recurrences"
# Didarul Alam

# Acknowledgements:
# I worked with the class
# I used the following sites ... (if applicable)


import Assignment1
import math
import numpy as np

dict_funcs = {}


def ff(f, n):
    func_name = f.__name__
    if func_name not in dict_funcs:
        dict_funcs[func_name] = {}
    dict_func = dict_funcs[func_name]
    if n not in dict_func:
        dict_func[n] = f(f, n)
    return dict_func[n]


def fib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n - 1) + fib(n - 2)


def f1_fibonacci(f, n):
    return 0 if n == 0 else (1 if n == 1 else ff(f, n - 1) + ff(f, n - 2))


def f2_bitstrings(f, n):
    return 1 if n == 0 else (2 if n == 1 else (3 if n == 2 else ff(f, n - 1) + ff(f, n - 2)))


def f3_linear_search(f, n):
    return 0 if n == 0 else 1 + ff(f, n - 1) + 1


def f4_binarysearch(f, n):
    return 0 if n == 0 else ff(f, int(n / 2)) + 1


def f5_mergesort(f, n):
    return 0 if n == 0 else 2 * ff(f, int(n / 2)) + 1


def f6_bubblesort(f, n):
    return 0 if n == 0 else 2 * ff(f, n - 1) + (n - 1)


def f7_slide(f, n):
    return 2 if n == 0 else (7 if n == 1 else ff(f, n - 1) + 2 * ff(f, n - 2))


# If f(n) = O(nc) where c < Logba then T(n) = Θ(nLogba)
# If f(n) = Θ(nc) where c = Logba then T(n) = Θ(ncLog n)
# If f(n) = Ω(nc) where c > Logba then T(n) = Θ(f(n))
def master_theorem(a, b, c):
    log_b_a = math.log(a, b)
    result = " T(n) = Θ("
    if c < log_b_a:
        result += "n^(log_" + str(b) + " " + str(a) + ")"
    elif c == log_b_a:
        result += "n^" + str(c) + " log n" + ")"
    else:
        result += "n^" + str(c) + ")"
    result += ")"
    return "Master Theorem with a = " + str(a) + " b = " + str(b) + " c = " + str(c) + " is" + result


# Solves recurrence of the form a(n) = c1 * a(n-1) + c2 * a(n-2)
def solve_recurrence(desc, c1, c0, a0, a1):
    print(desc)
    recurrence = "a(n) = " + str(c1) + "a(n-1) + " + str(c0) + "a(n-2) "
    print("The recurrence is", recurrence)
    characteristic_equation = "r^2 - " + ("" if c1 == 1 else str(c1)) + "r - " + str(c0)
    print("characteristic equation is " + characteristic_equation)
    a = 1
    b = -1 * c1
    c = -1 * c0
    temp = (math.sqrt(b ** 2 - 4 * a * c))
    r1 = ((-1 * b) + temp) / (2 * a)
    r2 = ((-1 * b) - temp) / (2 * a)
    print("The roots are", r1, r2)
    distinct = r1 != r2
    A = np.array([[r1 ** 0, (0 if not distinct else 1) * r2 ** 0], [r1 ** 1, (1 if not distinct else 1) * r2 ** 1]])
    B = np.array([a0, a1])
    X = np.linalg.solve(A, B)
    print("The coefficients are", X)
    formula = "a(n) = " + str(X[0]) + " * " + str(r1) + "^n" + " + " + str(X[1]) + " * " + (
        " n * " if not distinct else "") + str(r2) + "^n"
    print("The closed-form formula is ", formula)
    a2_recurrence = c1 * a1 + c0 * a0
    a2_formula = X[0] * r1 ** 2 + X[1] * (2 if not distinct else 1) * r2 ** 2
    print("a4 recurrence", a2_recurrence)
    print("a4 formula", a2_formula)
    print()


def call_and_print(func, sizes):
    print(func.__name__)
    print(Assignment1.func_body(func))
    for n in sizes:
        print("for n = ", n, "is", ff(func, n))
    print()


def method_theorem_examples():
    print(master_theorem(2, 2, 1))  # merge sort
    print(master_theorem(1, 2, 0))  # binary search
    print(master_theorem(4, 2, 1))  # D&C Long integer multiplication
    print(master_theorem(3, 2, 1))  # Karatsuba Long integer multiplication
    print(master_theorem(8, 2, 2))  # D&C Matrix multiplication
    print(master_theorem(7, 2, 2))  # D&C Strassen multiplication
    print(master_theorem(1, 2, 1))  # made up
    print()


def main():
    # sizes = [2 ** i for i in range(10)]
    sizes = [i for i in range(30)]
    funcs = [f1_fibonacci, f2_bitstrings, f3_linear_search,
             f4_binarysearch, f5_mergesort, f6_bubblesort, f7_slide]
    for func in funcs:
        call_and_print(func, sizes)
    method_theorem_examples()
    solve_recurrence("Fibonacci", 1, 1, 0, 1)
    solve_recurrence("Rossen ch. 8 slide 22", 1, 2, 2, 7)
    solve_recurrence("Rossen ch. 8 slide 26", 6, -9, 1, 6)
    solve_recurrence("CSCI 220 Exam Summer 2022", 6, -5, 0, 1)


if __name__ == "__main__":
    main()
