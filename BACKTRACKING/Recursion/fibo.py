def fibo(n):
    if n == 0:
        print("n:", n)
        return 0
    if n == 1:
        print("n:", n)
        return 1
    print("n:", n)

    fib1 = fibo(n - 1)
    print("fib1:", fib1)
    print("after fib1 n:", n)

    fib2 = fibo(n - 2)
    print("fib2:", fib2)

    return fib1 + fib2


def better_fibo(n, a=0, b=1):
    print("n:", n, "a:", a, "b:", b)
    if n == 0:
        return a
    if n == 1:
        return b

    return better_fibo(n - 1, b, a + b)


fibo(5)
print("Better fibo:")
better_fibo(5)
