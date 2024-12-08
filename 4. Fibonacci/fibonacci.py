def fibonacci(n):
    if n < 1:
        return n
    fibo = list()
    fibo.append(0)
    fibo.append(1)
    for i in range(2, n+1):
        fibo.append(fibo[i - 1] + fibo[i - 2])
    return fibo[n]


if __name__ == "__main__":
    n = int(input())
    res = fibonacci(n)
    print(res)
