def fibonacci(n):
    n %= 60
    prev = 0
    curr = 1
    for _ in range(n+1):
        temp = curr
        curr += prev
        prev = temp
    return (curr - 1) % 10


if __name__ == "__main__":
    n = int(input())
    res = fibonacci(n)
    print(res)
