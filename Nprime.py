import pygame
import sys

# Pygameの初期化
pygame.init()

# ウィンドウのサイズ
width, height = 970, 600

# ウィンドウの作成
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("My Card Game")

# 長方形のサイズと配置
rect_width, rect_height = 140, 210
margin = 40

# ゲームループ
while True:
    # イベントの処理
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # 画面のクリア
    screen.fill((255, 255, 255))  # 白色で塗りつぶす

    # 長方形の描画
    num_rectangles = 5  # 5つの長方形を配置することを想定
    total_width = num_rectangles * rect_width + (num_rectangles - 1) * margin
    start_x = (width - total_width) // 2
    start_y = height - 30 - rect_height  # 下部から30px上に配置

    for i in range(num_rectangles):
        rect_x = start_x + i * (rect_width + margin)
        pygame.draw.rect(screen, (255, 255, 255), (rect_x, start_y, rect_width, rect_height), 2)

    # 画面の更新
    pygame.display.flip()
