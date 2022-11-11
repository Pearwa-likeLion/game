import pygame, sys
from button import Button

pygame.init()

SCREEN = pygame.display.set_mode((1280, 720))
pygame.display.set_caption("Menu")

BG = pygame.image.load("C:/Users/PC/Documents/menugame/assets/level_0.png")

def get_font(size): # Returns Press-Start-2P in the desired size
    return pygame.font.Font("assets/font.ttf", size)

def play():
    while True:
        PLAY_MOUSE_POS = pygame.mouse.get_pos()

        SCREEN.fill("black")

        PLAY_TEXT = get_font(45).render("This is the PLAY screen.", True, "White")
        PLAY_RECT = PLAY_TEXT.get_rect(center=(640, 260))
        SCREEN.blit(PLAY_TEXT, PLAY_RECT)

        PLAY_BACK = Button(image=None, pos=(640, 460), 
                            text_input="BACK", font=get_font(75), base_color="White", hovering_color="Green")

        PLAY_BACK.changeColor(PLAY_MOUSE_POS)
        PLAY_BACK.update(SCREEN)

        for event in pygame.event.get():
            keys = pygame.key.get_pressed()
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BACK.checkForInput(PLAY_MOUSE_POS):
                    main_menu()
            if keys[pygame.K_ESCAPE]:
                    main_menu()

        pygame.display.update()
    
def options():
    status = 'option'
    while True:
        OPTIONS_MOUSE_POS = pygame.mouse.get_pos()

        SCREEN.fill("white")

        #created by
        INFO1_TEXT = get_font(45).render("Created by", True, "Black")
        INFO1_RECT = INFO1_TEXT.get_rect(center=(640, 200))
        SCREEN.blit(INFO1_TEXT, INFO1_RECT)

        #name id
        INFO2_TEXT = get_font(55).render("65010782 Pearwa Tussanapoom", True, "Black")
        INFO2_RECT = INFO2_TEXT.get_rect(center=(640, 350))
        SCREEN.blit(INFO2_TEXT, INFO2_RECT)

        OPTIONS_BACK = Button(image=None, pos=(640, 550), 
                            text_input="BACK", font=get_font(75), base_color="Black", hovering_color="Green")

        OPTIONS_BACK.changeColor(OPTIONS_MOUSE_POS)
        OPTIONS_BACK.update(SCREEN)

        for event in pygame.event.get():
            keys = pygame.key.get_pressed()
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if OPTIONS_BACK.checkForInput(OPTIONS_MOUSE_POS):
                    status = 'menu'
            if keys[pygame.K_ESCAPE]:
                    status = 'menu'
        if status != 'option':
            break      
        pygame.display.update()
    return status
        
def leaderboard():
    status = 'board'
    while True:
        PLAY_MOUSE_POS = pygame.mouse.get_pos()

        SCREEN.fill("black")

        PLAY_TEXT = get_font(45).render("This is the Leaderboard screen.", True, "White")
        PLAY_RECT = PLAY_TEXT.get_rect(center=(640, 260))
        SCREEN.blit(PLAY_TEXT, PLAY_RECT)

        PLAY_BACK = Button(image=None, pos=(640, 460), 
                            text_input="BACK", font=get_font(75), base_color="White", hovering_color="Green")

        PLAY_BACK.changeColor(PLAY_MOUSE_POS)
        PLAY_BACK.update(SCREEN)

        for event in pygame.event.get():
            keys = pygame.key.get_pressed()
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BACK.checkForInput(PLAY_MOUSE_POS):
                    status = 'menu'
            if keys[pygame.K_ESCAPE]:
                    status = 'menu'
        if status != 'board':
            break
        pygame.display.update()
    return status

def main_menu():
    while True:
        SCREEN.blit(BG, (0, 0))
        status = 'menu'

        MENU_MOUSE_POS = pygame.mouse.get_pos()

        MENU_TEXT = font = pygame.font.Font("assets/ThaleahFat.ttf", 50).render("Super Romeo Adventure", True, "#FFFFFF")
        MENU_RECT = MENU_TEXT.get_rect(center=(1000, 75))
        MENUbg_TEXT = font = pygame.font.Font("assets/ThaleahFat.ttf", 50).render("Super Romeo Adventure", True, "#000000")
        MENUbg_RECT = MENUbg_TEXT.get_rect(center=(1000, 82))
        
        LOGOGAME = pygame.image.load("./logogame/logogame.png").convert_alpha()
        LOGO_RECT = LOGOGAME.get_rect(center=(200, 480))
        LOGOGAMEBG = pygame.image.load("./logogame/logobg.png").convert_alpha()
        LOGOBG_RECT = LOGOGAMEBG.get_rect(center=(230, 480))
        

        PLAY_BUTTON = Button(image=pygame.image.load("assets/Play Rect.png"), pos=(1000, 180), 
                            text_input="PLAY", font=get_font(25), base_color="#FFFFFF", hovering_color="Black")
        LEARDEBOARD_BUTTON = Button(image=pygame.image.load("assets/Quit Rect.png"), pos=(1000, 330), 
                            text_input="LEARDERBOARD", font=get_font(25), base_color="#FFFFFF", hovering_color="Black")
        OPTIONS_BUTTON = Button(image=pygame.image.load("assets/Play Rect.png"), pos=(1000, 480), 
                            text_input="Info", font=get_font(25), base_color="#FFFFFF", hovering_color="Black")
        QUIT_BUTTON = Button(image=pygame.image.load("assets/Quit Rect.png"), pos=(1000, 630), 
                            text_input="QUIT", font=get_font(25), base_color="#FFFFFF", hovering_color="Black")
        
        SCREEN.blit(MENUbg_TEXT, MENUbg_RECT)
        SCREEN.blit(MENU_TEXT, MENU_RECT)
        SCREEN.blit(LOGOGAMEBG, LOGOBG_RECT)
        SCREEN.blit(LOGOGAME, LOGO_RECT)
        

        for button in [PLAY_BUTTON, LEARDEBOARD_BUTTON ,OPTIONS_BUTTON, QUIT_BUTTON]:
            button.changeColor(MENU_MOUSE_POS)
            button.update(SCREEN)
        
        for event in pygame.event.get():
            key = pygame.key.get_pressed()
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if  key[pygame.K_ESCAPE]:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BUTTON.checkForInput(MENU_MOUSE_POS):
                    status = 'overworld'
                if OPTIONS_BUTTON.checkForInput(MENU_MOUSE_POS):
                    status = 'option'
                if LEARDEBOARD_BUTTON.checkForInput(MENU_MOUSE_POS):
                    status = 'board'
                if QUIT_BUTTON.checkForInput(MENU_MOUSE_POS):
                    pygame.quit()
                    sys.exit()

        pygame.display.update()
        return status
# main_menu()