import pygame, sys, time, math
import random
from pygame.locals import *
from tkinter import *

WINDOWWIDTH = 1200  # Chiều dài cửa sổ
WINDOWHEIGHT = 686  # Chiều cao cửa sổ

WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)

Main_Game = False

pygame.init()
root = Tk()

# Xác định FPS
FPS = 80
fpsClock = pygame.time.Clock()

window = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT))
pygame.display.set_caption('Do_An_Nhom_1')
Font_Winner = pygame.font.SysFont('consolas', 30)
Font_Pause = pygame.font.SysFont('consolas', 40)

Mouse_x = 0
Mouse_y = 0
CharacterName = ['Cowboy', 'Cow Girl', 'Dinosaurs', 'Ninja', 'Gold Dog', 'Grey Cat']

Speed = 10


# surface start
class Start():

    def __init__(Start):
        Start.x = 0  # hoành độ của giao diện start
        Start.y = 0  # tung độ của giao diện surface
        Start.dem1 = 0
        Start.start = True
        # tạo surface của start
        Start.surface = pygame.image.load('Start.png')
        # resize theo kích thước cửa sổ game
        Start.surface = pygame.transform.scale(Start.surface, (WINDOWWIDTH, WINDOWHEIGHT))

    # vẽ Start lên surface vừa tạo
    def draw(Start):
        window.blit(Start.surface, (Start.x, Start.y))
        if event.type == pygame.MOUSEBUTTONDOWN:
            Mouse_x, Mouse_y = pygame.mouse.get_pos()
            if event.button == 1 and (432 <= Mouse_x <= 773) and (355 <= Mouse_y <= 486):
                Start.start = False
                Map_Select.start = True


Start = Start()


class Map_Select():
    def __init__(Map_Select):
        Map_Select.x = 0
        Map_Select.start = False

        Map_Select.surface = pygame.image.load('MapSelect.png')
        Map_Select.surface = pygame.transform.scale(Map_Select.surface, (WINDOWWIDTH, WINDOWHEIGHT))

    def draw(Map_Select):
        window.blit(Map_Select.surface, (Map_Select.x, 0))
        Map_1 = pygame.Rect(262, 125, 250, 190)
        Map_2 = pygame.Rect(690, 125, 250, 190)
        Map_3 = pygame.Rect(262, 348, 250, 190)
        Map_4 = pygame.Rect(690, 348, 250, 190)
        if event.type == pygame.MOUSEBUTTONUP:
            Mouse_x, Mouse_y = pygame.mouse.get_pos()
            if event.button == 1:
                if Map_1.collidepoint((Mouse_x, Mouse_y)):
                    Character_Select.start = True
                    Map_Select.start = False
                    map.Sanhok = True
            if Map_2.collidepoint((Mouse_x, Mouse_y)):
                Character_Select.start = True
                Map_Select.start = False
                map.Vilkendi = True
            if Map_3.collidepoint((Mouse_x, Mouse_y)):
                Character_Select.start = True
                Map_Select.start = False
                map.Mirama = True
            if Map_4.collidepoint((Mouse_x, Mouse_y)):
                Character_Select.start = True
                Map_Select.start = False
                map.Sanhok_night = True


Map_Select = Map_Select()


class Character_Select():
    def __init__(Character_Select):
        Character_Select.x = 0
        Character_Select.start = False

        Character_Select.Mouse_x = 0
        Character_Select.Mouse_y = 0

        Character_Select.choice = 0

        Character_Select.surface = pygame.image.load('CharacterSelect.png')
        Character_Select.surface = pygame.transform.scale(Character_Select.surface, (WINDOWWIDTH, WINDOWHEIGHT))

    def draw(Character_Select):
        window.blit(Character_Select.surface, (Character_Select.x, 0))
        Mouse_x, Mouse_y = pygame.mouse.get_pos()
        Character_1 = pygame.Rect(224, 120, 193, 200)
        Character_2 = pygame.Rect(503, 120, 193, 200)
        Character_3 = pygame.Rect(808, 120, 193, 200)
        Character_4 = pygame.Rect(224, 339, 193, 200)
        Character_5 = pygame.Rect(503, 339, 193, 200)
        Character_6 = pygame.Rect(808, 339, 193, 200)
        if Character_Select.start == True:
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    if Character_1.collidepoint((Mouse_x, Mouse_y)):
                        print("Nhan vat 1")
                        Character_Select.choice = 1
                        Character_Select.start = False
                        Ready.start = True
                    if Character_2.collidepoint((Mouse_x, Mouse_y)):
                        print("Nhan vat 2")
                        Character_Select.choice = 2
                        Character_Select.start = False
                        Ready.start = True
                    if Character_3.collidepoint((Mouse_x, Mouse_y)):
                        print("Nhan vat 3")
                        Character_Select.choice = 3
                        Character_Select.start = False
                        Ready.start = True
                    if Character_4.collidepoint((Mouse_x, Mouse_y)):
                        print("Nhan vat 4")
                        Character_Select.choice = 4
                        Character_Select.start = False
                        Ready.start = True
                    if Character_5.collidepoint((Mouse_x, Mouse_y)):
                        print("Nhan vat 5")
                        Character_Select.choice = 5
                        Character_Select.start = False
                        Ready.start = True
                    if Character_6.collidepoint((Mouse_x, Mouse_y)):
                        print("Nhan vat 6")
                        Character_Select.choice = 6
                        Character_Select.start = False
                        Ready.start = True


Character_Select = Character_Select()


class Ready():
    def __init__(Ready):
        Ready.start = False
        Ready.x = WINDOWWIDTH / 2
        Ready.y = WINDOWHEIGHT / 4
        Ready.secs3 = pygame.image.load('3.png')
        Ready.secs2 = pygame.image.load('2.png')
        Ready.secs1 = pygame.image.load('1.png')
        Ready.go = pygame.image.load('GO.png')

    def draw(Ready):
        secs = [Ready.secs3, Ready.secs2, Ready.secs1, Ready.go]
        if event.type == pygame.MOUSEBUTTONUP and Ready.start:
            for sec in secs:
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
        Gold_Dog.y = 460
        # tạo surface và thêm hình golddog
        Gold_Dog.surface1 = pygame.image.load('golddog1.png')
        Gold_Dog.surface2 = pygame.image.load('golddog2.png')
        Gold_Dog.surface3 = pygame.image.load('golddog3.png')
        Gold_Dog.surface4 = pygame.image.load('golddog4.png')
        Gold_Dog.surface5 = pygame.image.load('golddog5.png')
        Gold_Dog.surface6 = pygame.image.load('golddog6.png')
        Gold_Dog.surface7 = pygame.image.load('golddog7.png')
        Gold_Dog.surface8 = pygame.image.load('golddog8.png')

    # gọi Noel.surface
    def draw(Gold_Dog):

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

    def update(Gold_Dog):
        Gold_Dog.x += random.randrange(1, Speed, 1)
        if Gold_Dog.x + 125 > WINDOWWIDTH and Gold_Dog.dem < 8:
            Gold_Dog.y -= 2.5
            Gold_Dog.dem += 1
            Gold_Dog.x += 3.5

        if Gold_Dog.dem >= 8:
            Gold_Dog.y += 3
            Gold_Dog.x += 3.5


Gold_Dog = Gold_Dog()


class Grey_Cat():

    def __init__(Grey_Cat):
        Grey_Cat.x = 125
        Grey_Cat.y = 572
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

    def draw(Grey_Cat):
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

    def update(Grey_Cat):
        Grey_Cat.x += random.randrange(1, Speed, 1)
        if Grey_Cat.x + 125 > WINDOWWIDTH and Grey_Cat.dem < 8:
            Grey_Cat.y -= 2.5
            Grey_Cat.dem += 1
            Grey_Cat.x += 3.5

        if Grey_Cat.dem >= 8:
            Grey_Cat.y += 3
            Grey_Cat.x += 3.5


Grey_Cat = Grey_Cat()


class Dinosaurs():

    def __init__(Dinosaurs):
        Dinosaurs.x = 125
        Dinosaurs.y = 234
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

    def draw(Dinosaurs):
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

    def update(Dinosaurs):
        Dinosaurs.x += random.randrange(1, Speed, 1)
        if Dinosaurs.x + 125 > WINDOWWIDTH and Dinosaurs.dem < 8:
            Dinosaurs.y -= 2.5
            Dinosaurs.dem += 1
            Dinosaurs.x += 3.5

        if Dinosaurs.dem >= 8:
            Dinosaurs.y += 3
            Dinosaurs.x += 3.5


Dinosaurs = Dinosaurs()


class Cowboy():
    def __init__(Cowboy):
        Cowboy.dem = 0
        Cowboy.dem2 = 1
        Cowboy.x = 125  # vị trí của ông già Noel
        Cowboy.y = 2
        # tạo surface và thêm hình golddog
        Cowboy.surface1 = pygame.image.load('cowboy1.png')
        Cowboy.surface2 = pygame.image.load('cowboy2.png')
        Cowboy.surface3 = pygame.image.load('cowboy3.png')
        Cowboy.surface4 = pygame.image.load('cowboy4.png')
        Cowboy.surface5 = pygame.image.load('cowboy5.png')
        Cowboy.surface6 = pygame.image.load('cowboy6.png')
        Cowboy.surface7 = pygame.image.load('cowboy7.png')
        Cowboy.surface8 = pygame.image.load('cowboy8.png')

        # gọi Noel.surface

    def draw(Cowboy):

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

    def update(Cowboy):
        Cowboy.x += random.randrange(1, Speed, 2)
        if Cowboy.x + 125 > WINDOWWIDTH and Cowboy.dem < 8:
            Cowboy.y -= 2.5
            Cowboy.dem += 1
            Cowboy.x += 3.5

        if Cowboy.dem >= 8:
            Cowboy.y += 3
            Cowboy.x += 3.5


Cowboy = Cowboy()


class Cowgirl():
    def __init__(Cowgirl):
        Cowgirl.dem = 0
        Cowgirl.dem2 = 1
        Cowgirl.x = 125  # vị trí của ông già Noel
        Cowgirl.y = 116
        # tạo surface và thêm hình golddog
        Cowgirl.surface1 = pygame.image.load('cowgirl1.png')
        Cowgirl.surface2 = pygame.image.load('cowgirl2.png')
        Cowgirl.surface3 = pygame.image.load('cowgirl3.png')
        Cowgirl.surface4 = pygame.image.load('cowgirl4.png')
        Cowgirl.surface5 = pygame.image.load('cowgirl5.png')
        Cowgirl.surface6 = pygame.image.load('cowgirl6.png')
        Cowgirl.surface7 = pygame.image.load('cowgirl7.png')
        Cowgirl.surface8 = pygame.image.load('cowgirl8.png')

        # gọi Noel.surface

    def draw(Cowgirl):

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

    def update(Cowgirl):
        Cowgirl.x += random.randrange(1, Speed, 2)
        if Cowgirl.x + 125 > WINDOWWIDTH and Cowgirl.dem < 8:
            Cowgirl.y -= 2.5
            Cowgirl.dem += 1
            Cowgirl.x += 3.5

        if Cowgirl.dem >= 8:
            Cowgirl.y += 3
            Cowgirl.x += 3.5


Cowgirl = Cowgirl()


class Ninja():

    def __init__(Ninja):
        Ninja.x = 125
        Ninja.y = 347
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

    def draw(Ninja):
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

    def update(Ninja):
        Ninja.x += random.randrange(1, Speed, 1)
        # print(Grey_Cat.x)
        if Ninja.x + 125 > WINDOWWIDTH and Ninja.dem < 8:
            Ninja.y -= 2.5
            Ninja.dem += 1
            Ninja.x += 3.5

        if Ninja.dem >= 8:
            Ninja.y += 3
            Ninja.x += 3.5


Ninja = Ninja()


class Game():

    def __init__(Game):
        Game.start = False
        Game.start2 = False

    def update(Game):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                Pause.start = True
                Game.start = False
        map.draw()
        Gold_Dog.draw()
        Gold_Dog.update()
        Grey_Cat.draw()
        Grey_Cat.update()
        Dinosaurs.draw()
        Dinosaurs.update()
        Cowboy.draw()
        Cowboy.update()
        Cowgirl.draw()
        Cowgirl.update()
        Ninja.draw()
        Ninja.update()


Game = Game()


class Pause():
    def __init__(Pause):
        Pause.x = WINDOWWIDTH / 4
        Pause.y = WINDOWHEIGHT / 2
        Pause.start = False
        Pause.surface = Font_Pause.render('PAUSE - Press C to continue', True, GREEN, RED)

    def draw(Pause):
        if Pause.start == True:
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_c:
                    Pause.start = False
                    Game.start = True

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

            window.blit(Pause.surface, (Pause.x, Pause.y))


Pause = Pause()


class Winner():
    def __init__(Winner):
        Winner.x = WINDOWWIDTH / 2 - 100
        Winner.y = 0
        Winner.dem = 0
        Winner.surface1 = Font_Winner.render(CharacterName[0] + ' Win', True, GREEN, RED)
        Winner.surface2 = Font_Winner.render(CharacterName[1] + ' Win', True, GREEN, RED)
        Winner.surface3 = Font_Winner.render(CharacterName[2] + ' Win', True, GREEN, RED)
        Winner.surface4 = Font_Winner.render(CharacterName[3] + ' Win', True, GREEN, RED)
        Winner.surface5 = Font_Winner.render(CharacterName[4] + ' Win', True, GREEN, RED)
        Winner.surface6 = Font_Winner.render(CharacterName[5] + ' Win', True, GREEN, RED)
        Winner.surface_Victory = pygame.image.load('VICTORY.png')
        Winner.surface_Lose = pygame.image.load('LOSE.png')

    def draw(Winner):
        if Cowboy.x + 50 >= WINDOWWIDTH and (Winner.dem == 0 or Winner.dem == 1):
            window.blit(Winner.surface1, (Winner.x, Winner.y))
            Winner.dem = 1
            if Winner.dem == Character_Select.choice:
                window.blit(Winner.surface_Victory, (450, 200))
            else:
                window.blit(Winner.surface_Lose, (450, 200))
        if Cowgirl.x + 50 >= WINDOWWIDTH and (Winner.dem == 0 or Winner.dem == 2):
            window.blit(Winner.surface2, (Winner.x, Winner.y))
            Winner.dem = 2
            if Winner.dem == Character_Select.choice:
                window.blit(Winner.surface_Victory, (450, 200))
            else:
                window.blit(Winner.surface_Lose, (450, 200))
        if Dinosaurs.x + 50 >= WINDOWWIDTH and (Winner.dem == 0 or Winner.dem == 3):
            window.blit(Winner.surface3, (Winner.x, Winner.y))
            Winner.dem = 3
            if Winner.dem == Character_Select.choice:
                window.blit(Winner.surface_Victory, (450, 200))
            else:
                window.blit(Winner.surface_Lose, (450, 200))
        if Ninja.x + 50 >= WINDOWWIDTH and (Winner.dem == 0 or Winner.dem == 4):
            window.blit(Winner.surface4, (Winner.x, Winner.y))
            Winner.dem = 4
            if Winner.dem == Character_Select.choice:
                window.blit(Winner.surface_Victory, (450, 200))
            else:
                window.blit(Winner.surface_Lose, (450, 200))
        if Gold_Dog.x + 50 >= WINDOWWIDTH and (Winner.dem == 0 or Winner.dem == 5):
            window.blit(Winner.surface5, (Winner.x, Winner.y))
            Winner.dem = 5
            if Winner.dem == Character_Select.choice:
                window.blit(Winner.surface_Victory, (450, 200))
            else:
                window.blit(Winner.surface_Lose, (450, 200))
        if Grey_Cat.x + 50 >= WINDOWWIDTH and (Winner.dem == 0 or Winner.dem == 6):
            window.blit(Winner.surface6, (Winner.x, Winner.y))
            Winner.dem = 6
            if Winner.dem == Character_Select.choice:
                window.blit(Winner.surface_Victory, (450, 200))
            else:
                window.blit(Winner.surface_Lose, (450, 200))


Winner = Winner()

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    window.fill(WHITE)

    if Start.start == True:
        Start.draw()

    if Map_Select.start == True:
        Map_Select.draw()

    if Character_Select.start == True:
        Character_Select.draw()

    if Ready.start:
        Ready.draw()

    if Game.start == True:
        Game.update()
        Winner.draw()
        time.sleep(0.07)

    if Pause.start == True:
        Pause.draw()

    pygame.display.update()
    fpsClock.tick(FPS)


