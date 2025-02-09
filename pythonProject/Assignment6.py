# Discrete Structures (CSCI 220)
# Winter 2023
# Assignment 6 -
# Didarul Alam

# Acknowledgements:
# I worked with the class
# I used the following sites ... (if applicable)

import inspect
import math

import matplotlib.pyplot as plt

import Assignment4


def func_body(f):
    body = inspect.getsource(f)
    idx = body.index("return")
    return body[7 + idx:].strip()


def fact(n):
    return math.factorial(n)


def log(n):
    try:
        return math.log10(n)
    except:
        return 0


def f0(n):
    return n


def f1(n):
    return 1.5 ** n


def f2(n):
    return 8 * n ** 3 + 17 * n ** 2 + 111


def f3(n):
    return log(n) ** 2


def f4(n):
    return 2 ** n


def f5(n):
    return log(log(n))


def f6(n):
    return (n ** 2) * log(n) ** 3


def f7(n):
    return (2 ** n) * (n ** 2 + 1)


def f8(n):
    return n ** 3 + n * log(n) ** 2


def f9(n):
    return 10000


def f10(n):
    return fact(n)


def eval_funcs(funcs, sizes):
    dict_funcs = {}
    dict_log_funcs = {}
    for func in funcs:
        key = func_key(func)
        dict_funcs[key] = {}
        dict_log_funcs[key] = {}
        for n in sizes:
            dict_funcs[key][n] = func(n)
            dict_log_funcs[key][n] = int(log(func(n)))
    return dict_funcs, dict_log_funcs


def func_key(func):
    return func.__name__ + " " + func_body(func)


def plot_values(dict_funcs, sizes, funcs, title, file_name):
    func_num = 0
    plt.xticks([j for j in range(len(sizes))], [str(size) for size in sizes])
    for func in funcs:
        func_num += 1
        d = dict_funcs[func_key(func)]
        x_axis = [j + 0.05 * func_num for j in range(len(sizes))]
        y_axis = [d[i] for i in sizes]
        plt.bar(x_axis, y_axis, width=0.05, alpha=0.75, label=func_key(func))
    plt.legend()
    plt.title(title)
    plt.xlabel("Size")
    plt.ylabel("Log f(n)")
    plt.savefig(file_name)
    plt.show()


def main():
    assn = "Assignment6"
    title = "Log of Functions"
    sizes = [10 * i for i in range(11)]

    funcs = [f0, f1, f2, f3, f4, f5, f6, f7, f8, f9, f10]
    dict_funcs, dict_log_funcs = eval_funcs(funcs, sizes)

    Assignment4.print_times(dict_funcs)
    Assignment4.print_times(dict_log_funcs)
    plot_values(dict_log_funcs, sizes, funcs, title, assn + ".png")


if __name__ == "__main__":
    main()
