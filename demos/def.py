def test(n):
    if n == 1:
        return 1
    return n * test(n - 1)

print test(10)


def fib(n):
    if n < 0:
        return;
    a, b = 0, 1
    while True:
        if a < n:
            print a;
            a, b = b, a + b
        else:
            break;


fib(10)
