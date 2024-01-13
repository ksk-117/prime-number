import pygame
import sys
import random

# Pygameの初期化
pygame.init()

# ウィンドウのサイズ
width, height = 970, 600

# ウィンドウの作成
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("My Card Game")

# 画像のロード
background_image = pygame.image.load('background.jpg')

# フォントの設定
font_size = 72
font = pygame.font.Font(None, font_size)

# 長方形のサイズと配置
rect_width, rect_height = 140, 210
margin = 40
shadow_offset = 10  # 影のオフセット

# ランダムな数字の生成と関数への保存
def generate_card():
    return random.randint(1, 9)

card1 = generate_card()
card2 = generate_card()
card3 = generate_card()
card4 = generate_card()
card5 = generate_card()

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

# クリックされたカードの位置を保存する変数
clicked_card1 = None

# クリックされた位置にあるカードを特定する関数
def find_clicked_card(pos):
    num_rectangles = 5
    total_width = num_rectangles * rect_width + (num_rectangles - 1) * margin
    start_x = (width - total_width) // 2
    start_y = height - 30 - rect_height

    for i in range(num_rectangles):
        rect_x = start_x + i * (rect_width + margin)
        card_rect = pygame.Rect(rect_x, start_y, rect_width, rect_height)

        if card_rect.collidepoint(pos):
            return i + 1  # カード番号を返す

    return None  # クリックされた位置にカードがない場合はNoneを返す

# カードの位置を入れ替える関数
def swap_cards(card1_name, card2_name):
    globals()[card1_name], globals()[card2_name] = globals()[card2_name], globals()[card1_name]

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

    # 画面のクリア
    screen.blit(background_image, (0, 0))

    # カードの描画
    draw_cards()

    # 画面の更新
    pygame.display.flip()
