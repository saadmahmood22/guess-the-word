import pygame
import random
import sys

pygame.init()

pygame.display.set_caption("Guess the Word")

white = (255, 255, 255)
black = (0, 0, 0)

width = 1050
height = 400

screen = pygame.display.set_mode((width, height))

word_list = ["acres", "adult", "advice", "arrangement", "attempt", "august", "autumn", "border", "breeze", "brick",
             "calm", "canal", "casey", "cast", "chose", "claws", "coach", "constantly", "contrast", "cookies",
             "customs", "damage", "danny", "deeply", "depth", "discussion", "doll", "donkey", "egypt", "ellen",
             "essential", "exchange", "exist", "explanation", "facing", "film", "finest", "fireplace", "floating",
             "folks", "fort", "garage", "grabbed", "grandmother", "habit", "happily", "harry", "heading", "hunter",
             "illinois", "image", "independent", "instant", "january", "kids", "label", "lee", "lungs", "manufacturing",
             "martin", "mathematics", "melted", "memory", "mill", "mission", "monkey", "mountain", "mysterious",
             "neighborhood", "norway", "nuts", "occasionally", "official", "ourselves", "palace", "pennsylvania",
             "philadelphia", "plates", "poetry", "policeman", "positive", "possibly", "practical", "pride", "promised",
             "recall", "relationship", "remarkable", "require", "rhyme", "rocky", "rubbed", "rush", "sale",
             "satellites", "satisfied", "scared", "selection", "shake", "shaking", "shallow", "shout", "silly",
             "simplest", "slight", "slip", "slope", "soap", "solar", "species", "spin", "stiff", "swung", "tales",
             "thumb", "tobacco", "toy", "trap", "treated", "tune", "university", "vapor", "vessels", "wealth", "wolf",
             "zoo"]

word_list = sorted(word_list, key = lambda x: x[2])

word = word_list[random.randint(0, len(word_list) - 1)]

blank_word = ""
for letter in word:
    blank_word += "_ "
blank_word = blank_word.strip()

wrong_letters_text = "wrong letters:"

wrong_letters = ""

Font = pygame.font.SysFont("monospace", 37)

game_over = False

def wrong_letter_update(w_l, letter):
    w_l += letter
    return w_l

def blank_update(w, b_w, letter):
    i = 0
    while i < len(w):
        if letter == w[i]:
            b_w = b_w[:i * 2] + letter + b_w[i * 2 + 1:]
            i += 1
        elif b_w[i * 2] == w[i]:
            b_w = b_w[:i * 2] + w[i] + b_w[i * 2 + 1:]
            i += 1
        else:
            i += 1
    return b_w

def game_end(s):
    if s[-1] == "0":
        return "Game Over!"
    else:
        return ""

def any_key_to_exit(l, b_w):
    if l[-1] == "0" or "_" not in b_w:
        return "Press any key to exit"
    else:
        return ""

def win(b_w):
    if "_" not in b_w:
        return "Congrats, You Win!"
    else:
        return ""

while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if len(wrong_letters) == 5 or "_" not in blank_word:
                sys.exit()
            else:
                if 97 <= event.key <= 122:
                    guess = chr(event.key)
                    if guess in blank_word:
                        pass
                    elif guess in wrong_letters:
                        pass
                    elif guess in word:
                        blank_word = blank_update(word, blank_word, guess)
                    else:
                        wrong_letters = wrong_letter_update(wrong_letters, guess)

    screen.fill(white)
    wrong_letters_display = Font.render(wrong_letters_text, True, black)
    screen.blit(wrong_letters_display, (10, height - 50))
    wrong_letter_string = Font.render(wrong_letters, True, black)
    screen.blit(wrong_letter_string, (320, height - 50))
    blanks = Font.render(blank_word, True, black)
    screen.blit(blanks, (int(width / 3), int(height / 2.5)))
    gtw = Font.render("Guess the Word:", True, black)
    screen.blit(gtw, (10, int(height / 2.5)))
    lives_string = "lives " + str(5 - len(wrong_letters))
    lives = Font.render(lives_string, True, black)
    screen.blit(lives, (int(width - 200), int(height - 50)))
    g_o = Font.render(game_end(lives_string), True, black)
    screen.blit(g_o, (int(width / 2.5), int(height / 20)))
    akte_loss = Font.render(any_key_to_exit(lives_string, blank_word), True, black)
    screen.blit(akte_loss, (int(width / 3.5), int(height / 7)))
    win_text = Font.render(win(blank_word), True, black)
    screen.blit(win_text, (int(width / 3.1), int(height / 20)))
    akte_win = Font.render(any_key_to_exit(lives_string, blank_word), True, black)
    screen.blit(akte_win, (int(width / 3.5), int(height / 7)))
    pygame.display.update()