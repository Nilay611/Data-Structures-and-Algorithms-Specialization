def pairwise_product(numbers, n):
    max_number_index = -1
    second_max_number_index = -1
    for i in range(n):
        if max_number_index == -1 or numbers[i] > numbers[max_number_index]:
            max_number_index = i
    for j in range(n):
        if j != max_number_index and (second_max_number_index == -1 or numbers[j] > numbers[second_max_number_index]):
            second_max_number_index = j
    return numbers[max_number_index] * numbers[second_max_number_index]


if __name__ == "__main__":
    n = int(input())
    numbers = list(map(int, input().split()))
    res = pairwise_product(numbers, n)
    print(res)
