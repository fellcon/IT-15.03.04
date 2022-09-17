while True:
    fib = lambda i : 0 if i < 1 else 1 if i == 1 \
        else fib(i-1) + fib(i-2)
    x = int(input())
    i = 0
    while x > fib(i):
        i+=1
    print('Число Фиббоначи' if fib(i) == x else 'Другое число')