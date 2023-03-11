def fib(n):
    results = []
    a, b = 0, 1
    while a < n:
        results.append(a)
        a, b = b, a+b
    print(results) 

numbers = fib(10)