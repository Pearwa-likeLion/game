import pygame
import level
import player
# import main

vec = pygame.math.Vector2


class Item(pygame.sprite.Sprite):
    def __init__(self, x, y, itemtype, name):
        super().__init__()

        self.ID = itemtype
        self.image = pygame.image.load(name).convert_alpha()
        self.rect = self.image.get_rect()
        self.pos = vec(x, y-17) 
        self.rect.topleft = self.pos

    def update(self,shift):
        self.rect.x += shift

        # hits = self.rect.colliderect(player.rect)

        # if pygame.sprite.collide_rect(self,player):
        #     if hits:
        #         if self.ID == 0:
        #             player.change_health(10)
        #         elif self.ID == 1:
        #             pass

        # self.kill()


    def render(self, display):
        display.blit(self.image, self.pos)



# ID -> 0 -> Coin
# ID -> 1 -> Health

#def update(self,shift):
        
        

        
