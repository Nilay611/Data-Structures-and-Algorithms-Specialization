def calculate_gcd(a, b):
    if b == 0:
        return a
    rem = a % b
    return calculate_gcd(b, rem)


if __name__ == "__main__":
    input = input()
    tokens = input.split()
    a = int(tokens[0])
    b = int(tokens[1])
    res = calculate_gcd(a, b)
    print(res)