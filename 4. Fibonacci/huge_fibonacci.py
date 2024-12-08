def calc_pisano_period(m):
    prev, curr = 0, 1
    for i in range(m * m):
        prev, curr = curr, (prev + curr) % m

        if prev == 0 and curr == 1:
            return i + 1


def fibonacci(n, m):
    if n <= 1:
        return n
    x = calc_pisano_period(m)
    n %= x
    prev = 0
    curr = 1
    for _ in range(n-1):
        temp = curr
        curr += prev
        prev = temp
    return curr % m


if __name__ == "__main__":
    input = input()
    tokens = input.split()
    n = int(tokens[0])
    m = int(tokens[1])
    res = fibonacci(n, m)
    print(res)
