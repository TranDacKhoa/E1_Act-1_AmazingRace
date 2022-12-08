import pygame, sys, random
import math
import openpyxl
from pygame.locals import *


pygame.init()

BLACK =(0,0,0)
YELLOW = (255,255,0)
RED = (255,30,0)
GREY = (128,128,128)
PINK =(255,123,133)
WHITE = (255,255,255)
GREEN = (0,128,0)
BLUE = (30,144,255)

FPS = 30
fpsClock = pygame.time.Clock()

dem_so_tk=2

WINDOWWIDTH = 1300 # Chiều dài cửa sổ
WINDOWHEIGHT = 650 # Chiều cao cửa sổ

font = pygame.font.SysFont('comicsansms',40)
screen = pygame.display.set_mode((WINDOWWIDTH,WINDOWHEIGHT))
pygame.display.set_caption('Mortal Race')

smallfont1 = pygame.font.SysFont('comicsansms',18)
smallfont = pygame.font.SysFont('comicsansms',25)
mediumfont = pygame.font.SysFont('comicsansms',32)
largefont1 = pygame.font.SysFont('gillsansultra',50)
largefont2 = pygame.font.SysFont('comicsansms',75)
largefont3 = pygame.font.SysFont('gillsansultra',75)

COLOR_INACTIVE = pygame.Color(YELLOW)
COLOR_ACTIVE = pygame.Color(GREEN)

def get_value(cellname):
    filename='login.xlsx'
    wb = openpyxl.load_workbook(filename)
    sheet_login = wb['Sheet1']
    wb.close()
    return str(sheet_login[cellname].value)

def update_value(number,user, password):
    filename='login.xlsx'
    pos_user='A'+str(number)
    pos_password='B'+str(number)
    wb = openpyxl.load_workbook(filename)
    sheet_login = wb['Sheet1']
    sheet_login[pos_user].value = user
    sheet_login[pos_password].value = password
    wb.close()
    wb.save(filename)

def check_login(user,password):
	kt = False
	for i in range (2,11):
		pos_user='A'+str(i)
		pos_password='B'+str(i)
		check_user=get_value(pos_user)
		check_password=get_value(pos_password)
		if user== check_user and password== check_password:
			kt = True
	if kt== True:
		print("Login successfully!!!")
	else:
		print("Username or password is incorrect!!!")



    
def login():
    font = pygame.font.Font(None, 32)
    clock = pygame.time.Clock()
    input_box1 = pygame.Rect(500, 300, 140, 32)
    input_box2 = pygame.Rect(500, 350, 140, 32)
    color_inactive = pygame.Color(YELLOW)
    color_active = pygame.Color(BLUE)
    color1 = color_inactive
    active1 = False
    color2 = color_inactive
    active2 = False
    text1 = ''
    text2 = ''
    text2_sao=''
    login_user=''
    login_password=''
    done = False

    

    global dem_so_tk

    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
            if event.type == pygame.MOUSEBUTTONDOWN:
                # If the user clicked on the input_box rect.
                if input_box1.collidepoint(event.pos):
                    # Toggle the active variable.
                    active1 = not active1
                else:
                    active1 = False
                # Change the current color of the input box.
                color1 = color_active if active1 else color_inactive
            if event.type == pygame.KEYDOWN:
                if active1:
                    if event.key == pygame.K_BACKSPACE:
                        text1 = text1[:-1]
                    else:
                        text1 += event.unicode
            if event.type == pygame.MOUSEBUTTONDOWN:
                # If the user clicked on the input_box rect.
                if input_box2.collidepoint(event.pos):
                    # Toggle the active variable.
                    active2 = not active2
                else:
                    active2 = False
                # Change the current color of the input box.
                color2 = color_active if active2 else color_inactive
            if event.type == pygame.KEYDOWN:
                if active2:
                    if event.key == pygame.K_BACKSPACE:
                        text2 = text2[:-1]
                        text2_sao = text2_sao[:-1]
                    else:
                        text2 += event.unicode
                        text2_sao +='*'

        screen.fill((30, 30, 30))

        txt_surface1 = font.render(text1, True, color1)
        txt_surface2 = font.render(text2_sao, True, color2)
    
        width1 = max(200, txt_surface1.get_width()+10)
        width2 = max(200, txt_surface2.get_width()+10)
        input_box1.w = width1
        input_box2.w = width2

        screen.blit(txt_surface1, (input_box1.x+5, input_box1.y+5))
        screen.blit(txt_surface2, (input_box2.x+5, input_box2.y+5))

        pygame.draw.rect(screen, color1, input_box1, 2)
        pygame.draw.rect(screen, color2, input_box2, 2)

        login_Text=largefont3.render("LOGIN", True, RED)
        user=smallfont.render("Username ", True, BLUE)
        password=smallfont.render("Password ",True, BLUE)
        login_Boxtext=smallfont.render("Login", True, BLACK)
        register_Boxtext=smallfont.render("Create an account?", True, WHITE)
        screen.blit(login_Text,(450,100))
        screen.blit(user,(380,300))
        screen.blit(password,(380,350))
        login_Box = pygame.Surface((400,40))
        login_Box.fill(WHITE)
        login_Box.blit(login_Boxtext,(180,3))
        screen.blit(login_Box,(380,450))
        mouse_x, mouse_y = pygame.mouse.get_pos()
        register_Box = pygame.Surface((230,40))
        register_Box.fill((30,30,30))
        register_Box.blit(register_Boxtext,(0,4))
        screen.blit(register_Box,(500,500))
        mouse_x, mouse_y = pygame.mouse.get_pos()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1 and (500 < mouse_x < 590) and (450 < mouse_y < 490):
                check_login(text1,text2)

            if event.button == 1 and (500 < mouse_x < 730) and (500 < mouse_y < 540):
                register()
        pygame.display.flip()
        clock.tick(30)
                
def register():
    font = pygame.font.Font(None, 32)
    register = True
    register_user = ''
    register_password = ''
    register_password_sao = ''
    register_confirm = ''
    register_confirm_sao = ''
    color_inactive = pygame.Color(BLACK)
    color_active = pygame.Color(RED)
    color3 = color_inactive
    active3 = False
    color4 = color_inactive
    active4 = False
    color5 = color_inactive
    active5 = False


    while register:    
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit() 
                quit()
            register_tab = pygame.Surface((866,500))
            register_tab.fill(WHITE)
            register_Text=largefont1.render("CREATE YOUR ACCOUNT", True, BLACK)
            register_tab.blit(register_Text,(75,75))
            register_input_user = pygame.Rect(400, 200, 140, 32)
            register_input_password = pygame.Rect(400, 250, 140, 32)
            register_input_confirm = pygame.Rect(400, 300, 140, 32)
            user=smallfont.render("Username", True, BLACK)
            password= smallfont.render("Password",True, BLACK)
            confirm= smallfont.render("Repeat password",True, BLACK)
            register_tab.blit(user,(190,200))
            register_tab.blit(password,(190,250))
            register_tab.blit(confirm,(190,300))
            mouse_x, mouse_y = pygame.mouse.get_pos()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if 866 > mouse_x-217 > 826 and 433 > mouse_y-108 > 0 and event.button == 1:
                    register = False
            quit_register = smallfont.render("X", True, BLACK)
            pygame.draw.line(register_tab, BLACK, (0,40), (866,40), 3)
            register_tab.blit(quit_register,(836,5))
            if event.type == pygame.MOUSEBUTTONDOWN:
                # If the user clicked on the input_box rect.
                if event.button == 1 and 350<mouse_x-217<350+200 and 200<mouse_y-108<200+32:
                    # Toggle the active variable.
                    active3 = True
                else:
                    active3 = False
                # Change the current color of the input box.
            color3 = color_active if active3 else color_inactive
            if active3:
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_BACKSPACE:
                        register_user = register_user[:-1]
                    else:
                        register_user += event.unicode
                    
                    
            if event.type == pygame.MOUSEBUTTONDOWN:
                # If the user clicked on the input_box rect.
                if event.button == 1 and 350<mouse_x-217<350+200 and 250<mouse_y-108 <250+32:
                    # Toggle the active variable.
                    active4 = True
                else:
                    active4 = False
                # Change the current color of the input box.
                color4 = color_active if active4 else color_inactive
            if active4:
                if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_BACKSPACE:
                            register_password = register_password[:-1]
                            register_password_sao = register_password_sao[:-1]
                        else:
                            register_password += event.unicode
                            register_password_sao +='*'

            if event.type == pygame.MOUSEBUTTONDOWN:
                # If the user clicked on the input_box rect.
                if event.button == 1 and 350<mouse_x-217<350+200 and 300<mouse_y-108 <300+32:
                    # Toggle the active variable.
                    active5 = True
                else:
                    active5 = False
                # Change the current color of the input box.
                color5 = color_active if active5 else color_inactive
            if active5:
                if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_BACKSPACE:
                            register_confirm = register_confirm[:-1]
                            register_confirm_sao = register_confirm_sao[:-1]
                        else:
                            register_confirm += event.unicode
                            register_confirm_sao +='*'

            txt_register_1 = font.render(register_user, True, color3)
            txt_register_2 = font.render(register_password_sao, True, color4)
            txt_register_3 = font.render(register_confirm_sao, True, color5)
    
            width1 = max(200, txt_register_1.get_width()+10)
            width2 = max(200, txt_register_2.get_width()+10)
            width3 = max(200, txt_register_3.get_width()+10)
            register_input_user.w = width1
            register_input_password.w = width2
            register_input_confirm.w = width3
        
            pygame.draw.rect(register_tab, color3, register_input_user, 2)
            pygame.draw.rect(register_tab, color4, register_input_password, 2)
            pygame.draw.rect(register_tab, color5, register_input_confirm, 2)

            register_tab.blit(txt_register_1, (register_input_user.x+5, register_input_user.y+5))
            register_tab.blit(txt_register_2, (register_input_password.x+5, register_input_password.y+5))
            register_tab.blit(txt_register_3, (register_input_confirm.x+5, register_input_confirm.y+5))

            register_Boxtext=smallfont.render("REGISTER", True, WHITE)
            register_Box = pygame.Surface((410,40))
            register_Box.fill(BLACK)
            register_Box.blit(register_Boxtext,(155,3))
            register_tab.blit(register_Box, (190,350))
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1 and 190<mouse_x-217<190+410 and 350<mouse_y-108 <350+40:
                    if register_confirm == register_password:
                        conclusion= smallfont1.render("Registered successfully!!!",True, RED)
                        register_tab.blit(conclusion,(190,400))
                    else:
                        conclusion= smallfont1.render("Passwords do not match!!!",True, RED)
                        register_tab.blit(conclusion,(300,400))  


            screen.blit(register_tab,(217,108))
            pygame.display.flip()          

        

login()
pygame.quit()

