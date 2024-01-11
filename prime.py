import random

# カードの属性
card_types = ['A', 'B', 'C', 'D', 'E']

# カードの数字
all_numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
deck = []
selected_cards = []
first_clicked_card = None

# 山札からカードを引く
def draw_cards():
    global deck, selected_cards, first_clicked_card
    # 山札を初期化
    deck = all_numbers.copy()
    selected_cards = []

    # 山札から5枚引く
    for i in range(5):
        random_index = random.randint(0, len(deck) - 1)
        drawn_card = deck.pop(random_index)
        card_type = card_types[i % len(card_types)]
        selected_cards.append({'number': drawn_card, 'type': card_type})

    display_cards()

# カードの表示
def display_cards():
    print("選択したカード:")
    for card in selected_cards:
        print(f"{card['number']} {card['type']}")
    update_result()

# カードの選択
def select_card(number, index):
    global first_clicked_card
    if first_clicked_card is None:
        # 一回目のクリック
        first_clicked_card = {'number': number, 'index': index}
    else:
        # 二回目のクリック
        swap_cards(first_clicked_card['index'], index)
        first_clicked_card = None
    display_cards()

# カードの入れ替え
def swap_cards(index1, index2):
    selected_cards[index1], selected_cards[index2] = selected_cards[index2], selected_cards[index1]

# 結果の更新
def update_result():
    selected_number = ''.join(str(card['number']) for card in selected_cards)
    print(f"選択した数字: {selected_number}")

# 数字を作り、素数か判定する
def arrange_cards():
    selected_number = ''.join(str(card['number']) for card in selected_cards)
    result = "素数です" if is_prime(int(selected_number)) else "素数ではありません"
    print(result)

# 素数かどうかの判定
def is_prime(num):
    if num < 2:
        return False
    for i in range(2, num):
        if num % i == 0:
            return False
    return True

# ゲームのメインループ
while True:
    print("\n1. 山札からカードを引く")
    print("2. カードを入れ替える")
    print("3. 素数か判定する")
    print("4. ゲーム終了")
    
    choice = input("選択してください (1-4): ")

    if choice == '1':
        draw_cards()
    elif choice == '2':
        index = int(input("入れ替えるカードの番号を選択してください (0-4): "))
        select_card(selected_cards[index]['number'], index)
    elif choice == '3':
        arrange_cards()
    elif choice == '4':
        print("ゲームを終了します。")
        break
    else:
        print("無効な選択です。再度選択してください。")
