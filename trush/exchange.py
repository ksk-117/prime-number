import pygame
import random

# Pygameの初期化
pygame.init()

# ウィンドウのサイズと色の設定
WIDTH, HEIGHT = 800, 600
BG_COLOR = (255, 255, 255)
CARD_COLOR = (200, 200, 200)
CARD_FONT = pygame.font.SysFont(None, 48)

# ゲームの初期化
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Card Game")
clock = pygame.time.Clock()

cards = [random.randint(1, 9) for _ in range(5)]
selected_card_indices = []

def draw_cards():
    for i, card in enumerate(cards):
        pygame.draw.rect(screen, CARD_COLOR, (50 + i * 150, 250, 100, 150))
        text = CARD_FONT.render(str(card), True, (0, 0, 0))
        screen.blit(text, (100 + i * 150 - text.get_width() // 2, 325 - text.get_height() // 2))

def draw_selected_cards():
    for i, index in enumerate(selected_card_indices):
        pygame.draw.rect(screen, CARD_COLOR, (50 + i * 150, 50, 100, 150))
        text = CARD_FONT.render(str(cards[index]), True, (0, 0, 0))
        screen.blit(text, (100 + i * 150 - text.get_width() // 2, 125 - text.get_height() // 2))

def main():
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    x, y = event.pos
                    if 50 < y < 200:
                        index = (x - 50) // 150
                        if index < len(cards):
                            selected_card_indices.append(index)
                            if len(selected_card_indices) == 2:
                                # 入れ替え
                                cards[selected_card_indices[0]], cards[selected_card_indices[1]] = (
                                    cards[selected_card_indices[1]],
                                    cards[selected_card_indices[0]],
                                )
                                selected_card_indices.clear()

        screen.fill(BG_COLOR)
        draw_cards()
        draw_selected_cards()
        
        # 5桁の値を表示
        result_value = int("".join(map(str, cards)))
        result_text = CARD_FONT.render(str(result_value), True, (0, 0, 0))
        screen.blit(result_text, (WIDTH // 2 - result_text.get_width() // 2, 500 - result_text.get_height() // 2))
        
        pygame.display.flip()
        clock.tick(30)

    pygame.quit()

if __name__ == "__main__":
    main()
