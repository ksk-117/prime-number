import pygame
import sys
import random

# Pygameの初期化
pygame.init()

# ウィンドウのサイズ
width, height = 970, 600

# ウィンドウの作成
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Prime Number Game")

# 画像のロード
background_image = pygame.image.load('background.jpg')

# フォントの設定
font_size = 36
font = pygame.font.Font(None, font_size)

# 長方形のサイズと配置
rect_width, rect_height = 140, 210
margin = 40
shadow_offset = 10  # 影のオフセット

# ランダムな数字の生成と変数への保存
def generate_card():
    return random.randint(1, 9)

# カードの初期配置
card1 = generate_card()
card2 = generate_card()
card3 = generate_card()
card4 = generate_card()
card5 = generate_card()

# ターゲット
five_1 = int(f"{card1}{card2}{card3}{card4}{card5}")
four_1 = int(f"{card1}{card2}{card3}{card4}")
four_2 = int(f"{card2}{card3}{card4}{card5}")
three_1 = int(f"{card1}{card2}{card3}")
three_2 = int(f"{card2}{card3}{card4}")
three_3 = int(f"{card3}{card4}{card5}")
two_1 = int(f"{card1}{card2}")
two_2 = int(f"{card2}{card3}")
two_3 = int(f"{card3}{card4}")
two_4 = int(f"{card4}{card5}")   #  & card1~5

# 素数かどうかを判定する関数
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

# 初期のポイント
score = 0
score_element = []

# クリックされたカードの位置を保存する変数
clicked_card1 = None

# 右クリックで引き直す機能の追加
redraw_count = 5  # 引き直し回数の初期設定

# カードの描画関数
def draw_cards():
    # 長方形の描画（影を含む）
    num_rectangles = 5  # 5つの長方形を配置することを想定
    total_width = num_rectangles * rect_width + (num_rectangles - 1) * margin
    start_x = (width - total_width) // 2
    start_y = height - 30 - rect_height  # 下部から30px上に配置

    for i in range(num_rectangles):
        rect_x = start_x + i * (rect_width + margin)

        # 影の描画
        shadow_rect = pygame.Rect(rect_x + shadow_offset, start_y + shadow_offset, rect_width, rect_height)
        pygame.draw.rect(screen, (0, 0, 0, 100), shadow_rect)  # 半透明度を持つ黒い色で描画

        # カードの描画
        card = globals()[f"card{i + 1}"]  # card1, card2, ..., card5
        card_rect = pygame.Rect(rect_x, start_y, rect_width, rect_height)
        pygame.draw.rect(screen, (255, 255, 255), card_rect)  # カードの描画

        # 数字の描画
        text = font.render(str(card), True, (0, 0, 0))  # テキストを描画
        text_rect = text.get_rect(center=(rect_x + rect_width // 2, start_y + rect_height // 2))
        screen.blit(text, text_rect)

# ゲームループ
while True:
    # イベントの処理
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:  # 左クリック
                clicked_pos = event.pos

                # カードがクリックされた場合の処理
                clicked_card = find_clicked_card(clicked_pos)

                if clicked_card:
                    if clicked_card1 is None:
                        # 1回目のクリックならclicked_card1に保存
                        clicked_card1 = clicked_card
                    else:
                        # 2回目のクリックで、保存されたカードと入れ替え
                        clicked_card2 = clicked_card
                        card1_name = f"card{clicked_card1}"
                        card2_name = f"card{clicked_card2}"

                        # カードの位置を入れ替え
                        swap_cards(card1_name, card2_name)

                        # クリックされたカードの位置をリセット
                        clicked_card1 = None

                        # スコア計算
                        score = 0
                        add_score()
                        print(f"Score: {score}")

        # キーボードの特定のキーが押された場合
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                # スペースキーが押されたらスコアを計算
                score = 0
                add_score()
                print(f"Score: {score}")

                # 引き直し回数の表示
                print(f"Redraw Count: {redraw_count}")

    # 画面のクリア
    screen.blit(background_image, (0, 0))

    # カードの描画
    draw_cards()

    # ポイント表示
    score_text = font.render(f"Score: {score}", True, (255, 255, 255))
    screen.blit(score_text, (10, 10))

    # リストの要素を描画
    y_position = 110
    for item in score_element:
        score_element_text = font.render(str(item), True, (255, 255, 255))
        screen.blit(score_element_text, (10, y_position))
        y_position += 40

    # 引き直し回数の表示
    redraw_count_text = font.render(f"Redraw Count: {redraw_count}", True, (255, 255, 255))
    screen.blit(redraw_count_text, (10, 70))

    # 画面の更新
    pygame.display.flip()

