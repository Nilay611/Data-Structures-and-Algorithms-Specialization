from max_pairwise_product import pairwise_product
from random import randint


def pairwise_product_test(numbers, n):
    max_product = 0
    for i in range(n):
        for j in range(i + 1, n):
            max_product = max(max_product, numbers[i] * numbers[j])
    return max_product


def unit_test():
    while True:
        n = randint(2, 100)
        numbers = list()
        for _ in range(n):
            numbers.append(randint(1, 100000))
        test_res = pairwise_product_test(numbers, n)
        real_res = pairwise_product(numbers, n)
        if test_res == real_res:
            print("OK...")
        else:
            print(numbers)
            print(test_res, real_res)
            break


if __name__ == "__main__":
    unit_test()
