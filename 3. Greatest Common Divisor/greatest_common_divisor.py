def calculate_gcd(a, b):
    if b == 0:
        return a
    rem = a % b
    return calculate_gcd(b, rem)


if __name__ == "__main__":
    a = int(input())
    b = int(input())
    res = calculate_gcd(a, b)
    print(res)