def fibonacci(m, n):
    sum = 0
    prev = 0
    curr = 1
    m %= 60
    n %= 60
    if n < m:
        n += 60
    for _ in range(n+1):
        if m <= _ <= n:
            sum += prev
        temp = curr
        curr += prev
        prev = temp
    return sum % 10


if __name__ == "__main__":
    input = input()
    tokens = input.split()
    m = int(tokens[0])
    n = int(tokens[1])
    res = fibonacci(m, n)
    print(res)
