from itertools import permutations

def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def find_prime_combination(digits):
    permutations_list = permutations(digits)
    for perm in permutations_list:
        number = int(''.join(map(str, perm)))
        if is_prime(number):
            return number
    return None

while True:
    # 5つの数字をユーザーに入力させる
    try:
        input_digits = [int(input(f"数字{i+1}: ")) for i in range(5)]
    except ValueError:
        print("数字を正しく入力してください。")
        continue

    result = find_prime_combination(input_digits)

    if result is not None:
        print(f"素数: {result}")
        break
    else:
        print("素数が見つかりませんでした。再度数字を入力してください。")
