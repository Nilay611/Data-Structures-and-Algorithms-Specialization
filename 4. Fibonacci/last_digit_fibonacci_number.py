def fibonacci(n):
    if n < 1:
        return n
    prev = 0
    curr = 1
    for _ in range(n-1):
        temp = curr % 10
        curr += prev % 10
        prev = temp
    return curr % 10


if __name__ == "__main__":
    n = int(input())
    res = fibonacci(n)
    print(res)
