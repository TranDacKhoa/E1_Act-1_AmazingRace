import pygame, sys, time
import random
import openpyxl
from pygame.locals import *
from random import randint
from tkinter import *
from time import sleep

WINDOWWIDTH = 1200  # Chiều dài cửa sổ
WINDOWHEIGHT = 686  # Chiều cao cửa sổ

WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)
YELLOW = (255, 255, 0)
BLUE = (0, 0, 255)

pygame.init()
root = Tk()

# Xác định FPS
FPS = 80
fpsClock = pygame.time.Clock()

window = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT))
pygame.display.set_caption('Do_An_Nhom_1')
Font_Winner = pygame.font.SysFont('consolas', 30)
Font_Pause = pygame.font.SysFont('consolas', 40)
Font_sans20 = pygame.font.SysFont('sans', 20)
Font_sans30 = pygame.font.SysFont('sans', 30)
Font_sans40 = pygame.font.SysFont('sans', 40)

Mouse_x = 0
Mouse_y = 0

CharacterName1 = ['Cowboy', 'Cow Girl', 'Dinosaurs', 'Ninja', 'Gold Dog', 'Grey Cat']
CharacterName2 = ['Dac Khoa', 'Quang Khoa', 'An Nguyen', 'Gia Long', 'Khoi Nguyen', 'Dinh Loc']

Speed = 10

click = 0

def Timing(Timing):
    for i in range(1, Timing + 1):
        time.sleep(1)
        if i == Timing:
            return i

class Login():
    def __init__(Login):
        Login.start = True
        Login.text_user_start = False
        Login.text_pass_start = False
        Login.print_sai_mk = False
        Login.print_uer_not_exist = False
        Login.surface = pygame.image.load('login.png')
        Login.surface1 = pygame.image.load('login(1).png')
        Login.surface2 = pygame.image.load('login(2).png')
        Login.surface = pygame.transform.scale(Login.surface, (WINDOWWIDTH, WINDOWHEIGHT))
        Login.surface1 = pygame.transform.scale(Login.surface1, (WINDOWWIDTH, WINDOWHEIGHT))
        Login.surface2 = pygame.transform.scale(Login.surface2, (WINDOWWIDTH, WINDOWHEIGHT))
        Login.surface_user_not_exist = Font_sans40.render('user not exist', True, RED)
        Login.surface_sai_mk = Font_sans40.render('incorrect password', True, RED)
        Login.pos_user = pygame.Rect(540, 250, 450, 60)
        Login.pos_pass = pygame.Rect(540, 340, 450, 60)
        Login.pos_sign_in = pygame.Rect(490, 427, 176, 63)
        Login.pos_register = pygame.Rect(835, 520, 115, 35)
        Login.File = 'login.xlsx'
        Login.Load = openpyxl.load_workbook(Login.File)
        Login.Sheet = Login.Load['Sheet1']
        Login.so_tk = 1
        Login.text_user = ''
        Login.text_password = ''
        Login.text_sao = ''

    def Get_value(self, pos):
        Login.Load.close()
        return Login.Sheet[pos].value

    def Update_value(self, pos, value):
        print('dia chi update', pos)
        Login.Sheet[pos].value = value
        Login.Load.save(Login.File)
        Login.Load.close()

    def Check_user(self, user):
        Login.so_tk = Login.Get_value('D1')
        for i in range(1, Login.so_tk + 1):
            Check_user = Login.Get_value('A' + str(i))
            if user == Check_user:
                return True
            elif i == Login.so_tk:
                return False

    def Check_pass(self, password):
        Login.so_tk = Login.Get_value('D1')
        for i in range(1, Login.so_tk + 1):
            Check_pass = Login.Get_value('B' + str(i))
            if password == Check_pass:
                return True
            elif i == Login.so_tk:
                return False

    def Find_user(self, user):
        for i in range(1, Login.so_tk + 1):
            Check_user = Login.Get_value('A' + str(i))
            print('do hang', i)
            if user == Check_user:
                print('tim thay user o hang', i)
                return i

    def draw(Login):
        window.blit(Login.surface, (0, 0))
        if Login.text_user_start:
            window.blit(Login.surface1, (0, 0))
        if Login.text_pass_start:
            window.blit(Login.surface2, (0, 0))
        Login.surface_user = Font_sans40.render(Login.text_user, True, BLACK)
        Login.surface_sao = Font_sans40.render(Login.text_sao, True, BLACK)
        window.blit(Login.surface_user, (600, 250))
        window.blit(Login.surface_sao, (600, 340))

        if Login.print_sai_mk:
            window.blit(Login.surface_sai_mk, (435, 516))
        if Login.print_uer_not_exist:
            window.blit(Login.surface_user_not_exist, (480, 516))

    def Login(Login):

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    if Login.pos_user.collidepoint(event.pos):
                        Login.text_user_start = True
                        Login.text_pass_start = False
                    if Login.pos_pass.collidepoint(event.pos):
                        Login.text_pass_start = True
                        Login.text_user_start = False
                    if Login.pos_register.collidepoint(event.pos):
                        Register.start = True
                        Login.start = False
                    if Login.pos_sign_in.collidepoint(event.pos):
                        if Login.Check_user(Login.text_user):
                            if Login.Check_pass(Login.text_password):
                                print('dang nhap thanh cong')
                                Money.existing = Login.Get_value('C' + str(Login.Find_user(Login.text_user)))
                                Start.start = True
                                Login.start = False
                                Login.print_sai_mk = False
                                Login.print_uer_not_exist = False
                            else:
                                Login.print_sai_mk = True
                                Login.print_uer_not_exist = False
                                print('sai mat khau')
                        else:
                            Login.print_uer_not_exist = True
                            Login.print_sai_mk = False
                            print('ten dang nhap khong ton tai')

            if event.type == pygame.KEYDOWN:
                if Login.text_user_start:
                    if event.key == pygame.K_BACKSPACE:
                        Login.text_user = Login.text_user[:-1]
                    else:
                        Login.text_user += event.unicode

                if Login.text_pass_start:
                    if event.key == pygame.K_BACKSPACE:
                        Login.text_password = Login.text_password[:-1]
                        Login.text_sao = Login.text_sao[:-1]
                    elif event.unicode:
                        Login.text_password += event.unicode
                        Login.text_sao += '*'

                if event.key == pygame.K_RETURN:
                    if Login.Check_user(Login.text_user):
                        if Login.Check_pass(Login.text_password):
                            print('dang nhap thanh cong')
                            Money.existing = Login.Get_value('C' + str(Login.Find_user(Login.text_user)))
                            Start.start = True
                            Login.start = False
                            Login.print_sai_mk = False
                            Login.print_uer_not_exist = False
                        else:
                            Login.print_sai_mk = True
                            Login.print_uer_not_exist = False
                            print('sai mat khau')
                    else:
                        Login.print_uer_not_exist = True
                        Login.print_sai_mk = False
                        print('ten dang nhap khong ton tai')
Login = Login()


class Register():
    def __init__(Register):
        Register.start = False
        Register.tao_tk = False
        Register.nhap_mk = False
        Register.khac_mk_retype = False
        Register.user_exist = False
        Register.surface_tao_tk = Font_sans40.render('Create Account Success', True, RED)
        Register.surface_nhap_mk = Font_sans40.render('Please enter a password', True, RED)
        Register.surface_khac_mk_retype = Font_sans40.render("That password doesn't match. Try again", True, RED)
        Register.surface_user_exist = Font_sans40.render("Account already exists", True, RED)
        Register.surface1 = pygame.image.load('register.png')
        Register.surface2 = pygame.image.load('register(1).png')
        Register.surface3 = pygame.image.load('register(2).png')
        Register.surface4 = pygame.image.load('register(3).png')
        Register.surface1 = pygame.transform.scale(Register.surface1, (WINDOWWIDTH, WINDOWHEIGHT))
        Register.surface2 = pygame.transform.scale(Register.surface2, (WINDOWWIDTH, WINDOWHEIGHT))
        Register.surface3 = pygame.transform.scale(Register.surface3, (WINDOWWIDTH, WINDOWHEIGHT))
        Register.surface4 = pygame.transform.scale(Register.surface4, (WINDOWWIDTH, WINDOWHEIGHT))
        Register.pos_quit = pygame.Rect(905, 160, 45, 40)
        Register.pos_user = pygame.Rect(540, 240, 370, 50)
        Register.pos_pass = pygame.Rect(540, 320, 370, 50)
        Register.pos_retype = pygame.Rect(540, 405, 370, 50)
        Register.enter = pygame.Rect(500, 480, 195, 60)
        Register.text_user = ''
        Register.text_password = ''
        Register.text_retype = ''
        Register.text_sao1= ''
        Register.text_sao2 = ''
        Register.text_user_start = False
        Register.text_password_start = False
        Register.text_retype_start = False
    def Register(Register):
        if Register.start:
            window.blit(Register.surface1, (0, 0))
            if Register.text_user_start:
                window.blit(Register.surface2, (0, 0))
            if Register.text_password_start:
                window.blit(Register.surface3, (0, 0))
            if Register.text_retype_start:
                window.blit(Register.surface4, (0, 0))
            Register.surface_user = Font_sans40.render(Register.text_user, True, BLACK)
            Register.surface_sao1 = Font_sans40.render(Register.text_sao1, True, BLACK)
            Register.surface_sao2 = Font_sans40.render(Register.text_sao2, True, BLACK)
            window.blit(Register.surface_user, (610, 240))
            window.blit(Register.surface_sao1, (610, 320))
            window.blit(Register.surface_sao2, (610, 405))
            if Register.tao_tk:
                window.blit(Register.surface_tao_tk, (425,560))
            if Register.nhap_mk:
                window.blit(Register.surface_nhap_mk, (425, 560))
            if Register.khac_mk_retype:
                window.blit(Register.surface_khac_mk_retype, (325, 560))
            if Register.user_exist:
                window.blit(Register.surface_user_exist, (445, 560))

            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()

                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        if Register.pos_quit.collidepoint(event.pos):
                            Register.start = False
                            Login.start = True
                        if Register.pos_user.collidepoint(event.pos):
                            Register.text_user_start = True
                            Register.text_password_start = False
                            Register.text_retype_start = False
                        if Register.pos_pass.collidepoint(event.pos):
                            Register.text_user_start = False
                            Register.text_password_start = True
                            Register.text_retype_start = False
                        if Register.pos_retype.collidepoint(event.pos):
                            Register.text_user_start = False
                            Register.text_password_start = False
                            Register.text_retype_start = True

                        if Register.enter.collidepoint(event.pos):
                            if not Login.Check_user(Register.text_user):
                                if Register.text_password != '' and Register.text_password == Register.text_retype:
                                    Login.Update_value('A' + str(Login.so_tk + 1), Register.text_user)
                                    Login.Update_value('B' + str(Login.so_tk + 1), Register.text_password)
                                    Login.so_tk += 1
                                    Login.Update_value('D1', Login.so_tk)
                                    Login.Update_value('C' + str(Login.Find_user(Register.text_user)), int(0))
                                    Register.tao_tk = True
                                    Register.nhap_mk = False
                                    Register.khac_mk_retype = False
                                    Register.user_exist = False
                                    print('tao tai khoan thanh cong')
                                elif Register.text_password == '' or Register.text_retype == '':
                                    Register.tao_tk = False
                                    Register.nhap_mk = True
                                    Register.khac_mk_retype = False
                                    Register.user_exist = False
                                    print('vui long nhap mat khau cua ban')
                                elif Register.text_password != Register.text_retype:
                                    Register.tao_tk = False
                                    Register.nhap_mk = False
                                    Register.khac_mk_retype = True
                                    Register.user_exist = False
                                    print('mat khau va retype khac nhau')
                            else:
                                Register.tao_tk = False
                                Register.nhap_mk = False
                                Register.khac_mk_retype = False
                                Register.user_exist = True
                                print('ten dang nhap da ton tai')

                if event.type == pygame.KEYDOWN:
                    if Register.text_user_start:
                        if event.key == pygame.K_BACKSPACE:
                            Register.text_user = Register.text_user[:-1]
                        else:
                            Register.text_user += event.unicode

                    if Register.text_password_start:
                        if event.key == pygame.K_BACKSPACE:
                            Register.text_password = Register.text_password[:-1]
                            Register.text_sao1 = Register.text_sao1[:-1]
                        elif event.unicode:
                            Register.text_password += event.unicode
                            Register.text_sao1 += '*'

                    if Register.text_retype_start:
                        if event.key == pygame.K_BACKSPACE:
                            Register.text_retype = Register.text_password[:-1]
                            Register.text_sao2 = Register.text_sao2[:-1]
                        elif event.unicode:
                            Register.text_retype += event.unicode
                            Register.text_sao2 += '*'

                    if event.key == pygame.K_RETURN:
                        if not Login.Check_user(Register.text_user):
                            if Register.text_password != '' and Register.text_password == Register.text_retype:
                                Login.Update_value('A' + str(Login.so_tk + 1), Register.text_user)
                                Login.Update_value('B' + str(Login.so_tk + 1), Register.text_password)
                                Login.so_tk += 1
                                Login.Update_value('D1', Login.so_tk)
                                Login.Update_value('C' + str(Login.Find_user(Register.text_user)), int(0))
                                Register.tao_tk = True
                                Register.nhap_mk = False
                                Register.khac_mk_retype = False
                                Register.user_exist = False
                                print('tao tai khoan thanh cong')
                            elif Register.text_password == '' or Register.text_retype == '':
                                Register.tao_tk = False
                                Register.nhap_mk = True
                                Register.khac_mk_retype = False
                                Register.user_exist = False
                                print('vui long nhap mat khau cua ban')
                            elif Register.text_password != Register.text_retype:
                                Register.tao_tk = False
                                Register.nhap_mk = False
                                Register.khac_mk_retype = True
                                Register.user_exist = False
                                print('mat khau va retype khac nhau')
                        else:
                            Register.tao_tk = False
                            Register.nhap_mk = False
                            Register.khac_mk_retype = False
                            Register.user_exist = True
                            print('ten dang nhap da ton tai')
Register = Register()


# surface start
class Start():

    def __init__(Start):
        Start.x = 0  # hoành độ của giao diện start
        Start.y = 0  # tung độ của giao diện surface
        Start.dem1 = 0
        Start.start = False
        # tạo surface của start
        Start.surface = pygame.image.load('Start.png')
        # resize theo kích thước cửa sổ game
        Start.surface = pygame.transform.scale(Start.surface, (WINDOWWIDTH, WINDOWHEIGHT))
        Start.Start_rect = pygame.Rect(457, 167, 298, 131)
        Start.MiniGame_rect = pygame.Rect(457, 350, 298, 131)
        Start.shop_button = pygame.Rect(490, 582, 90, 68)
        Start.sound = pygame.mixer.music.load('Christmas Verse LOOP WITHOUT MELODY.mp3')

    # vẽ Start lên surface vừa tạo
    def draw(Start):
        window.blit(Start.surface, (Start.x, Start.y))
        Start.Mouse_x, Start.Mouse_y = pygame.mouse.get_pos()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                if Start.Start_rect.collidepoint((Start.Mouse_x, Start.Mouse_y)):
                    Start.start = False
                    Map_Select.start = True
                if Start.MiniGame_rect.collidepoint((Start.Mouse_x, Start.Mouse_y)):
                    Start.start = False
                    Game_Select.start = True
                if Start.shop_button.collidepoint((Mouse_x, Mouse_y)):
                    Shop.start = True
                    Start.start = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                Login.start = True
                Start.start = False
        Bet.__init__()
        Cowboy.__init__()
        Cowgirl.__init__()
        Dinosaurs.__init__()
        Ninja.__init__()
        Gold_Dog.__init__()
        Grey_Cat.__init__()
        Dac_Khoa.__init__()
        Quang_Khoa.__init__()
        An_Nguyen.__init__()
        Gia_Long.__init__()
        Khoi_Nguyen.__init__()
        Dinh_Loc.__init__()
        Winner.__init__()


Start = Start()


class Shop():
    def __init__(Shop):
        Shop.start = False
        Shop.surface = pygame.image.load('SHOP.png')
        Shop.surface = pygame.transform.scale(Shop.surface, (WINDOWWIDTH, WINDOWHEIGHT))
        Shop.red = 2
        Shop.gold = 2
        Shop.blue = 2
        Shop.red_surface = pygame.image.load('bua do.png')
        Shop.gold_surface = pygame.image.load('bua vang.png')
        Shop.blue_surface = pygame.image.load('bua xanh.png')
        Shop.font = pygame.font.SysFont('sans', 20)
        Shop.price_red = 25
        Shop.price_gold = 5
        Shop.price_blue = 50
        Shop.buy_red = pygame.Rect(225, 252, 125, 38)
        Shop.buy_gold = pygame.Rect(540, 252, 125, 38)
        Shop.buy_blue = pygame.Rect(860, 252, 125, 38)
        Shop.home = pygame.Rect(277, 572, 111, 87)
        Shop.back = pygame.Rect(804, 572, 111, 87)

    def draw(Shop):
        if Shop.start:
            window.blit(Shop.surface, (0, 0))
            window.blit(Shop.red_surface, (260, 145))
            window.blit(Shop.gold_surface, (575, 145))
            window.blit(Shop.blue_surface, (895, 145))

            red_existing = Shop.font.render(str(Shop.red), True, BLACK)
            gold_existing = Shop.font.render(str(Shop.gold), True, BLACK)
            blue_existing = Shop.font.render(str(Shop.blue), True, BLACK)
            window.blit(red_existing, (342, 225))
            window.blit(gold_existing, (657, 225))
            window.blit(blue_existing, (978, 225))

            price_red = Shop.font.render(str(Shop.price_red) + '$', True, BLACK)
            price_gold = Shop.font.render(str(Shop.price_gold) + '$', True, BLACK)
            price_blue = Shop.font.render(str(Shop.price_blue) + '$', True, BLACK)
            window.blit(price_red, (225, 225))
            window.blit(price_gold, (540, 225))
            window.blit(price_blue, (860, 225))

            Mouse_x, Mouse_y = pygame.mouse.get_pos()

            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        if Shop.buy_red.collidepoint(Mouse_x, Mouse_y):
                            if Money.existing >= Shop.price_red:
                                Money.existing -= Shop.price_red
                                Shop.red += 1
                        if Shop.buy_gold.collidepoint(Mouse_x, Mouse_y):
                            if Money.existing >= Shop.price_gold:
                                Money.existing -= Shop.price_gold
                                Shop.gold += 1
                        if Shop.buy_blue.collidepoint(Mouse_x, Mouse_y):
                            if Money.existing >= Shop.price_blue:
                                Money.existing -= Shop.price_blue
                                Shop.blue += 1
                        if Shop.home.collidepoint(Mouse_x, Mouse_y):
                            Shop.start = False
                            Start.start = True


Shop = Shop()


class Game_Select():

    def __init__(Game_Select):
        Game_Select.start = False
        Game_Select.surface = pygame.image.load('Mini Game.png')
        Game_Select.surface = pygame.transform.scale(Game_Select.surface, (WINDOWWIDTH, WINDOWHEIGHT))
        Game_Select.Snake = pygame.Rect(300, 400, 175, 70)
        Game_Select.Flappy = pygame.Rect(735, 400, 175, 70)
        Game_Select.Back = pygame.Rect(800, 580, 110, 70)

    def draw(Game_Select):
        window.blit(Game_Select.surface, (0, 0))
        if event.type == pygame.MOUSEBUTTONDOWN:
            Game_Select.Mouse_x, Game_Select.Mouse_y = pygame.mouse.get_pos()
            if event.button == 1:
                if Game_Select.Snake.collidepoint(Game_Select.Mouse_x, Game_Select.Mouse_y):
                    Snake.start = True
                    Game_Select.start = False
                if Game_Select.Flappy.collidepoint(Game_Select.Mouse_x, Game_Select.Mouse_y):
                    Flappy.start = True
                    Game_Select.start = False
                if Game_Select.Back.collidepoint(Game_Select.Mouse_x, Game_Select.Mouse_y):
                    Start.start = True
                    Game_Select.start = False


Game_Select = Game_Select()


class Snake():
    def __init__(Snake):
        Snake.start = False
        Snake.clock = pygame.time.Clock()
        Snake.snakes = [[5, 10]]
        Snake.direction = "right"

        Snake.apple = [randint(0, 19), randint(0, 19)]
        Snake.font_small = pygame.font.SysFont('sans', 20)
        Snake.font_big = pygame.font.SysFont('sans', 50)
        Snake.score = 0
        Snake.pausing = False

    def draw(Snake):
        if Snake.start:
            Snake.clock.tick(60)
            window.fill(WHITE)

            tail_x = Snake.snakes[0][0]
            tail_y = Snake.snakes[0][1]

            for snake in Snake.snakes:
                pygame.draw.rect(window, GREEN, (300 + snake[0] * 30, 43 + snake[1] * 30, 30, 30))

            pygame.draw.rect(window, RED, (300 + Snake.apple[0] * 30, 43 + Snake.apple[1] * 30, 30, 30))

            pygame.draw.rect(window, BLACK, (257, 0, 43, WINDOWHEIGHT))
            pygame.draw.rect(window, BLACK, (900, 0, 43, WINDOWHEIGHT))
            pygame.draw.rect(window, BLACK, (300, 0, 600, 43))
            pygame.draw.rect(window, BLACK, (300, 643, 600, 43))

            if Snake.snakes[-1][0] == Snake.apple[0] and Snake.snakes[-1][1] == Snake.apple[1]:
                Snake.snakes.insert(0, [tail_x, tail_y])
                Snake.apple = [randint(0, 19), randint(0, 19)]
                Snake.score += 1
                Money.existing += 1

            # check crash with edge
            if Snake.snakes[-1][0] < 0 or Snake.snakes[-1][0] > 19 or Snake.snakes[-1][1] < 0 or Snake.snakes[-1][
                1] > 19:
                Snake.pausing = True

                # Draw score
            score_txt = Snake.font_small.render("Score: " + str(Snake.score), True, BLACK)
            window.blit(score_txt, (5, 5))

            # Snake move
            if Snake.pausing == False:
                if Snake.direction == "right":
                    Snake.snakes.append([Snake.snakes[-1][0] + 1, Snake.snakes[-1][1]])
                    Snake.snakes.pop(0)
                if Snake.direction == "left":
                    Snake.snakes.append([Snake.snakes[-1][0] - 1, Snake.snakes[-1][1]])
                    Snake.snakes.pop(0)
                if Snake.direction == "up":
                    Snake.snakes.append([Snake.snakes[-1][0], Snake.snakes[-1][1] - 1])
                    Snake.snakes.pop(0)
                if Snake.direction == "down":
                    Snake.snakes.append([Snake.snakes[-1][0], Snake.snakes[-1][1] + 1])
                    Snake.snakes.pop(0)

                    # check crash with body
            for i in range(len(Snake.snakes) - 1):
                if Snake.snakes[-1][0] == Snake.snakes[i][0] and Snake.snakes[-1][1] == Snake.snakes[i][1]:
                    Snake.pausing = True

                    # Draw game over
            if Snake.pausing:
                game_over_txt = Snake.font_big.render("Game over, score: " + str(Snake.score), True, BLACK)
                press_space_txt = Snake.font_big.render("Press Space to continue", True, BLACK)
                window.blit(game_over_txt, (350, 200))
                window.blit(press_space_txt, (350, 300))

            time.sleep(0.1)

            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP and Snake.direction != "down":
                        Snake.direction = "up"
                    if event.key == pygame.K_DOWN and Snake.direction != "up":
                        Snake.direction = "down"
                    if event.key == pygame.K_LEFT and Snake.direction != "right":
                        Snake.direction = "left"
                    if event.key == pygame.K_RIGHT and Snake.direction != "left":
                        Snake.direction = "right"
                    if event.key == pygame.K_SPACE and Snake.pausing == True:
                        Snake.pausing = False
                        Snake.snakes = [[5, 10]]
                        Snake.apple = [randint(0, 19), randint(0, 19)]
                        Snake.score = 0
                    if event.key == pygame.K_ESCAPE:
                        Snake.start = False
                        # Start.start = False
                        Game_Select.start = True
                        Snake.start = False


Snake = Snake()


class Flappy():
    def __init__(Flappy):
        Flappy.start = False
        Flappy.clock = pygame.time.Clock()
        Flappy.running = True

        Flappy.HEIGHT = 686
        Flappy.WIDTH = 400

        Flappy.TUBE_WIDTH = 50
        Flappy.TUBE_VELOCITY = 3
        Flappy.TUBE_GAP = 200

        Flappy.tube1_x = 1100
        Flappy.tube2_x = 1300
        Flappy.tube3_x = 1500

        Flappy.tube1_height = randint(100, 400)
        Flappy.tube2_height = randint(100, 400)
        Flappy.tube3_height = randint(100, 400)

        Flappy.BIRD_X = 450
        Flappy.bird_y = 400
        Flappy.BIRD_WIDTH = 35
        Flappy.BIRD_HEIGHT = 35

        Flappy.bird_drop_velocity = 0
        Flappy.GRAVITY = 0.5

        Flappy.score = 0
        Flappy.font = pygame.font.SysFont('sans', 20)

        Flappy.tube1_pass = False
        Flappy.tube2_pass = False
        Flappy.tube3_pass = False

        Flappy.pausing = False

        Flappy.backround_image = pygame.image.load("bg.png")
        Flappy.backround_image = pygame.transform.scale(Flappy.backround_image, (WINDOWWIDTH, WINDOWHEIGHT))
        Flappy.bird_image = pygame.image.load("redbird-midflap.png")
        Flappy.bird_image = pygame.transform.scale(Flappy.bird_image, (Flappy.BIRD_WIDTH, Flappy.BIRD_HEIGHT))

    def draw(Flappy):
        if Flappy.start:

            window.blit(Flappy.backround_image, (0, 0))

            Flappy.clock.tick(60)
            tube1_rect = pygame.draw.rect(window, BLUE, (Flappy.tube1_x, 0, Flappy.TUBE_WIDTH, Flappy.tube1_height))
            tube2_rect = pygame.draw.rect(window, BLUE, (Flappy.tube2_x, 0, Flappy.TUBE_WIDTH, Flappy.tube2_height))
            tube3_rect = pygame.draw.rect(window, BLUE, (Flappy.tube3_x, 0, Flappy.TUBE_WIDTH, Flappy.tube3_height))

            tube1_rect_inv = pygame.draw.rect(window, BLUE, (
                Flappy.tube1_x, Flappy.tube1_height + Flappy.TUBE_GAP, Flappy.TUBE_WIDTH,
                Flappy.HEIGHT - Flappy.tube1_height - Flappy.TUBE_GAP))
            tube2_rect_inv = pygame.draw.rect(window, BLUE, (
                Flappy.tube2_x, Flappy.tube2_height + Flappy.TUBE_GAP, Flappy.TUBE_WIDTH,
                Flappy.HEIGHT - Flappy.tube2_height - Flappy.TUBE_GAP))
            tube3_rect_inv = pygame.draw.rect(window, BLUE, (
                Flappy.tube3_x, Flappy.tube3_height + Flappy.TUBE_GAP, Flappy.TUBE_WIDTH,
                Flappy.HEIGHT - Flappy.tube3_height - Flappy.TUBE_GAP))

            Flappy.tube1_x = Flappy.tube1_x - Flappy.TUBE_VELOCITY
            Flappy.tube2_x = Flappy.tube2_x - Flappy.TUBE_VELOCITY
            Flappy.tube3_x = Flappy.tube3_x - Flappy.TUBE_VELOCITY

            sand_rect = pygame.draw.rect(window, YELLOW, (400, 670, 400, 18))

            sky_rect = pygame.draw.rect(window, BLUE, (400, 0, 400, 5))

            bird_rect = window.blit(Flappy.bird_image, (Flappy.BIRD_X, Flappy.bird_y))

            Flappy.bird_y += Flappy.bird_drop_velocity
            Flappy.bird_drop_velocity += Flappy.GRAVITY

            if Flappy.tube1_x < -Flappy.TUBE_WIDTH + 400:
                Flappy.tube1_x = 950
                Flappy.tube1_height = randint(100, 400)
                Flappy.tube1_pass = False
            if Flappy.tube2_x < -Flappy.TUBE_WIDTH + 400:
                Flappy.tube2_x = 950
                Flappy.tube2_pass = False
                Flappy.tube2_height = randint(100, 400)
            if Flappy.tube3_x < -Flappy.TUBE_WIDTH + 400:
                Flappy.tube3_x = 950
                Flappy.tube3_height = randint(100, 400)
                Flappy.tube3_pass = False

            pygame.draw.rect(window, WHITE, (0, 0, 400, WINDOWWIDTH))
            pygame.draw.rect(window, WHITE, (800, 0, 400, WINDOWWIDTH))
            score_txt = Flappy.font.render("Score: " + str(Flappy.score), True, BLACK)
            window.blit(score_txt, (405, 5))

            if Flappy.tube1_x + Flappy.TUBE_WIDTH <= Flappy.BIRD_X and Flappy.tube1_pass == False:
                Flappy.score += 1
                Money.existing += 1
                Flappy.tube1_pass = True
            if Flappy.tube2_x + Flappy.TUBE_WIDTH <= Flappy.BIRD_X and Flappy.tube2_pass == False:
                Flappy.score += 1
                Money.existing += 1
                Flappy.tube2_pass = True
            if Flappy.tube3_x + Flappy.TUBE_WIDTH <= Flappy.BIRD_X and Flappy.tube3_pass == False:
                Flappy.score += 1
                Money.existing += 1
                Flappy.tube3_pass = True

            for tube in [tube1_rect, tube2_rect, tube3_rect, tube1_rect_inv, tube2_rect_inv, tube3_rect_inv, sand_rect,
                         sky_rect]:
                if bird_rect.colliderect(tube):
                    Flappy.TUBE_VELOCITY = 0
                    Flappy.bird_drop_velocity = 0
                    game_over_txt = Flappy.font.render("GAME OVER! Score: " + str(Flappy.score), True, BLACK)
                    window.blit(game_over_txt, (550, 300))
                    press_space_txt = Flappy.font.render("Press SPACE to Continue", True, BLACK)
                    window.blit(press_space_txt, (550, 350))
                    Flappy.pausing = True

            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        if Flappy.pausing:
                            Flappy.bird_y = 400
                            Flappy.TUBE_VELOCITY = 3
                            Flappy.tube1_x = 1100
                            Flappy.tube2_x = 1300
                            Flappy.tube3_x = 1500
                            Flappy.score = 0
                            Flappy.pausing = False

                        Flappy.bird_drop_velocity = 0
                        Flappy.bird_drop_velocity -= 10
                    if event.key == pygame.K_ESCAPE:
                        Flappy.start = False
                        # Start.start = False
                        Game_Select.start = True
                        Flappy.running = False

                        # pygame.display.flip()


Flappy = Flappy()


class Map_Select():
    def __init__(Map_Select):
        Map_Select.x = 0
        Map_Select.start = False

        Map_Select.surface = pygame.image.load('MapSelect.png')
        Map_Select.surface = pygame.transform.scale(Map_Select.surface, (WINDOWWIDTH, WINDOWHEIGHT))
        Map_Select.Back = pygame.Rect(820, 590, 75, 60)

    def draw(Map_Select):
        window.blit(Map_Select.surface, (Map_Select.x, 0))
        Map_1 = pygame.Rect(262, 125, 250, 190)
        Map_2 = pygame.Rect(690, 125, 250, 190)
        Map_3 = pygame.Rect(262, 348, 250, 190)
        Map_4 = pygame.Rect(690, 348, 250, 190)

        if event.type == pygame.MOUSEBUTTONUP:
            if event.button == 1:
                Map_Select.Mouse_x, Map_Select.Mouse_y = pygame.mouse.get_pos()
                if Map_Select.Back.collidepoint((Map_Select.Mouse_x, Map_Select.Mouse_y)):
                    Start.start = True
                    Map_Select.start = False
                if Map_1.collidepoint((Map_Select.Mouse_x, Map_Select.Mouse_y)):
                    Character_Select.start = True
                    Map_Select.start = False
                    map.Sanhok = True
                if Map_2.collidepoint((Map_Select.Mouse_x, Map_Select.Mouse_y)):
                    Character_Select.start = True
                    Map_Select.start = False
                    map.Vilkendi = True
                if Map_3.collidepoint((Map_Select.Mouse_x, Map_Select.Mouse_y)):
                    Character_Select.start = True
                    Map_Select.start = False
                    map.Mirama = True
                if Map_4.collidepoint((Map_Select.Mouse_x, Map_Select.Mouse_y)):
                    Character_Select.start = True
                    Map_Select.start = False
                    map.Sanhok_night = True


Map_Select = Map_Select()


class Character_Select():
    def __init__(Character_Select):
        Character_Select.x = 0
        Character_Select.start = False
        Character_Select.start1 = True
        Character_Select.start2 = False

        Character_Select.Mouse_x = 0
        Character_Select.Mouse_y = 0

        Character_Select.choice = 0

        Character_Select.surface1 = pygame.image.load('CharacterSelect1.png')
        Character_Select.surface1 = pygame.transform.scale(Character_Select.surface1, (WINDOWWIDTH, WINDOWHEIGHT))
        Character_Select.surface2 = pygame.image.load('CharacterSelect2.png')
        Character_Select.surface2 = pygame.transform.scale(Character_Select.surface2, (WINDOWWIDTH, WINDOWHEIGHT))

        Character_Select.Right = pygame.Rect(1076, 300, 91, 74)
        Character_Select.Left = pygame.Rect(40, 300, 91, 74)
        CharacterName1 = ['Cowboy', 'Cow Girl', 'Dinosaurs', 'Ninja', 'Gold Dog', 'Grey Cat']
        CharacterName2 = ['An Nguyen', 'Dac Khoa', 'Quang Khoa', 'Dinh Loc', 'Gia Long', 'Khoi Nguyen']

    def draw(Character_Select):
        if Character_Select.start1:
            window.blit(Character_Select.surface1, (Character_Select.x, 0))
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    Character_Select.Mouse_x, Character_Select.Mouse_y = pygame.mouse.get_pos()
                    if Character_Select.Right.collidepoint((Character_Select.Mouse_x, Character_Select.Mouse_y)):
                        Character_Select.start2 = True
                        Character_Select.start1 = False
        if Character_Select.start2:
            window.blit(Character_Select.surface2, (Character_Select.x, 0))
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    Character_Select.Mouse_x, Character_Select.Mouse_y = pygame.mouse.get_pos()
                    if Character_Select.Left.collidepoint((Character_Select.Mouse_x, Character_Select.Mouse_y)):
                        Character_Select.start1 = True
                        Character_Select.start2 = False

        Character_1 = pygame.Rect(224, 120, 193, 200)
        Character_2 = pygame.Rect(503, 120, 193, 200)
        Character_3 = pygame.Rect(808, 120, 193, 200)
        Character_4 = pygame.Rect(224, 339, 193, 200)
        Character_5 = pygame.Rect(503, 339, 193, 200)
        Character_6 = pygame.Rect(808, 339, 193, 200)
        Character_Select.back = pygame.Rect(822, 580, 96, 70)

        if Character_Select.start == True:
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    Character_Select.Mouse_x, Character_Select.Mouse_y = pygame.mouse.get_pos()
                    if Character_Select.back.collidepoint((Character_Select.Mouse_x, Character_Select.Mouse_y)):
                        Map_Select.start = True
                        Character_Select.start = False
                    if Character_1.collidepoint((Character_Select.Mouse_x, Character_Select.Mouse_y)):
                        print("Nhan vat 1")
                        Character_Select.choice = 1
                        Character_Select.start = False
                        Bet.start = True
                    if Character_2.collidepoint((Character_Select.Mouse_x, Character_Select.Mouse_y)):
                        print("Nhan vat 2")
                        Character_Select.choice = 2
                        Character_Select.start = False
                        Bet.start = True
                    if Character_3.collidepoint((Character_Select.Mouse_x, Character_Select.Mouse_y)):
                        print("Nhan vat 3")
                        Character_Select.choice = 3
                        Character_Select.start = False
                        Bet.start = True
                    if Character_4.collidepoint((Character_Select.Mouse_x, Character_Select.Mouse_y)):
                        print("Nhan vat 4")
                        Character_Select.choice = 4
                        Character_Select.start = False
                        Bet.start = True
                    if Character_5.collidepoint((Character_Select.Mouse_x, Character_Select.Mouse_y)):
                        print("Nhan vat 5")
                        Character_Select.choice = 5
                        Character_Select.start = False
                        Bet.start = True
                    if Character_6.collidepoint((Character_Select.Mouse_x, Character_Select.Mouse_y)):
                        print("Nhan vat 6")
                        Character_Select.choice = 6
                        Character_Select.start = False
                        Bet.start = True


Character_Select = Character_Select()


class Bet():
    def __init__(Bet):
        Bet.start = False
        Bet.x = 0
        Bet.y = 0
        Bet.surface = pygame.image.load('BET.png')
        Bet.surface = pygame.transform.scale(Bet.surface, (WINDOWWIDTH, WINDOWHEIGHT))
        Bet.minus = pygame.Rect(420, 270, 50, 20)
        Bet.plus = pygame.Rect(740, 250, 45, 50)
        Bet.confirm = pygame.Rect(530, 360, 150, 50)
        Bet.home = pygame.Rect(500, 450, 60, 50)
        Bet.back = pygame.Rect(630, 450, 60, 50)
        Bet.amount = 0

    def draw(Bet):
        Bet.surface_amount = Font_sans30.render('' + str(Bet.amount), True, BLACK)
        window.blit(Bet.surface, (Bet.x, Bet.y))
        window.blit(Bet.surface_amount, (580, 265))
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    if Bet.plus.collidepoint(event.pos) and int(Money.existing) > 0:
                        Bet.amount += 1
                        Money.existing -= 1
                    if Bet.minus.collidepoint(event.pos) and int(Bet.amount) > 0:
                        Bet.amount -= 1
                        Money.existing += 1
                    if Bet.confirm.collidepoint(event.pos) and int(Bet.amount) > 0:
                        Ready.start = True
                        Bet.start = False
                    if Bet.home.collidepoint(event.pos):
                        Start.start = True
                        Bet.start = False
                    if Bet.back.collidepoint(event.pos):
                        Character_Select.start = True
                        Bet.start = False
            if event.type == pygame.KEYDOWN:
                if (event.key == pygame.K_RIGHT or event.key == pygame.K_UP) and int(Money.existing) > 0:
                    Bet.amount += 1
                    Money.existing -= 1
                if (event.key == pygame.K_LEFT or event.key == pygame.K_DOWN) and int(Bet.amount) > 0:
                    Bet.amount -= 1
                    Money.existing += 1
                if event.key == pygame.K_RETURN and int(Bet.amount) > 0:
                    Ready.start = True
                    Bet.start = False
                if event.key == pygame.K_ESCAPE:
                    Character_Select.start = True
                    Bet.start = False
            if event.type == QUIT:
                Money.existing += Bet.amount
                Login.Update_value('C' + str(Login.Find_user(Login.text_user)), int(Money.existing))
                pygame.quit()
                sys.exit()

Bet = Bet()


class Ready():
    def __init__(Ready):
        Ready.start = False
        Ready.x = WINDOWWIDTH / 2
        Ready.y = WINDOWHEIGHT / 4
        Ready.secs3 = pygame.image.load('3.png')
        Ready.secs2 = pygame.image.load('2.png')
        Ready.secs1 = pygame.image.load('1.png')
        Ready.go = pygame.image.load('GO.png')
        Ready.sound = pygame.mixer.Sound('countdown.wav')

    def draw(Ready):
        pygame.mixer.music.stop()
        # pygame.mixer.pause()
        pygame.mixer.Sound.play(Ready.sound)
        secs = [Ready.secs3, Ready.secs2, Ready.secs1, Ready.go]
        if event.type == pygame.MOUSEBUTTONUP and Ready.start:
            for sec in secs:
                map.draw()
                if Character_Select.start1:
                    Gold_Dog.dem2 = 1
                    Grey_Cat.dem2 = 1
                    Dinosaurs.dem2 = 1
                    Cowboy.dem2 = 1
                    Cowgirl.dem2 = 1
                    Ninja.dem2 = 1

                    Gold_Dog.draw()
                    Grey_Cat.draw()
                    Dinosaurs.draw()
                    Cowboy.draw()
                    Cowgirl.draw()
                    Ninja.draw()
                    window.blit(sec, (Ready.x, Ready.y))
                    pygame.display.update()

                if Character_Select.start2:
                    An_Nguyen.dem2 = 1
                    Dac_Khoa.dem2 = 1
                    Quang_Khoa.dem2 = 1
                    Dinh_Loc.dem2 = 1
                    Khoi_Nguyen.dem2 = 1
                    Gia_Long.dem2 = 1

                    An_Nguyen.draw()
                    Dac_Khoa.draw()
                    Quang_Khoa.draw()
                    Dinh_Loc.draw()
                    Khoi_Nguyen.draw()
                    Gia_Long.draw()
                    window.blit(sec, (Ready.x, Ready.y))
                    pygame.display.update()
                time.sleep(1)
            Ready.start = False
            Game.start = True


Ready = Ready()


# surface map
class map():
    def __init__(map):
        map.x = 0  # vị trí của map
        # tạo surface và thêm map
        map.start = False
        map.Sanhok = False
        map.Vilkendi = False
        map.Mirama = False
        map.Sanhok_night = False
        map.surface1 = pygame.image.load('Sanhok.png')
        map.surface2 = pygame.image.load('Vilkendi.png')
        map.surface3 = pygame.image.load('Mirama.png')
        map.surface4 = pygame.image.load('Sanhok-night.png')
        map.surface1 = pygame.transform.scale(map.surface1, (WINDOWWIDTH, WINDOWHEIGHT))
        map.surface2 = pygame.transform.scale(map.surface2, (WINDOWWIDTH, WINDOWHEIGHT))
        map.surface3 = pygame.transform.scale(map.surface3, (WINDOWWIDTH, WINDOWHEIGHT))
        map.surface4 = pygame.transform.scale(map.surface4, (WINDOWWIDTH, WINDOWHEIGHT))
        # ve map len surface

    def draw(map):
        if map.Sanhok == True:
            window.blit(map.surface1, (map.x, 0))

        if map.Vilkendi == True:
            window.blit(map.surface2, (map.x, 0))

        if map.Mirama == True:
            window.blit(map.surface3, (map.x, 0))

        if map.Sanhok_night == True:
            window.blit(map.surface4, (map.x, 0))


map = map()


class Gold_Dog():
    def __init__(Gold_Dog):
        Gold_Dog.dem = 0
        Gold_Dog.dem2 = 1
        Gold_Dog.x = 125  # vị trí của ông già Noel
        Gold_Dog.y = 426
        # tạo surface và thêm hình golddog
        Gold_Dog.surface1 = pygame.image.load('golddog1.png')
        Gold_Dog.surface2 = pygame.image.load('golddog2.png')
        Gold_Dog.surface3 = pygame.image.load('golddog3.png')
        Gold_Dog.surface4 = pygame.image.load('golddog4.png')
        Gold_Dog.surface5 = pygame.image.load('golddog5.png')
        Gold_Dog.surface6 = pygame.image.load('golddog6.png')
        Gold_Dog.surface7 = pygame.image.load('golddog7.png')
        Gold_Dog.surface8 = pygame.image.load('golddog8.png')
        Gold_Dog.surface_win = pygame.image.load('Gold_dog_win.png')
        Gold_Dog.surface_lose = pygame.image.load('Gold_doglose.png')

    # gọi Noel.surface
    def draw(Gold_Dog):
        if Gold_Dog.x + 170 < WINDOWWIDTH:
            if Gold_Dog.dem2 == 1:
                window.blit(Gold_Dog.surface1, (Gold_Dog.x, Gold_Dog.y))
            if Gold_Dog.dem2 == 2:
                window.blit(Gold_Dog.surface2, (Gold_Dog.x, Gold_Dog.y))
            if Gold_Dog.dem2 == 3:
                window.blit(Gold_Dog.surface3, (Gold_Dog.x, Gold_Dog.y))
            if Gold_Dog.dem2 == 4:
                window.blit(Gold_Dog.surface4, (Gold_Dog.x, Gold_Dog.y))
            if Gold_Dog.dem2 == 5:
                window.blit(Gold_Dog.surface5, (Gold_Dog.x, Gold_Dog.y))
            if Gold_Dog.dem2 == 6:
                window.blit(Gold_Dog.surface6, (Gold_Dog.x, Gold_Dog.y))
            if Gold_Dog.dem2 == 7:
                window.blit(Gold_Dog.surface7, (Gold_Dog.x, Gold_Dog.y))
            if Gold_Dog.dem2 == 8:
                window.blit(Gold_Dog.surface8, (Gold_Dog.x, Gold_Dog.y))

            if Gold_Dog.dem2 < 8:
                Gold_Dog.dem2 += 1
            else:
                Gold_Dog.dem2 = 1
        elif Winner.xep_hang_so[0] == 5:
            window.blit(Gold_Dog.surface_win, (Gold_Dog.x, Gold_Dog.y))
        else:
            window.blit(Gold_Dog.surface_lose, (Gold_Dog.x, Gold_Dog.y))

    def update(Gold_Dog):
        if Gold_Dog.x + 170 < WINDOWWIDTH:
            Gold_Dog.x += random.randrange(1, Speed, 1)
        else:
            Gold_Dog.x = WINDOWWIDTH - 170


Gold_Dog = Gold_Dog()


class Grey_Cat():

    def __init__(Grey_Cat):
        Grey_Cat.x = 125
        Grey_Cat.y = 530
        Grey_Cat.dem = 0
        Grey_Cat.dem2 = 1
        Grey_Cat.surface1 = pygame.image.load('greycat1.png')
        Grey_Cat.surface2 = pygame.image.load('greycat2.png')
        Grey_Cat.surface3 = pygame.image.load('greycat3.png')
        Grey_Cat.surface4 = pygame.image.load('greycat4.png')
        Grey_Cat.surface5 = pygame.image.load('greycat5.png')
        Grey_Cat.surface6 = pygame.image.load('greycat6.png')
        Grey_Cat.surface7 = pygame.image.load('greycat7.png')
        Grey_Cat.surface8 = pygame.image.load('greycat8.png')
        Grey_Cat.surface_win = pygame.image.load('Grey_cat_win.png')
        Grey_Cat.surface_lose = pygame.image.load('Greycat_lose.png')

    def draw(Grey_Cat):
        if Grey_Cat.x + 170 < WINDOWWIDTH:
            if Grey_Cat.dem2 == 1:
                window.blit(Grey_Cat.surface1, (Grey_Cat.x, Grey_Cat.y))
            if Grey_Cat.dem2 == 2:
                window.blit(Grey_Cat.surface2, (Grey_Cat.x, Grey_Cat.y))
            if Grey_Cat.dem2 == 3:
                window.blit(Grey_Cat.surface3, (Grey_Cat.x, Grey_Cat.y))
            if Grey_Cat.dem2 == 4:
                window.blit(Grey_Cat.surface4, (Grey_Cat.x, Grey_Cat.y))
            if Grey_Cat.dem2 == 5:
                window.blit(Grey_Cat.surface5, (Grey_Cat.x, Grey_Cat.y))
            if Grey_Cat.dem2 == 6:
                window.blit(Grey_Cat.surface6, (Grey_Cat.x, Grey_Cat.y))
            if Grey_Cat.dem2 == 7:
                window.blit(Grey_Cat.surface7, (Grey_Cat.x, Grey_Cat.y))
            if Grey_Cat.dem2 == 8:
                window.blit(Grey_Cat.surface8, (Grey_Cat.x, Grey_Cat.y))

            if Grey_Cat.dem2 < 8:
                Grey_Cat.dem2 += 1
            else:
                Grey_Cat.dem2 = 1

        elif Winner.xep_hang_so[0] == 6:
            window.blit(Grey_Cat.surface_win, (Grey_Cat.x, Grey_Cat.y))
        else:
            window.blit(Grey_Cat.surface_lose, (Grey_Cat.x, Grey_Cat.y))

    def update(Grey_Cat):

        if Grey_Cat.x + 170 < WINDOWWIDTH:
            Grey_Cat.x += random.randrange(1, Speed, 1)
        else:
            Grey_Cat.x = WINDOWWIDTH - 170


Grey_Cat = Grey_Cat()


class Dinosaurs():

    def __init__(Dinosaurs):
        Dinosaurs.x = 125
        Dinosaurs.y = 225
        Dinosaurs.dem_amulet = 0
        Dinosaurs.dem = 0
        Dinosaurs.dem2 = 1
        Dinosaurs.surface1 = pygame.image.load('Dinosaurs1.png')
        Dinosaurs.surface2 = pygame.image.load('Dinosaurs2.png')
        Dinosaurs.surface3 = pygame.image.load('Dinosaurs3.png')
        Dinosaurs.surface4 = pygame.image.load('Dinosaurs4.png')
        Dinosaurs.surface5 = pygame.image.load('Dinosaurs5.png')
        Dinosaurs.surface6 = pygame.image.load('Dinosaurs6.png')
        Dinosaurs.surface7 = pygame.image.load('Dinosaurs7.png')
        Dinosaurs.surface8 = pygame.image.load('Dinosaurs8.png')
        Dinosaurs.surface_win = pygame.image.load('Dinasours_win.png')
        Dinosaurs.surface_lose = pygame.image.load('Dinasourslose.png')

    def draw(Dinosaurs):
        if Dinosaurs.x + 170 < WINDOWWIDTH:
            if Dinosaurs.dem2 == 1:
                window.blit(Dinosaurs.surface1, (Dinosaurs.x, Dinosaurs.y))
            if Dinosaurs.dem2 == 2:
                window.blit(Dinosaurs.surface2, (Dinosaurs.x, Dinosaurs.y))
            if Dinosaurs.dem2 == 3:
                window.blit(Dinosaurs.surface3, (Dinosaurs.x, Dinosaurs.y))
            if Dinosaurs.dem2 == 4:
                window.blit(Dinosaurs.surface4, (Dinosaurs.x, Dinosaurs.y))
            if Dinosaurs.dem2 == 5:
                window.blit(Dinosaurs.surface5, (Dinosaurs.x, Dinosaurs.y))
            if Dinosaurs.dem2 == 6:
                window.blit(Dinosaurs.surface6, (Dinosaurs.x, Dinosaurs.y))
            if Dinosaurs.dem2 == 7:
                window.blit(Dinosaurs.surface7, (Dinosaurs.x, Dinosaurs.y))
            if Dinosaurs.dem2 == 8:
                window.blit(Dinosaurs.surface8, (Dinosaurs.x, Dinosaurs.y))

            if Dinosaurs.dem2 < 8:
                Dinosaurs.dem2 += 1
            else:
                Dinosaurs.dem2 = 1
        elif Winner.xep_hang_so[0] == 3 or Winner.xep_hang_so[0] == 0:
            window.blit(Dinosaurs.surface_win, (Dinosaurs.x, Dinosaurs.y))
        else:
            window.blit(Dinosaurs.surface_lose, (Dinosaurs.x, Dinosaurs.y))

    def update(Dinosaurs):
        if Dinosaurs.x + 170 < WINDOWWIDTH:

            if Amulet.character_x_start[1][3] == 1:
                if Dinosaurs.dem_amulet < 3:
                    Dinosaurs.x += 3
                    Dinosaurs.dem_amulet += 1
                else:
                    Amulet.character_x_start[1][3] = 0
                    Dinosaurs.dem_amulet = 0
            elif Amulet.character_x_start[2][3] == 1:
                if Dinosaurs.dem_amulet < 3:
                    Dinosaurs.x = Dinosaurs.x
                    Dinosaurs.dem_amulet += 1
                else:
                    Amulet.character_x_start[1][3] = 0
                    Dinosaurs.dem_amulet = 0
            elif Amulet.character_x_start[3][3] == 1:
                if Dinosaurs.dem_amulet < 3:
                    Dinosaurs.x -= 3
                    Dinosaurs.dem_amulet += 1
                else:
                    Amulet.character_x_start[1][3] = 0
                    Dinosaurs.dem_amulet = 0
            elif Amulet.character_x_start[4][3] == 1:
                if Dinosaurs.dem_amulet < 3:
                    Dinosaurs.x += 3
                    Dinosaurs.x += random.randrange(1, Speed, 1)
                    Dinosaurs.dem_amulet += 1
                else:
                    Amulet.character_x_start[1][3] = 0
                    Dinosaurs.dem_amulet = 0
            elif Amulet.character_x_start[5][3] == 1:
                Dinosaurs.x += 20
                Amulet.character_x_start[1][3] = 0
            elif Amulet.character_x_start[6][3] == 1:
                Dinosaurs.x = WINDOWWIDTH - 170
            elif Amulet.character_x_start[7][3] == 1:
                Dinosaurs.x = 125
            else:
                Dinosaurs.x += random.randrange(1, Speed, 1)
        else:
            Dinosaurs.x = WINDOWWIDTH - 170


Dinosaurs = Dinosaurs()


class Cowboy():
    def __init__(Cowboy):
        Cowboy.dem = 0
        Cowboy.dem2 = 1
        Cowboy.x = 125  # vị trí của ông già Noel
        Cowboy.y = 17
        # tạo surface và thêm hình golddog
        Cowboy.surface1 = pygame.image.load('cowboy1.png')
        Cowboy.surface2 = pygame.image.load('cowboy2.png')
        Cowboy.surface3 = pygame.image.load('cowboy3.png')
        Cowboy.surface4 = pygame.image.load('cowboy4.png')
        Cowboy.surface5 = pygame.image.load('cowboy5.png')
        Cowboy.surface6 = pygame.image.load('cowboy6.png')
        Cowboy.surface7 = pygame.image.load('cowboy7.png')
        Cowboy.surface8 = pygame.image.load('cowboy8.png')
        Cowboy.surface_win = pygame.image.load('Cowboy_Win.png')
        Cowboy.surface_lose = pygame.image.load('Cowboylose.png')

        # gọi Noel.surface

    def draw(Cowboy):
        if Cowboy.x + 170 < WINDOWWIDTH:
            if Cowboy.dem2 == 1:
                window.blit(Cowboy.surface1, (Cowboy.x, Cowboy.y))
            if Cowboy.dem2 == 2:
                window.blit(Cowboy.surface2, (Cowboy.x, Cowboy.y))
            if Cowboy.dem2 == 3:
                window.blit(Cowboy.surface3, (Cowboy.x, Cowboy.y))
            if Cowboy.dem2 == 4:
                window.blit(Cowboy.surface4, (Cowboy.x, Cowboy.y))
            if Cowboy.dem2 == 5:
                window.blit(Cowboy.surface5, (Cowboy.x, Cowboy.y))
            if Cowboy.dem2 == 6:
                window.blit(Cowboy.surface6, (Cowboy.x, Cowboy.y))
            if Cowboy.dem2 == 7:
                window.blit(Cowboy.surface7, (Cowboy.x, Cowboy.y))
            if Cowboy.dem2 == 8:
                window.blit(Cowboy.surface8, (Cowboy.x, Cowboy.y))

            if Cowboy.dem2 < 8:
                Cowboy.dem2 += 1
            else:
                Cowboy.dem2 = 1

        elif Winner.xep_hang_so[0] == 1 or Winner.xep_hang_so[0] == 0:
            window.blit(Cowboy.surface_win, (Cowboy.x, Cowboy.y))
        else:
            window.blit(Cowboy.surface_lose, (Cowboy.x, Cowboy.y))

    def update(Cowboy):

        if Cowboy.x + 170 < WINDOWWIDTH:
            Cowboy.x += random.randrange(1, Speed, 1)
        else:
            Cowboy.x = WINDOWWIDTH - 170


Cowboy = Cowboy()


class Cowgirl():
    def __init__(Cowgirl):
        Cowgirl.dem = 0
        Cowgirl.dem2 = 1
        Cowgirl.x = 125  # vị trí của ông già Noel
        Cowgirl.y = 119
        # tạo surface và thêm hình golddog
        Cowgirl.surface1 = pygame.image.load('cowgirl1.png')
        Cowgirl.surface2 = pygame.image.load('cowgirl2.png')
        Cowgirl.surface3 = pygame.image.load('cowgirl3.png')
        Cowgirl.surface4 = pygame.image.load('cowgirl4.png')
        Cowgirl.surface5 = pygame.image.load('cowgirl5.png')
        Cowgirl.surface6 = pygame.image.load('cowgirl6.png')
        Cowgirl.surface7 = pygame.image.load('cowgirl7.png')
        Cowgirl.surface8 = pygame.image.load('cowgirl8.png')
        Cowgirl.surface_win = pygame.image.load('Cowgirl_Win.png')
        Cowgirl.surface_lose = pygame.image.load('Cowgirl_lose.png')

        # gọi Noel.surface

    def draw(Cowgirl):
        if Cowgirl.x + 170 < WINDOWWIDTH:
            if Cowgirl.dem2 == 1:
                window.blit(Cowgirl.surface1, (Cowgirl.x, Cowgirl.y))
            if Cowgirl.dem2 == 2:
                window.blit(Cowgirl.surface2, (Cowgirl.x, Cowgirl.y))
            if Cowgirl.dem2 == 3:
                window.blit(Cowgirl.surface3, (Cowgirl.x, Cowgirl.y))
            if Cowgirl.dem2 == 4:
                window.blit(Cowgirl.surface4, (Cowgirl.x, Cowgirl.y))
            if Cowgirl.dem2 == 5:
                window.blit(Cowgirl.surface5, (Cowgirl.x, Cowgirl.y))
            if Cowgirl.dem2 == 6:
                window.blit(Cowgirl.surface6, (Cowgirl.x, Cowgirl.y))
            if Cowgirl.dem2 == 7:
                window.blit(Cowgirl.surface7, (Cowgirl.x, Cowgirl.y))
            if Cowgirl.dem2 == 8:
                window.blit(Cowgirl.surface8, (Cowgirl.x, Cowgirl.y))

            if Cowgirl.dem2 < 8:
                Cowgirl.dem2 += 1
            else:
                Cowgirl.dem2 = 1

        elif Winner.xep_hang_so[0] == 2 or Winner.xep_hang_so[0] == 0:
            window.blit(Cowgirl.surface_win, (Cowgirl.x, Cowgirl.y))
        else:
            window.blit(Cowgirl.surface_lose, (Cowgirl.x, Cowgirl.y))

    def update(Cowgirl):

        if Cowgirl.x + 170 < WINDOWWIDTH:
            Cowgirl.x += random.randrange(1, Speed, 1)
        else:
            Cowgirl.x = WINDOWWIDTH - 170


Cowgirl = Cowgirl()


class Ninja():

    def __init__(Ninja):
        Ninja.x = 125
        Ninja.y = 324
        Ninja.dem = 0
        Ninja.dem2 = 1
        Ninja.surface1 = pygame.image.load('Ninja1.png')
        Ninja.surface2 = pygame.image.load('Ninja2.png')
        Ninja.surface3 = pygame.image.load('Ninja3.png')
        Ninja.surface4 = pygame.image.load('Ninja4.png')
        Ninja.surface5 = pygame.image.load('Ninja5.png')
        Ninja.surface6 = pygame.image.load('Ninja6.png')
        Ninja.surface7 = pygame.image.load('Ninja7.png')
        Ninja.surface8 = pygame.image.load('Ninja8.png')
        Ninja.surface9 = pygame.image.load('Ninja9.png')
        Ninja.surface10 = pygame.image.load('Ninja10.png')
        Ninja.surface_win = pygame.image.load('Ninja_win.png')
        Ninja.surface_lose = pygame.image.load('Ninjalose.png')

    def draw(Ninja):
        if Ninja.x + 170 < WINDOWWIDTH:
            if Ninja.dem2 == 1:
                window.blit(Ninja.surface1, (Ninja.x, Ninja.y))
            if Ninja.dem2 == 2:
                window.blit(Ninja.surface2, (Ninja.x, Ninja.y))
            if Ninja.dem2 == 3:
                window.blit(Ninja.surface3, (Ninja.x, Ninja.y))
            if Ninja.dem2 == 4:
                window.blit(Ninja.surface4, (Ninja.x, Ninja.y))
            if Ninja.dem2 == 5:
                window.blit(Ninja.surface5, (Ninja.x, Ninja.y))
            if Ninja.dem2 == 6:
                window.blit(Ninja.surface6, (Ninja.x, Ninja.y))
            if Ninja.dem2 == 7:
                window.blit(Ninja.surface7, (Ninja.x, Ninja.y))
            if Ninja.dem2 == 8:
                window.blit(Ninja.surface8, (Ninja.x, Ninja.y))
            if Ninja.dem2 == 9:
                window.blit(Ninja.surface9, (Ninja.x, Ninja.y))
            if Ninja.dem2 == 10:
                window.blit(Ninja.surface10, (Ninja.x, Ninja.y))

            if Ninja.dem2 < 10:
                Ninja.dem2 += 1
            else:
                Ninja.dem2 = 1

        elif Winner.xep_hang_so[0] == 4 or Winner.xep_hang_so[0] == 0:
            window.blit(Ninja.surface_win, (Ninja.x, Ninja.y))
        else:
            window.blit(Ninja.surface_lose, (Ninja.x, Ninja.y))

    def update(Ninja):

        if Ninja.x + 170 < WINDOWWIDTH:
            Ninja.x += random.randrange(1, Speed, 1)
        else:
            Ninja.x = WINDOWWIDTH - 170


Ninja = Ninja()


class An_Nguyen():

    def __init__(An_Nguyen):
        An_Nguyen.x = 125
        An_Nguyen.y = 225
        An_Nguyen.dem = 0
        An_Nguyen.dem2 = 1
        An_Nguyen.surface1 = pygame.image.load('An_Nguyen1.png')
        An_Nguyen.surface2 = pygame.image.load('An_Nguyen2.png')
        An_Nguyen.surface3 = pygame.image.load('An_Nguyen3.png')
        An_Nguyen.surface4 = pygame.image.load('An_Nguyen4.png')
        An_Nguyen.surface5 = pygame.image.load('An_Nguyen5.png')
        An_Nguyen.surface6 = pygame.image.load('An_Nguyen6.png')
        An_Nguyen.surface7 = pygame.image.load('An_Nguyen7.png')
        An_Nguyen.surface_win = pygame.image.load('An_Nguyen_Win.png')
        An_Nguyen.surface_lose = pygame.image.load('AnNguyen_lose.png')

    def draw(An_Nguyen):
        if An_Nguyen.x + 170 < WINDOWWIDTH:
            if An_Nguyen.dem2 == 1:
                window.blit(An_Nguyen.surface1, (An_Nguyen.x, An_Nguyen.y))
            if An_Nguyen.dem2 == 2:
                window.blit(An_Nguyen.surface2, (An_Nguyen.x, An_Nguyen.y))
            if An_Nguyen.dem2 == 3:
                window.blit(An_Nguyen.surface3, (An_Nguyen.x, An_Nguyen.y))
            if An_Nguyen.dem2 == 4:
                window.blit(An_Nguyen.surface4, (An_Nguyen.x, An_Nguyen.y))
            if An_Nguyen.dem2 == 5:
                window.blit(An_Nguyen.surface5, (An_Nguyen.x, An_Nguyen.y))
            if An_Nguyen.dem2 == 6:
                window.blit(An_Nguyen.surface6, (An_Nguyen.x, An_Nguyen.y))
            if An_Nguyen.dem2 == 7:
                window.blit(An_Nguyen.surface7, (An_Nguyen.x, An_Nguyen.y))

            if An_Nguyen.dem2 < 7:
                An_Nguyen.dem2 += 1
            else:
                An_Nguyen.dem2 = 1

        elif Winner.xep_hang_so[0] == 3 or Winner.xep_hang_so[0] == 0:
            window.blit(An_Nguyen.surface_win, (An_Nguyen.x, An_Nguyen.y))
        else:
            window.blit(An_Nguyen.surface_lose, (An_Nguyen.x, An_Nguyen.y))

    def update(An_Nguyen):

        if An_Nguyen.x + 170 < WINDOWWIDTH:
            An_Nguyen.x += random.randrange(1, Speed, 1)
        else:
            An_Nguyen.x = WINDOWWIDTH - 170


An_Nguyen = An_Nguyen()


class Dac_Khoa():
    def __init__(Dac_Khoa):
        Dac_Khoa.dem = 0
        Dac_Khoa.dem2 = 1
        Dac_Khoa.x = 125  # vị trí của ông già Noel
        Dac_Khoa.y = 17
        # tạo surface và thêm hình golddog
        Dac_Khoa.surface1 = pygame.image.load('Dac_Khoa1.png')
        Dac_Khoa.surface2 = pygame.image.load('Dac_Khoa2.png')
        Dac_Khoa.surface3 = pygame.image.load('Dac_Khoa3.png')
        Dac_Khoa.surface4 = pygame.image.load('Dac_Khoa4.png')
        Dac_Khoa.surface5 = pygame.image.load('Dac_Khoa5.png')
        Dac_Khoa.surface6 = pygame.image.load('Dac_Khoa6.png')
        Dac_Khoa.surface7 = pygame.image.load('Dac_Khoa7.png')
        Dac_Khoa.surface8 = pygame.image.load('Dac_Khoa8.png')
        Dac_Khoa.surface_win = pygame.image.load('DacKhoa_win.png')
        Dac_Khoa.surface_lose = pygame.image.load('DacKhoalose.png')

        # gọi Noel.surface

    def draw(Dac_Khoa):

        if Dac_Khoa.x + 170 < WINDOWWIDTH:
            if Dac_Khoa.dem2 == 1:
                window.blit(Dac_Khoa.surface1, (Dac_Khoa.x, Dac_Khoa.y))
            if Dac_Khoa.dem2 == 2:
                window.blit(Dac_Khoa.surface2, (Dac_Khoa.x, Dac_Khoa.y))
            if Dac_Khoa.dem2 == 3:
                window.blit(Dac_Khoa.surface3, (Dac_Khoa.x, Dac_Khoa.y))
            if Dac_Khoa.dem2 == 4:
                window.blit(Dac_Khoa.surface4, (Dac_Khoa.x, Dac_Khoa.y))
            if Dac_Khoa.dem2 == 5:
                window.blit(Dac_Khoa.surface5, (Dac_Khoa.x, Dac_Khoa.y))
            if Dac_Khoa.dem2 == 6:
                window.blit(Dac_Khoa.surface6, (Dac_Khoa.x, Dac_Khoa.y))
            if Dac_Khoa.dem2 == 7:
                window.blit(Dac_Khoa.surface7, (Dac_Khoa.x, Dac_Khoa.y))
            if Dac_Khoa.dem2 == 8:
                window.blit(Dac_Khoa.surface8, (Dac_Khoa.x, Dac_Khoa.y))

            if Dac_Khoa.dem2 < 8:
                Dac_Khoa.dem2 += 1
            else:
                Dac_Khoa.dem2 = 1

        elif Winner.xep_hang_so[0] == 1 or Winner.xep_hang_so[0] == 0:
            window.blit(Dac_Khoa.surface_win, (Dac_Khoa.x, Dac_Khoa.y))
        else:
            window.blit(Dac_Khoa.surface_lose, (Dac_Khoa.x, Dac_Khoa.y))

    def update(Dac_Khoa):

        if Dac_Khoa.x + 170 < WINDOWWIDTH:
            Dac_Khoa.x += random.randrange(1, Speed, 1)
        else:
            Dac_Khoa.x = WINDOWWIDTH - 170

Dac_Khoa = Dac_Khoa()


class Quang_Khoa():
    def __init__(Quang_Khoa):
        Quang_Khoa.dem = 0
        Quang_Khoa.dem2 = 1
        Quang_Khoa.x = 125  # vị trí của ông già Noel
        Quang_Khoa.y = 119
        # tạo surface và thêm hình golddog
        Quang_Khoa.surface1 = pygame.image.load('Quang_Khoa1.png')
        Quang_Khoa.surface2 = pygame.image.load('Quang_Khoa2.png')
        Quang_Khoa.surface3 = pygame.image.load('Quang_Khoa3.png')
        Quang_Khoa.surface4 = pygame.image.load('Quang_Khoa4.png')
        Quang_Khoa.surface5 = pygame.image.load('Quang_Khoa5.png')
        Quang_Khoa.surface6 = pygame.image.load('Quang_Khoa6.png')
        Quang_Khoa.surface7 = pygame.image.load('Quang_Khoa7.png')
        Quang_Khoa.surface8 = pygame.image.load('Quang_Khoa8.png')
        Quang_Khoa.surface_win = pygame.image.load('QuangKhoa_win.png')
        Quang_Khoa.surface_lose = pygame.image.load('QuangKhoalose.png')

        # gọi Noel.surface

    def draw(Quang_Khoa):

        if Quang_Khoa.x + 170 < WINDOWWIDTH:
            if Quang_Khoa.dem2 == 1:
                window.blit(Quang_Khoa.surface1, (Quang_Khoa.x, Quang_Khoa.y))
            if Quang_Khoa.dem2 == 2:
                window.blit(Quang_Khoa.surface2, (Quang_Khoa.x, Quang_Khoa.y))
            if Quang_Khoa.dem2 == 3:
                window.blit(Quang_Khoa.surface3, (Quang_Khoa.x, Quang_Khoa.y))
            if Quang_Khoa.dem2 == 4:
                window.blit(Quang_Khoa.surface4, (Quang_Khoa.x, Quang_Khoa.y))
            if Quang_Khoa.dem2 == 5:
                window.blit(Quang_Khoa.surface5, (Quang_Khoa.x, Quang_Khoa.y))
            if Quang_Khoa.dem2 == 6:
                window.blit(Quang_Khoa.surface6, (Quang_Khoa.x, Quang_Khoa.y))
            if Quang_Khoa.dem2 == 7:
                window.blit(Quang_Khoa.surface7, (Quang_Khoa.x, Quang_Khoa.y))
            if Quang_Khoa.dem2 == 8:
                window.blit(Quang_Khoa.surface8, (Quang_Khoa.x, Quang_Khoa.y))

            if Quang_Khoa.dem2 < 8:
                Quang_Khoa.dem2 += 1
            else:
                Quang_Khoa.dem2 = 1

        elif Winner.xep_hang_so[0] == 2 or Winner.xep_hang_so[0] == 0:
            window.blit(Quang_Khoa.surface_win, (Quang_Khoa.x, Quang_Khoa.y))
        else:
            window.blit(Quang_Khoa.surface_lose, (Quang_Khoa.x, Quang_Khoa.y))

    def update(Quang_Khoa):

        if Quang_Khoa.x + 170 < WINDOWWIDTH:
            Quang_Khoa.x += random.randrange(1, Speed, 1)
        else:
            Quang_Khoa.x = WINDOWWIDTH - 170


Quang_Khoa = Quang_Khoa()


class Dinh_Loc():
    def __init__(Dinh_Loc):
        Dinh_Loc.dem = 0
        Dinh_Loc.dem2 = 1
        Dinh_Loc.x = 125  # vị trí của ông già Noel
        Dinh_Loc.y = 530
        # tạo surface và thêm hình golddog
        Dinh_Loc.surface1 = pygame.image.load('Dinh_Loc1.png')
        Dinh_Loc.surface2 = pygame.image.load('Dinh_Loc2.png')
        Dinh_Loc.surface3 = pygame.image.load('Dinh_Loc3.png')
        Dinh_Loc.surface4 = pygame.image.load('Dinh_Loc4.png')
        Dinh_Loc.surface5 = pygame.image.load('Dinh_Loc5.png')
        Dinh_Loc.surface6 = pygame.image.load('Dinh_Loc6.png')
        Dinh_Loc.surface7 = pygame.image.load('Dinh_Loc7.png')
        Dinh_Loc.surface8 = pygame.image.load('Dinh_Loc8.png')
        Dinh_Loc.surface_win = pygame.image.load('Dinh_Loc_Win.png')
        Dinh_Loc.surface_lose = pygame.image.load('Dinh-Loc_lose.png')

        # gọi Noel.surface

    def draw(Dinh_Loc):

        if Dinh_Loc.x + 170 < WINDOWWIDTH:
            if Dinh_Loc.dem2 == 1:
                window.blit(Dinh_Loc.surface1, (Dinh_Loc.x, Dinh_Loc.y))
            if Dinh_Loc.dem2 == 2:
                window.blit(Dinh_Loc.surface2, (Dinh_Loc.x, Dinh_Loc.y))
            if Dinh_Loc.dem2 == 3:
                window.blit(Dinh_Loc.surface3, (Dinh_Loc.x, Dinh_Loc.y))
            if Dinh_Loc.dem2 == 4:
                window.blit(Dinh_Loc.surface4, (Dinh_Loc.x, Dinh_Loc.y))
            if Dinh_Loc.dem2 == 5:
                window.blit(Dinh_Loc.surface5, (Dinh_Loc.x, Dinh_Loc.y))
            if Dinh_Loc.dem2 == 6:
                window.blit(Dinh_Loc.surface6, (Dinh_Loc.x, Dinh_Loc.y))
            if Dinh_Loc.dem2 == 7:
                window.blit(Dinh_Loc.surface7, (Dinh_Loc.x, Dinh_Loc.y))
            if Dinh_Loc.dem2 == 8:
                window.blit(Dinh_Loc.surface8, (Dinh_Loc.x, Dinh_Loc.y))

            if Dinh_Loc.dem2 < 8:
                Dinh_Loc.dem2 += 1
            else:
                Dinh_Loc.dem2 = 1

        elif Winner.xep_hang_so[0] == 6 or Winner.xep_hang_so[0] == 0:
            window.blit(Dinh_Loc.surface_win, (Dinh_Loc.x, Dinh_Loc.y))
        else:
            window.blit(Dinh_Loc.surface_lose, (Dinh_Loc.x, Dinh_Loc.y))

    def update(Dinh_Loc):

        if Dinh_Loc.x + 170 < WINDOWWIDTH:
            Dinh_Loc.x += random.randrange(1, Speed, 1)
        else:
            Dinh_Loc.x = WINDOWWIDTH - 170


Dinh_Loc = Dinh_Loc()


class Gia_Long():
    def __init__(Gia_Long):
        Gia_Long.dem = 0
        Gia_Long.dem2 = 1
        Gia_Long.x = 125  # vị trí của ông già Noel
        Gia_Long.y = 324
        # tạo surface và thêm hình golddog
        Gia_Long.surface1 = pygame.image.load('Gia_Long1.png')
        Gia_Long.surface2 = pygame.image.load('Gia_Long2.png')
        Gia_Long.surface3 = pygame.image.load('Gia_Long3.png')
        Gia_Long.surface4 = pygame.image.load('Gia_Long4.png')
        Gia_Long.surface5 = pygame.image.load('Gia_Long5.png')
        Gia_Long.surface6 = pygame.image.load('Gia_Long6.png')
        Gia_Long.surface7 = pygame.image.load('Gia_Long7.png')
        Gia_Long.surface8 = pygame.image.load('Gia_Long8.png')
        Gia_Long.surface_win = pygame.image.load('Gia_Long_win.png')
        Gia_Long.surface_lose = pygame.image.load('Gialonglose.png')

        # gọi Noel.surface

    def draw(Gia_Long):

        if Gia_Long.x + 170 < WINDOWWIDTH:
            if Gia_Long.dem2 == 1:
                window.blit(Gia_Long.surface1, (Gia_Long.x, Gia_Long.y))
            if Gia_Long.dem2 == 2:
                window.blit(Gia_Long.surface2, (Gia_Long.x, Gia_Long.y))
            if Gia_Long.dem2 == 3:
                window.blit(Gia_Long.surface3, (Gia_Long.x, Gia_Long.y))
            if Gia_Long.dem2 == 4:
                window.blit(Gia_Long.surface4, (Gia_Long.x, Gia_Long.y))
            if Gia_Long.dem2 == 5:
                window.blit(Gia_Long.surface5, (Gia_Long.x, Gia_Long.y))
            if Gia_Long.dem2 == 6:
                window.blit(Gia_Long.surface6, (Gia_Long.x, Gia_Long.y))
            if Gia_Long.dem2 == 7:
                window.blit(Gia_Long.surface7, (Gia_Long.x, Gia_Long.y))
            if Gia_Long.dem2 == 8:
                window.blit(Gia_Long.surface8, (Gia_Long.x, Gia_Long.y))

            if Gia_Long.dem2 < 8:
                Gia_Long.dem2 += 1
            else:
                Gia_Long.dem2 = 1

        elif Winner.xep_hang_so[0] == 4 or Winner.xep_hang_so[0] == 0:
            window.blit(Gia_Long.surface_win, (Gia_Long.x, Gia_Long.y))
        else:
            window.blit(Gia_Long.surface_lose, (Gia_Long.x, Gia_Long.y))

    def update(Gia_Long):

        if Gia_Long.x + 170 < WINDOWWIDTH:
            Gia_Long.x += random.randrange(1, Speed, 1)
        else:
            Gia_Long.x = WINDOWWIDTH - 170


Gia_Long = Gia_Long()


class Khoi_Nguyen():
    def __init__(Khoi_Nguyen):
        Khoi_Nguyen.dem = 0
        Khoi_Nguyen.dem2 = 1
        Khoi_Nguyen.x = 125  # vị trí của ông già Noel
        Khoi_Nguyen.y = 426
        # tạo surface và thêm hình golddog
        Khoi_Nguyen.surface1 = pygame.image.load('Khoi_Nguyen1.png')
        Khoi_Nguyen.surface2 = pygame.image.load('Khoi_Nguyen2.png')
        Khoi_Nguyen.surface3 = pygame.image.load('Khoi_Nguyen3.png')
        Khoi_Nguyen.surface4 = pygame.image.load('Khoi_Nguyen4.png')
        Khoi_Nguyen.surface5 = pygame.image.load('Khoi_Nguyen5.png')
        Khoi_Nguyen.surface6 = pygame.image.load('Khoi_Nguyen6.png')
        Khoi_Nguyen.surface7 = pygame.image.load('Khoi_Nguyen7.png')
        Khoi_Nguyen.surface8 = pygame.image.load('Khoi_Nguyen8.png')
        Khoi_Nguyen.surface_win = pygame.image.load('KhoiNguyen_win.png')
        Khoi_Nguyen.surface_lose = pygame.image.load('Khoinguyenlose.png')

        # gọi Noel.surface

    def draw(Khoi_Nguyen):

        if Khoi_Nguyen.x + 170 < WINDOWWIDTH:
            if Khoi_Nguyen.dem2 == 1:
                window.blit(Khoi_Nguyen.surface1, (Khoi_Nguyen.x, Khoi_Nguyen.y))
            if Khoi_Nguyen.dem2 == 2:
                window.blit(Khoi_Nguyen.surface2, (Khoi_Nguyen.x, Khoi_Nguyen.y))
            if Khoi_Nguyen.dem2 == 3:
                window.blit(Khoi_Nguyen.surface3, (Khoi_Nguyen.x, Khoi_Nguyen.y))
            if Khoi_Nguyen.dem2 == 4:
                window.blit(Khoi_Nguyen.surface4, (Khoi_Nguyen.x, Khoi_Nguyen.y))
            if Khoi_Nguyen.dem2 == 5:
                window.blit(Khoi_Nguyen.surface5, (Khoi_Nguyen.x, Khoi_Nguyen.y))
            if Khoi_Nguyen.dem2 == 6:
                window.blit(Khoi_Nguyen.surface6, (Khoi_Nguyen.x, Khoi_Nguyen.y))
            if Khoi_Nguyen.dem2 == 7:
                window.blit(Khoi_Nguyen.surface7, (Khoi_Nguyen.x, Khoi_Nguyen.y))
            if Khoi_Nguyen.dem2 == 8:
                window.blit(Khoi_Nguyen.surface8, (Khoi_Nguyen.x, Khoi_Nguyen.y))

            if Khoi_Nguyen.dem2 < 8:
                Khoi_Nguyen.dem2 += 1
            else:
                Khoi_Nguyen.dem2 = 1

        elif Winner.xep_hang_so[0] == 5 or Winner.xep_hang_so[0] == 0:
            window.blit(Khoi_Nguyen.surface_win, (Khoi_Nguyen.x, Khoi_Nguyen.y))
        else:
            window.blit(Khoi_Nguyen.surface_lose, (Khoi_Nguyen.x, Khoi_Nguyen.y))

    def update(Khoi_Nguyen):

        if Khoi_Nguyen.x + 170 < WINDOWWIDTH:
            Khoi_Nguyen.x += random.randrange(1, Speed, 1)
        else:
            Khoi_Nguyen.x = WINDOWWIDTH - 170


Khoi_Nguyen = Khoi_Nguyen()


class Avatar():
    def __init__(Avatar):
        Avatar.x = 0
        Avatar.y = 0
        Avatar.surface1 = pygame.image.load('Avarta.png')
        Avatar.surface2 = Font_sans20.render(Login.text_user, True, GREEN, RED)

    def draw(Avatar):
        Avatar.surface2 = Font_sans20.render(Login.text_user, True, GREEN)

        window.blit(Avatar.surface1, (Avatar.x, Avatar.y))
        window.blit(Avatar.surface2, (61, 30))
        window.blit(Money.surface, (Money.x, Money.y))


Avatar = Avatar()


class Money():
    def __init__(Money):
        Money.x = 70
        Money.y = 8
        Money.existing = int(0)
        Money.font = pygame.font.SysFont('sons', 25)

    def update(Money):
        Money.surface = Money.font.render('$ ' + str(Money.existing), True, RED)


Money = Money()

class Amulet():
    def __init__(Amulet):
        Amulet.pos_x = [0, 0, 0, 0, 0, 0]
        Amulet.pos_y = [17, 119, 225, 324, 426, 530]
        Amulet.pos_x_character = [Cowboy.x, Cowgirl.x, Dinosaurs.x, Ninja.x, Gold_Dog.x, Grey_Cat.x]
        Amulet.character_x_start = [[1, 2, 3, 4, 5, 6],
                                    [0, 0, 0, 0, 0, 0],
                                    [0, 0, 0, 0, 0, 0],
                                    [0, 0, 0, 0, 0, 0],
                                    [0, 0, 0, 0, 0, 0],
                                    [0, 0, 0, 0, 0, 0],
                                    [0, 0, 0, 0, 0, 0],
                                    [0, 0, 0, 0, 0, 0], ]
        Amulet.surface = pygame.image.load('amulet.png')

    def draw(Amulet):
        for i in range(0, 6):
            if Amulet.pos_x[i] != 0:
                window.blit(Amulet.surface, (Amulet.pos_x[i], Amulet.pos_y[i]))
    def update(Amulet):
        for i in range(0, 6):
            if Amulet.pos_x[i] == 0:
                if Amulet.pos_x_character[i] + 300 < WINDOWWIDTH - 180 and random.randrange(1, 200, 1) == i:
                    Amulet.pos_x[i] = random.randrange(Amulet.pos_x_character[i], Amulet.pos_x_character[i] + 250, 1)
            if Amulet.pos_x_character[i] + 10 >= Amulet.pos_x[i] and Amulet.pos_x[i] != 0:
                Amulet.character_x_start[random.randrange(1, 7, 1)][i] = 1
                Amulet.pos_x[i] = 0



Amulet = Amulet()


class Amulet_Red():
    def __init__(Amulet_Red):
        Amulet_Red.start = False
        Amulet_Red.x = 30
        Amulet_Red.y = 20
        Amulet_Red.Mouse_x = 0
        Amulet_Red.Mouse_y = 0
        Amulet_Red.surface1 = pygame.image.load('bua do.png')
        Amulet_Red.sound = pygame.mixer.Sound('amulet1.mp3')
        Amulet_Red.rect = pygame.Rect(30, 20, 60, 98)

    def draw(Amulet_Red):
        Amulet_Red.surface2 = Font_sans20.render('X' + str(Shop.red), True, RED)

        window.blit(Amulet_Red.surface1, (Amulet_Red.x, Amulet_Red.y))
        window.blit(Amulet_Red.surface2, (95, 69))

        if event.type == pygame.MOUSEBUTTONDOWN:
            Amulet_Red.Mouse_x, Amulet_Red.Mouse_y = pygame.mouse.get_pos()
            if event.button == 1:
                if Amulet_Red.rect.collidepoint((Amulet_Red.Mouse_x, Amulet_Red.Mouse_y)) and Shop.red > 0:
                    pygame.mixer.Sound.play(Amulet_Red.sound)
                    Shop.red -= 1
                    if Character_Select.choice == 1:
                        Cowgirl.x -= 20
                        Dinosaurs.x -= 20
                        Ninja.x -= 20
                        Gold_Dog.x -= 20
                        Grey_Cat.x -= 20
                        Quang_Khoa.x -= 20
                        An_Nguyen.x -= 20
                        Gia_Long.x -= 20
                        Khoi_Nguyen.x -= 20
                        Dinh_Loc.x -= 20
                    if Character_Select.choice == 2:
                        Cowboy.x -= 20
                        Dinosaurs.x -= 20
                        Ninja.x -= 20
                        Gold_Dog.x -= 20
                        Grey_Cat.x -= 20
                        Dac_Khoa.x -= 20
                        An_Nguyen.x -= 20
                        Gia_Long.x -= 20
                        Khoi_Nguyen.x -= 20
                        Dinh_Loc.x -= 20
                    if Character_Select.choice == 3:
                        Cowboy.x -= 20
                        Cowgirl.x -= 20
                        Ninja.x -= 20
                        Gold_Dog.x -= 20
                        Grey_Cat.x -= 20
                        Dac_Khoa.x -= 20
                        Quang_Khoa.x -= 20
                        Gia_Long.x -= 20
                        Khoi_Nguyen.x -= 20
                        Dinh_Loc.x -= 20
                    if Character_Select.choice == 4:
                        Cowboy.x -= 20
                        Cowgirl.x -= 20
                        Dinosaurs.x -= 20
                        Gold_Dog.x -= 20
                        Grey_Cat.x -= 20
                        Dac_Khoa.x -= 20
                        Quang_Khoa.x -= 20
                        An_Nguyen.x -= 20
                        Khoi_Nguyen.x -= 20
                        Dinh_Loc.x -= 20
                    if Character_Select.choice == 5:
                        Cowboy.x -= 20
                        Cowgirl.x -= 20
                        Dinosaurs.x -= 20
                        Ninja.x -= 20
                        Grey_Cat.x -= 20
                        Dac_Khoa.x -= 20
                        Quang_Khoa.x -= 20
                        An_Nguyen.x -= 20
                        Gia_Long.x -= 20
                        Dinh_Loc.x -= 20
                    if Character_Select.choice == 6:
                        Cowboy.x -= 20
                        Cowgirl.x -= 20
                        Dinosaurs.x -= 20
                        Ninja.x -= 20
                        Gold_Dog.x -= 20
                        Dac_Khoa.x -= 20
                        Quang_Khoa.x -= 20
                        An_Nguyen.x -= 20
                        Gia_Long.x -= 20
                        Khoi_Nguyen.x -= 20

Amulet_Red = Amulet_Red()


class Amulet_Gold():
    def __init__(Amulet_Gold):
        Amulet_Gold.start = False
        Amulet_Gold.x = 30
        Amulet_Gold.y = 167
        Amulet_Gold.surface1 = pygame.image.load('bua vang.png')
        Amulet_Gold.sound = pygame.mixer.Sound('amulet2.mp3')
        Amulet_Gold.rect = pygame.Rect(30, 167, 60, 98)

    def draw(Amulet_Gold):
        Amulet_Gold.surface2 = Font_sans20.render('X' + str(Shop.gold), True, RED)

        window.blit(Amulet_Gold.surface1, (Amulet_Gold.x, Amulet_Gold.y))
        window.blit(Amulet_Gold.surface2, (95, 216))

        if event.type == pygame.MOUSEBUTTONDOWN:
            Amulet_Gold.Mouse_x, Amulet_Gold.Mouse_y = pygame.mouse.get_pos()
            if event.button == 1:
                if Amulet_Gold.rect.collidepoint((Amulet_Gold.Mouse_x, Amulet_Gold.Mouse_y)) and Shop.gold > 0:
                    pygame.mixer.Sound.play(Amulet_Gold.sound)
                    Shop.gold -= 1
                    Cowboy.x -= 40
                    Cowgirl.x -= 40
                    Dinosaurs.x -= 40
                    Ninja.x -= 40
                    Gold_Dog.x -= 40
                    Grey_Cat.x -= 40
                    Dac_Khoa.x -= 20
                    Quang_Khoa.x -= 20
                    An_Nguyen.x -= 20
                    Gia_Long.x -= 20
                    Khoi_Nguyen.x -= 20
                    Dinh_Loc.x -= 20


Amulet_Gold = Amulet_Gold()


class Amulet_Blue():
    def __init__(Amulet_Blue):
        Amulet_Blue.start = False
        Amulet_Blue.x = 30
        Amulet_Blue.y = 314
        Amulet_Blue.surface1 = pygame.image.load('bua xanh.png')
        Amulet_Blue.sound = pygame.mixer.Sound('amulet3.mp3')
        Amulet_Blue.rect = pygame.Rect(30, 314, 60, 98)

    def draw(Amulet_Blue):
        Amulet_Blue.surface2 = Font_sans20.render('X' + str(Shop.blue), True, RED)
        window.blit(Amulet_Blue.surface1, (Amulet_Blue.x, Amulet_Blue.y))
        window.blit(Amulet_Blue.surface2, (95, 350))

        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                Amulet_Blue.Mouse_x, Amulet_Blue.Mouse_y = pygame.mouse.get_pos()
                if Amulet_Blue.rect.collidepoint((Amulet_Blue.Mouse_x, Amulet_Blue.Mouse_y)) and Shop.blue > 0:
                    Shop.blue -= 1
                    pygame.mixer.Sound.play(Amulet_Blue.sound)
                    if Character_Select.choice == 1:
                        Cowboy.x += 20
                        Cowgirl.x -= 20
                        Dinosaurs.x -= 20
                        Ninja.x -= 20
                        Gold_Dog.x -= 20
                        Grey_Cat.x -= 20
                        Dac_Khoa.x += 20
                        Quang_Khoa.x -= 20
                        An_Nguyen.x -= 20
                        Gia_Long.x -= 20
                        Khoi_Nguyen.x -= 20
                        Dinh_Loc.x -= 20
                    if Character_Select.choice == 2:
                        Cowboy.x -= 20
                        Cowgirl.x += 20
                        Dinosaurs.x -= 20
                        Ninja.x -= 20
                        Gold_Dog.x -= 20
                        Grey_Cat.x -= 20
                        Dac_Khoa.x -= 20
                        Quang_Khoa.x += 20
                        An_Nguyen.x -= 20
                        Gia_Long.x -= 20
                        Khoi_Nguyen.x -= 20
                        Dinh_Loc.x -= 20
                    if Character_Select.choice == 3:
                        Cowboy.x -= 20
                        Cowgirl.x -= 20
                        Dinosaurs.x += 20
                        Ninja.x -= 20
                        Gold_Dog.x -= 20
                        Grey_Cat.x -= 20
                        Dac_Khoa.x -= 20
                        Quang_Khoa.x -= 20
                        An_Nguyen.x += 20
                        Gia_Long.x -= 20
                        Khoi_Nguyen.x -= 20
                        Dinh_Loc.x -= 20
                    if Character_Select.choice == 4:
                        Cowboy.x -= 20
                        Cowgirl.x -= 20
                        Dinosaurs.x -= 20
                        Ninja.x += 20
                        Gold_Dog.x -= 20
                        Grey_Cat.x -= 20
                        Dac_Khoa.x -= 20
                        Quang_Khoa.x -= 20
                        An_Nguyen.x -= 20
                        Gia_Long.x += 20
                        Khoi_Nguyen.x -= 20
                        Dinh_Loc.x -= 20
                    if Character_Select.choice == 5:
                        Cowboy.x -= 20
                        Cowgirl.x -= 20
                        Dinosaurs.x -= 20
                        Ninja.x -= 20
                        Gold_Dog.x += 20
                        Grey_Cat.x -= 20
                        Dac_Khoa.x -= 20
                        Quang_Khoa.x -= 20
                        An_Nguyen.x -= 20
                        Gia_Long.x -= 20
                        Khoi_Nguyen.x += 20
                        Dinh_Loc.x -= 20
                    if Character_Select.choice == 6:
                        Cowboy.x -= 20
                        Cowgirl.x -= 20
                        Dinosaurs.x -= 20
                        Ninja.x -= 20
                        Gold_Dog.x -= 20
                        Grey_Cat.x += 20
                        Dac_Khoa.x -= 20
                        Quang_Khoa.x -= 20
                        An_Nguyen.x -= 20
                        Gia_Long.x -= 20
                        Khoi_Nguyen.x -= 20
                        Dinh_Loc.x += 20


Amulet_Blue = Amulet_Blue()


class Game():

    def __init__(Game):
        Game.start = False
        Game.start2 = False

    def update(Game):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                Pause.start = True
                Game.start = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                Game.Mouse_x, Game.Mouse_y = pygame.mouse.get_pos()
                if Pause.pos.collidepoint((Game.Mouse_x, Game.Mouse_y)):
                    Pause.start = True
                    Game.start = False
        # pygame.mixer.music.unload()
        # Game.music = pygame.mixer.music.load('platform1.mp3')
        # pygame.mixer.music.play(-1)
        map.draw()
        Pause.draw()
        Amulet_Red.draw()
        Amulet_Gold.draw()
        Amulet_Blue.draw()
        if Character_Select.start1:

            Gold_Dog.update()
            Grey_Cat.update()
            Dinosaurs.update()
            Cowboy.update()
            Cowgirl.update()
            Ninja.update()
            Gold_Dog.draw()
            Grey_Cat.draw()
            Dinosaurs.draw()
            Cowboy.draw()
            Cowgirl.draw()
            Ninja.draw()

        if Character_Select.start2:

            An_Nguyen.update()
            Dac_Khoa.update()
            Quang_Khoa.update()
            Dinh_Loc.update()
            Gia_Long.update()
            Khoi_Nguyen.update()
            An_Nguyen.draw()
            Dac_Khoa.draw()
            Quang_Khoa.draw()
            Dinh_Loc.draw()
            Gia_Long.draw()
            Khoi_Nguyen.draw()


Game = Game()


class Pause():
    def __init__(Pause):
        Pause.x = WINDOWWIDTH / 4
        Pause.y = WINDOWHEIGHT / 2 - 100
        Pause.start = False
        Pause.surface = pygame.image.load('PAUSE.png')
        Pause.surface = pygame.transform.scale(Pause.surface, (WINDOWWIDTH, WINDOWHEIGHT))
        Pause.pos = pygame.Rect(1150, 13, 40, 37)
        Pause.back = pygame.Rect(450, 260, 380, 85)
        Pause.home = pygame.Rect(450, 385, 380, 85)

    def draw(Pause):
        if Pause.start == True:
            Pause.Mouse_x, Pause.Mouse_y = pygame.mouse.get_pos()
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    if Pause.back.collidepoint((Pause.Mouse_x, Pause.Mouse_y)):
                        Pause.start = False
                        Game.start = True
                    if Pause.home.collidepoint((Pause.Mouse_x, Pause.Mouse_y)):
                        Pause.start = False
                        Start.start = True

            if Character_Select.start1:
                Gold_Dog.dem2 = 1
                Grey_Cat.dem2 = 1
                Dinosaurs.dem2 = 1
                Cowboy.dem2 = 1
                Cowgirl.dem2 = 1
                Ninja.dem2 = 1
                map.draw()
                Gold_Dog.draw()
                Grey_Cat.draw()
                Dinosaurs.draw()
                Cowboy.draw()
                Cowgirl.draw()
                Ninja.draw()

            if Character_Select.start2:
                An_Nguyen.dem2 = 1
                Dac_Khoa.dem2 = 1
                Quang_Khoa.dem2 = 1
                Dinh_Loc.dem2 = 1
                Khoi_Nguyen.dem2 = 1
                Gia_Long.dem2 = 1
                map.draw()
                An_Nguyen.draw()
                Dac_Khoa.draw()
                Quang_Khoa.draw()
                Dinh_Loc.draw()
                Khoi_Nguyen.draw()
                Gia_Long.draw()

            window.blit(Pause.surface, (0, 0))


Pause = Pause()


class Winner():
    def __init__(Winner):
        Winner.start = True
        Winner.x = WINDOWWIDTH / 2 - 100
        Winner.y = 0
        Winner.dem = [0, 0, 0, 0, 0, 0]
        Winner.dem_bet = 0
        Winner.xep_hang_so = [0, 0, 0, 0, 0, 0]
        Winner.xep_hang_chu = ['', '', '', '', '', '']
        Winner.i = 0
        Winner.surface11 = Font_Winner.render(CharacterName1[0] + ' Win', True, GREEN, RED)
        Winner.surface12 = Font_Winner.render(CharacterName1[1] + ' Win', True, GREEN, RED)
        Winner.surface13 = Font_Winner.render(CharacterName1[2] + ' Win', True, GREEN, RED)
        Winner.surface14 = Font_Winner.render(CharacterName1[3] + ' Win', True, GREEN, RED)
        Winner.surface15 = Font_Winner.render(CharacterName1[4] + ' Win', True, GREEN, RED)
        Winner.surface16 = Font_Winner.render(CharacterName1[5] + ' Win', True, GREEN, RED)

        Winner.surface21 = Font_Winner.render(CharacterName2[0] + ' Win', True, GREEN, RED)
        Winner.surface22 = Font_Winner.render(CharacterName2[1] + ' Win', True, GREEN, RED)
        Winner.surface23 = Font_Winner.render(CharacterName2[2] + ' Win', True, GREEN, RED)
        Winner.surface24 = Font_Winner.render(CharacterName2[3] + ' Win', True, GREEN, RED)
        Winner.surface25 = Font_Winner.render(CharacterName2[4] + ' Win', True, GREEN, RED)
        Winner.surface26 = Font_Winner.render(CharacterName2[5] + ' Win', True, GREEN, RED)

        Winner.surface_End_hinh = pygame.image.load('KẾT QUẢ.png')
        Winner.surface_End_hinh = pygame.transform.scale(Winner.surface_End_hinh, (WINDOWWIDTH, WINDOWHEIGHT))

        Winner.surface_Victory = pygame.image.load('VICTORY.png')
        Winner.surface_Victory2 = pygame.image.load('you win.png')
        Winner.surface_Lose2 = pygame.image.load('you lose.png')
        Winner.surface_Lose = pygame.image.load('LOSE.png')

        Winner.pos_home = pygame.Rect(495, 590, 55, 40)
        Winner.pos_back = pygame.Rect(610, 590, 55, 40)

    def draw(Winner):
        if Winner.i <= 5:
            if Character_Select.start1:
                if Cowboy.x + 170 == WINDOWWIDTH and Winner.dem[0] == 0:
                    Winner.xep_hang_so[Winner.i] = 1
                    Winner.i += 1
                    Winner.dem[0] = 1
                if Cowgirl.x + 170 == WINDOWWIDTH and Winner.dem[1] == 0:
                    Winner.xep_hang_so[Winner.i] = 2
                    Winner.i += 1
                    Winner.dem[1] = 1
                if Dinosaurs.x + 170 == WINDOWWIDTH and Winner.dem[2] == 0:
                    Winner.xep_hang_so[Winner.i] = 3
                    Winner.i += 1
                    Winner.dem[2] = 1
                if Ninja.x + 170 == WINDOWWIDTH and Winner.dem[3] == 0:
                    Winner.xep_hang_so[Winner.i] = 4
                    Winner.i += 1
                    Winner.dem[3] = 1
                if Gold_Dog.x + 170 == WINDOWWIDTH and Winner.dem[4] == 0:
                    Winner.xep_hang_so[Winner.i] = 5
                    Winner.i += 1
                    Winner.dem[4] = 1
                if Grey_Cat.x + 170 == WINDOWWIDTH and Winner.dem[5] == 0:
                    Winner.xep_hang_so[Winner.i] = 6
                    Winner.i += 1
                    Winner.dem[5] = 1

            if Character_Select.start2:
                if Dac_Khoa.x + 170 == WINDOWWIDTH and Winner.dem[0] == 0:
                    Winner.xep_hang_so[Winner.i] = 1
                    Winner.i += 1
                    Winner.dem[0] = 1
                if Quang_Khoa.x + 170 == WINDOWWIDTH and Winner.dem[1] == 0:
                    Winner.xep_hang_so[Winner.i] = 2
                    Winner.i += 1
                    Winner.dem[1] = 1
                if An_Nguyen.x + 170 == WINDOWWIDTH and Winner.dem[2] == 0:
                    Winner.xep_hang_so[Winner.i] = 3
                    Winner.i += 1
                    Winner.dem[2] = 1
                if Gia_Long.x + 170 == WINDOWWIDTH and Winner.dem[3] == 0:
                    Winner.xep_hang_so[Winner.i] = 4
                    Winner.i += 1
                    Winner.dem[3] = 1
                if Khoi_Nguyen.x + 170 == WINDOWWIDTH and Winner.dem[4] == 0:
                    Winner.xep_hang_so[Winner.i] = 5
                    Winner.i += 1
                    Winner.dem[4] = 1
                if Dinh_Loc.x + 170 == WINDOWWIDTH and Winner.dem[5] == 0:
                    Winner.xep_hang_so[Winner.i] = 6
                    Winner.i += 1
                    Winner.dem[5] = 1

        if Winner.i == 6:
            for i in range(1, 3):
                time.sleep(1)

            window.blit(Winner.surface_End_hinh, (0, 0))
            if Character_Select.choice == Winner.xep_hang_so[0]:
                window.blit(Winner.surface_Victory2, (400, 160))
            else:
                window.blit(Winner.surface_Lose2, (400, 160))

            for event in pygame.event.get():
                if event.type == MOUSEBUTTONDOWN:
                    if event.button == 1:
                        if Winner.pos_home.collidepoint(event.pos):
                            Start.start = True
                            Game.start = False
            if Character_Select.start1:
                for i in range(0, 6):
                    Winner.xep_hang_chu[i] = CharacterName1[Winner.xep_hang_so[i] - 1]
                    Winner.surface_End_chu = Font_sans30.render(Winner.xep_hang_chu[i], True, BLACK)
                    window.blit(Winner.surface_End_chu, (500, 267 + 53 * i))
            else:
                for i in range(0, 6):
                    Winner.xep_hang_chu[i] = CharacterName2[Winner.xep_hang_so[i] - 1]
                    Winner.surface_End_chu = Font_sans30.render(Winner.xep_hang_chu[i], True, BLACK)
                    window.blit(Winner.surface_End_chu, (500, 267 + 53 * i))

        elif Winner.i != 0:
            if Character_Select.choice == Winner.xep_hang_so[0]:
                if Winner.dem_bet == 0:
                    Money.existing += Bet.amount * 4
                    Winner.dem_bet += 1
                window.blit(Winner.surface_Victory, (450, 50))
                pygame.mixer.music.unload()
                Winner.victory = pygame.mixer.music.load('victory.mp3')
                pygame.mixer.music.play(1)
            else:
                window.blit(Winner.surface_Lose, (450, 50))
                pygame.mixer.music.unload()
                Winner.lose = pygame.mixer.music.load('lose.mp3')
                pygame.mixer.music.play(1)

Winner = Winner()

pygame.mixer.music.play(-1)

while True:

    for event in pygame.event.get():
        if event.type == QUIT:
            if Money.existing == 0:
                Login.Update_value('C' + str(Login.Find_user(Login.text_user)), int(0))
            else:
                Login.Update_value('C' + str(Login.Find_user(Login.text_user)), int(Money.existing))
            pygame.quit()
            sys.exit()

    window.fill(WHITE)

    Mouse_x, Mouse_y = pygame.mouse.get_pos()
    #print(Mouse_x, '   ', Mouse_y)
    if Login.start:
        Login.draw()
        Login.Login()

    if Register.start:
        Register.Register()

    if Start.start:
        Start.draw()

    if Shop.start:
        Shop.draw()

    if Game_Select.start:
        Game_Select.draw()

    if Flappy.start:
        Flappy.draw()

    if Snake.start:
        Snake.draw()

    if Map_Select.start:
        Map_Select.draw()

    if Character_Select.start:
        Character_Select.draw()

    if Bet.start:
        Bet.draw()

    if Ready.start:
        Ready.draw()

    if Game.start:
        Game.update()
        Amulet.draw()
        Amulet.update()
        Winner.draw()
        time.sleep(0.1)

    if Pause.start:
        Pause.draw()

    if not Login.start and not Register.start:
        Money.update()
        Avatar.draw()

    pygame.display.update()
    fpsClock.tick(FPS)


