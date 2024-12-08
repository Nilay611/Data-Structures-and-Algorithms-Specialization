def fibonacci(n):
    n %= 60
    prev = 0
    curr = 1
    for _ in range(n):
        temp = curr
        curr += prev
        prev = temp
    return (curr * prev) % 10


if __name__ == "__main__":
    n = int(input())
    res = fibonacci(n)
    print(res)
