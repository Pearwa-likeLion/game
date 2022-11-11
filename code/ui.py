import pygame

class UI: #4
    def __init__(self,surface):
        #setup
        self.display_surface = surface
        
        #health
        self.health_bar = pygame.image.load('./graphics/ui/health_bar.png').convert_alpha() #5
        self.health_bar_topleft = (54,39) #สร้างแถบที่พิกัดนี้ จะตรงรูปพอดี #18
        self.bar_max_width = 152 #19
        self.bar_height = 4 #20
        
        #coins
        self.coin = pygame.image.load('./graphics/ui/coin.png').convert_alpha() #6
        self.coin_rect = self.coin.get_rect(topleft = (50,61)) #11 ตำแหน่งของเหรียญ 
        self.font = pygame.font.Font('./graphics/ui/ARCADEPI.ttf',30) #15
        
    def show_health(self,current,full): #7 อันนี้ต้องโชว์ถ้ารันเกมแบบในด่าน
        self.display_surface.blit(self.health_bar,(20,10)) #12 ตำแหน่งของแถบเลือด
        current_heath_ratio = current / full #21 
        current_bar_width = self.bar_max_width * current_heath_ratio #22 ขนาดความกว้างบาร์
        health_bar_rect = pygame.Rect((self.health_bar_topleft),(current_bar_width,self.bar_height)) #23
        pygame.draw.rect(self.display_surface,'#dc4949',health_bar_rect) #วาดแถบเลือด
    
    
    def show_coins(self,amount): #8
        self.display_surface.blit(self.coin,self.coin_rect) #13
        coin_amount_surf = self.font.render(str(amount),False,'#33323d')
        coin_amount_rect = coin_amount_surf.get_rect(midleft = (self.coin_rect.right+3,self.coin_rect.centery))    #16 แสดงค่าเหรียญที่เรามีอยู่ปัจจุบัน
        self.display_surface.blit(coin_amount_surf,coin_amount_rect) #17
        
        