import pygame
import sys
import random

pygame.init()

# 画面設定
width, height = 970, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Prime Number Game")
background_image = pygame.image.load('background.jpg')
scene = 0

font_path = "TEMPSITC.ttf"
font_path1 = "ipaexg.ttf"
font_size = 36
font = pygame.font.Font(font_path, font_size)
title_font_size = 72
title_font = pygame.font.Font(font_path, title_font_size)
play_font_size = 36
play_font = pygame.font.Font(font_path, play_font_size)
explain_font_size = 18
explain_font = pygame.font.Font(font_path1, explain_font_size)
number_font_size = 72
number_font = pygame.font.Font(font_path, number_font_size)

score = 0
score_element = []
keep_A = None
redraw_count = 5
rect_width, rect_height = 140, 210
margin = 40
shadow_offset = 10

# ボタンの設定
button_width, button_height = 200, 50
button_color = (100, 100, 100)
button_hover_color = (150, 150, 150)

def draw_button(screen, text, position, size, font, button_color, hover_color, action=None):
    button_rect = pygame.Rect(position, size)
    mouse_pos = pygame.mouse.get_pos()
    button_hover = button_rect.collidepoint(mouse_pos)

    if button_hover:
        pygame.draw.rect(screen, hover_color, button_rect)
    else:
        pygame.draw.rect(screen, button_color, button_rect)

    text_surface = font.render(text, True, (255, 255, 255))
    text_rect = text_surface.get_rect(center=button_rect.center)
    screen.blit(text_surface, text_rect)

    if button_hover and pygame.mouse.get_pressed()[0] == 1:
        if action is not None:
            action()

# ボタンがクリックされたときの処理
def score_table_button_action():
    global scene
    scene = 2

def judge_button_action():
    global scene
    scene = 3


############タイトル################################################################################
while scene == 0:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    screen.blit(background_image, (0, 0))

    title_text = title_font.render("Prime Number Poker", True, (255, 255, 255))
    title_rect = title_text.get_rect(center=(width / 2, height / 5))
    screen.blit(title_text, title_rect)

    explain_text_lines = [
        "このゲームは5つの数字を好きな順番に並べ替えて素数を作って高得点を目指すゲームです。",
        "",
        "左クリックで1回目にクリックしたカードと2回目にクリックしたカードを交換することができます。",
        "また、右クリックで新しいカードに変更できます。",
    ]
    
    play_text = play_font.render("--Space to PLAY!--", True, (255, 255, 255))
    play_rect = play_text.get_rect(center=(width / 2, 3*height / 5))
    screen.blit(play_text, play_rect)
    
    y_offset = 0
    for line in explain_text_lines:
        line_text = explain_font.render(line, True, (255, 255, 255))
        line_rect = line_text.get_rect(center=(width / 2, height / 3 + y_offset))
        screen.blit(line_text, line_rect)
        y_offset += 20

    draw_button(screen, "Score Table", (width / 2 - button_width / 2, height / 2 + 140), (button_width, button_height),
                font, button_color, button_hover_color, score_table_button_action)

    pygame.display.flip()
    # スペースキーの処理
    keys = pygame.key.get_pressed()
    if keys[pygame.K_SPACE]:
        scene = 1


############タイトル終了################################################################################

############点数表################################################################################
while scene == 2:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    screen.blit(background_image, (0, 0))  # 背景画像を描画

    title_text = title_font.render("Score Table", True, (255, 255, 255))
    title_rect = title_text.get_rect(center=(width / 2, height / 5))
    screen.blit(title_text, title_rect)
    
    explain_text_lines = [
        "5桁の素数…10000点",
        "4桁の素数…2000点",
        "3桁の素数…1000点",
        "2桁の素数…500点",
        "1桁の素数…200点",
        "(以下未実装)",
    ]
    y_offset = 0
    for line in explain_text_lines:
        line_text = explain_font.render(line, True, (255, 255, 255))
        line_rect = line_text.get_rect(center=(width / 2, height / 3 + y_offset))
        screen.blit(line_text, line_rect)
        y_offset += 20  # 行ごとに20ピクセル下にずらす
    
    play_text = play_font.render("--Space to PLAY!--", True, (255, 255, 255))
    play_rect = play_text.get_rect(center=(width / 2, 4*height / 5))
    screen.blit(play_text, play_rect)

    pygame.display.flip()

    # スペースキーの処理
    keys = pygame.key.get_pressed()
    if keys[pygame.K_SPACE]:
        scene = 1

############点数表終了################################################################################

##########   関数の定義   ################################################################################################

# ランダムな数字の生成と変数への保存
def generate_card():
    return random.randint(1, 9)

# 素数かどうかを判定する関数
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True


# カードの引き直し関数
def redraw_card(card_name):
    global redraw_count  # redraw_countをグローバル変数として宣言
    if redraw_count > 0:
        globals()[card_name] = generate_card()
        redraw_count -= 1


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
def swap_cards():
    globals()[card1_name], globals()[card2_name] = globals()[card2_name], globals()[card1_name]

# スコア計算関数
def add_score():
    global score
    global card1, card2, card3, card4, card5  
    
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

    targets =  [five_1, 
                four_1, four_2, 
                three_1, three_2, three_3, 
                two_1, two_2, two_3, two_4, 
                card1, card2, card3, card4, card5]
    
    for target in targets:
        if is_prime(target):
            score_element.append(target)   #スコアの要素に追加
            #桁数に応じて点数アップ
            if target == five_1:
                score += 10000
            if target in [four_1, four_2]:
                score += 2000
            if target in [three_1, three_2, three_3]:
                score += 1000
            if target in [two_1, two_2, two_3, two_4]:
                score += 500
            if target in [card1, card2, card3, card4, card5]:
                score += 200
            #ボーナス点数アップ（双子素数、グロタンディーク素数などを追加したい）
                

# カードの描画関数
def draw_cards():
    num_rectangles = 5  # 5つのカード
    total_width = num_rectangles * rect_width + (num_rectangles - 1) * margin
    start_x = (width - total_width) // 2
    start_y = height - 30 - rect_height  # 下部から30px上に配置

    for i in range(num_rectangles):
        rect_x = start_x + i * (rect_width + margin)

        # 影の描画
        shadow_rect = pygame.Rect(rect_x + shadow_offset, start_y + shadow_offset, rect_width, rect_height)
        pygame.draw.rect(screen, (0, 0, 0, 100), shadow_rect)  

        # カードの描画
        card = globals()[f"card{i + 1}"]  # card1, card2, ..., card5
        card_rect = pygame.Rect(rect_x, start_y, rect_width, rect_height)
        pygame.draw.rect(screen, (255, 255, 255), card_rect)  

        # 数字の描画
        number = number_font.render(str(card), True, (0, 0, 0))  # テキストを描画
        number_rect = number.get_rect(center=(rect_x + rect_width // 2, start_y + rect_height // 2))
        screen.blit(number, number_rect)

# カードの初期配布
card1 = generate_card()
card2 = generate_card()
card3 = generate_card()
card4 = generate_card()
card5 = generate_card()

cards = []     #リストに保管
cards.extend([card1, card2, card3, card4, card5])

############メインループ#######################################################################
while scene == 1:
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
                    if keep_A is None:
                        # 1回目のクリックならkeep_Aに保存
                        clicked_card1 = clicked_card
                        keep_A = globals()["card" + str(clicked_card1)]

                    else:
                        # 2回目のクリックで、保存されたカードと入れ替え
                        clicked_card2 = clicked_card
                        keep_B = globals()["card" + str(clicked_card2)]
                        cards[clicked_card2 - 1] = keep_A
                        cards[clicked_card1 - 1] = keep_B
                        card1_name = f"card{clicked_card1}"
                        card2_name = f"card{clicked_card2}"
                        # カードの位置を入れ替え
                        swap_cards()

                        # クリックされたカードの位置をリセット
                        keep_A = None

            elif event.button == 3:  # 右クリック
                clicked_pos = event.pos

                # 右クリックされた位置にあるカードを特定
                clicked_card = find_clicked_card(clicked_pos)

                if clicked_card:
                    card_name = f"card{clicked_card}"
                    redraw_card(card_name)

    # スコアを計算
    score = 0
    score_element = []
    add_score()

    #########画面の描写#########
    
    screen.blit(background_image, (0, 0)) # 画面のクリア

    draw_cards()                          # カードの描画

    draw_button(screen, "Judge", (width - button_width - margin, margin), (button_width, button_height),
                font, button_color, button_hover_color, judge_button_action)


    score_text = font.render(f"Score: {score}", True, (255, 255, 255))# ポイント表示
    screen.blit(score_text, (10, 10))

    y_position = 110                      # リストの要素を描画
    for item in score_element:
        score_element_text = font.render(str(item), True, (255, 255, 255))
        screen.blit(score_element_text, (10, y_position))
        y_position += 40

    redraw_count_text = font.render(f"Redraw Count: {redraw_count}", True, (255, 255, 255))# 引き直し回数の表示
    screen.blit(redraw_count_text, (10, 70))

    # 画面の更新
    pygame.display.flip()


#############メインループ終了###################################################################
        

############結果################################################################################
while scene == 3:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    screen.blit(background_image, (0, 0))  # 背景画像を描画

    title_text = title_font.render(f'Result… {score}pt', True, (255, 255, 255))
    title_rect = title_text.get_rect(center=(width / 2, height / 6))
    screen.blit(title_text, title_rect)
    

    y_position = 150  # リストの要素を描画
    for item in score_element:
        score_element_text = font.render(str(item), True, (255, 255, 255))
        screen.blit(score_element_text, (width / 2, y_position))
        y_position += 40
    
    play_text = play_font.render("--Space to END--", True, (255, 255, 255))
    play_rect = play_text.get_rect(center=(width / 2, 6*height / 7))
    screen.blit(play_text, play_rect)

    pygame.display.flip()
    keys = pygame.key.get_pressed()     # スペースキーで終了
    if keys[pygame.K_SPACE]:
        pygame.quit()

############結果終了################################################################################
