from itertools import permutations

def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def find_prime_combinations(digits):
    prime_combinations = set()
    for length in range(1, len(digits) + 1):
        for perm in permutations(digits, length):
            number = int(''.join(map(str, perm)))
            if is_prime(number):
                prime_combinations.add(number)
    return sorted(prime_combinations)

try:
    input_numbers = input("任意の整数を入力してください: ")
    number = [int(digit) for digit in str(input_numbers)]

    result = []

    for num_of_digits in range(len(number), len(number) + 1):
        prime_combinations = find_prime_combinations(number[:num_of_digits])

        if prime_combinations:
            result.extend(prime_combinations)

    if result:
        result_str = ', '.join(map(str, result))
        print("素数:")
        current_line_length = 0

        for prime in result_str.split(', '):
            prime_length = len(prime)
            if current_line_length + prime_length > 100:  # 40文字を超えたら改行
                print()
                current_line_length = 0
            print(prime, end=' ')
            current_line_length += prime_length + 1  # 1は空白の長さ

    else:
        print("素数が見つかりませんでした。")

except ValueError:
    print("数字を正しく入力してください。")
