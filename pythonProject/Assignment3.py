# Discrete Structures (CSCI 220)
# Winter 2023
# Assignment #3 "Induction and Recursion"
# Didarul Alam

# Acknowledgements:
# I worked with the class & classmate from discord
# I used the following sites ... (if applicable)

import math
import random


def fib_iterative(n):
    f0 = 0
    f1 = 1
    f2 = 0
    for i in range(2, n + 1):
        f2 = f1 + f0
        f0 = f1
        f1 = f2
    return f2


def fib_recursive(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib_recursive(n - 1) + fib_recursive(n - 2)


def fib_formula(n):
    sqrt5 = math.sqrt(5)
    return (1 / sqrt5) * (((1 + sqrt5) / 2) ** n - ((1 - sqrt5) / 2) ** n)


def find_postage(amount, stamps):
    if amount == 12:
        stamps[4] += 3
    elif amount == 13:
        stamps[5] += 1
        stamps[4] += 2
    elif amount == 14:
        stamps[5] += 2
        stamps[4] += 1
    elif amount == 15:
        stamps[5] += 3
    else:
        stamps[4] += 1
        find_postage(amount - 4, stamps)


def gcd_recursive(a, b):
    return b if a == 0 else gcd_recursive(b % a, a)


def all_strings(alphabet, size):
    strings = [""]
    strings2 = [""]
    for i in range(1, size + 1):
        strings3 = []
        for w in strings2:
            for a in alphabet:
                strings3.append(w + a)
        strings += strings3
        strings2 = strings3
    return strings


def rd3(n):
    return round(n, 3)


def question1():
    for amount in range(12, 101):
        stamps = {4: 0, 5: 0}
        find_postage(amount, stamps)
        print("Postage for", amount, "is", stamps)


def question2():
    numbers = 10
    print("Fibonacci Numbers:")
    for n in range(2, numbers + 1):
        fi = rd3(fib_iterative(n))
        fr = rd3(fib_recursive(n))
        ff = rd3(fib_formula(n))
        print(n, "Iterative", fi, "Recursive", fr, "Formula", ff, "MATCH" if fr == ff and fi == fr else "ERROR")


def question3():
    trials = 10
    for trial in range(trials):
        a = random.randint(1, 100)
        b = random.randint(1, 100)
        gcd1 = math.gcd(a, b)
        gcd2 = gcd_recursive(a, b)
        print("GCD of:", a, b, "math.gcd", gcd1, "Recursive", gcd2, "MATCH" if gcd1 == gcd2 else "ERROR")


def question4():
    alphabet = {"a"}
    print(alphabet, all_strings(alphabet, 10))
    alphabet = {"a", "b", "c"}
    print(alphabet, all_strings(alphabet, 3))


def do_question(num, func):
    print("Question", num)
    func()
    print()


def main():
    questions = [question1, question2, question3, question4]
    for i in range(len(questions)):
        do_question(i + 1, questions[i])


if __name__ == "__main__":
    main()