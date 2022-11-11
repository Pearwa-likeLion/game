import pygame ,sys
from ui import UI
from setting import *
from level import Level
from overworld import Overworld
from button import Button
import time
import menu
import item

pygame.display.set_caption("Menu")

BG = pygame.image.load("./assets/level_0.png")

def get_font(size): # Returns Press-Start-2P in the desired size
    return pygame.font.Font("./assets/font.ttf", size)

class Game:
    def __init__(self):
        
        #game.attributes
        self.max_level = 5
        self.max_health = 100 #1
        self.cur_health = 100 #2
        self.coins = 0 #maybe 3
        
        #audio
        self.level_bg_music = pygame.mixer.Sound('./audio/level_music.wav')
        self.overworld_bg_music = pygame.mixer.Sound('./audio/overworld_music.wav')
        
        #overworld creation  
        self.overworld = Overworld(0,self.max_level,screen,self.create_level) #การสลับไป level ต่างๆ
        self.status = 'menu'
        self.overworld_bg_music.play(loops= -1) 
        self.overworld_bg_music.set_volume(0.5)
        
       
        
        #user interface #9
        self.ui = UI(screen)
        
    def create_level(self,current_level):
        self.level = Level(current_level,screen,self.create_overworld,self.change_coins,self.change_health) #25
        self.status = 'level'     
        self.overworld_bg_music.stop()
        self.level_bg_music.play(loops= -1)
        
    def create_overworld(self,current_level,new_max_level):
        self.level_bg_music.stop()
        if new_max_level > self.max_level :
            self.max_level = new_max_level
        self.overworld  = Overworld(current_level,self.max_level,screen,self.create_level)
        self.status = 'overworld'   
        self.overworld_bg_music.play(loops= -1) 

    def change_coins(self,amount):
        self.coins += amount #26 นับเหรียญเพิ่ม

    def change_health(self,amount):
        self.cur_health += amount
    
    
    def check_gameover(self):
        if self.cur_health <= 0 or self.max_level == 6:
            self.cur_health = 100
            self.coins = 0
            self.max_level = 0
            self.overworld = Overworld(0,self.max_level,screen,self.create_level) #การสลับไป level ต่างๆ
            self.status = 'overworld'
            self.level_bg_music.stop()
            self.overworld_bg_music.play(loops= -1)

    
    def run(self):
        if self.status == 'menu':
            self.status = menu.main_menu()
        elif self.status == 'option':
            self.status = menu.options()
        elif self.status == 'board':
            self.status = menu.leaderboard()
        elif self.status == 'overworld':
            self.overworld.run()
        else:
            self.level.run()
            self.ui.show_health(self.cur_health,self.max_health) #10 ui แสดงแถบเลือด
            self.ui.show_coins(self.coins) #14 ui แสดงค่าเหรียญที่มี
            self.check_gameover()
            
#pygame program setup
pygame.init()
BG = pygame.image.load("C:/Users/PC/Documents/menugame/assets/Background.png")
screen = pygame.display.set_mode((screen_width,screen_height))
clock = pygame.time.Clock()
game = Game()
while True:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
           pygame.quit()
           sys.exit()

    screen.fill('grey')
    
    game.run()
    
    pygame.display.update()
    clock.tick(60)
    
    
    #แถบเลือด ภาพที่ใช้เป็นแถบเลือดกว้าง 152 ก็ต้องปรับให้สอดคล้องกับแถบที่จะสร้างขึ้นใหม่
    
