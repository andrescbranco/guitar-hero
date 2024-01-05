import pygame

class Key():
    def __init__(self,x,y,image_1,image_2,key):
        self.x = x
        self.y = y
        self.image_1 = image_1
        self.image_2 = image_2
        self.key = key
        self.rect = pygame.Rect(self.x, self.y, 40, 20)
        self.handled = False

keys = [
    Key(400,670,'Green Button Pressed.png', 'Green Button Pressed 2.png', pygame.K_a),
    Key(475,670,'Red Button Pressed.png', 'Red Button Pressed 2.png', pygame.K_s),
    Key(550,670,'Yellow Button Pressed.png', 'Yellow Button Pressed 2.png', pygame.K_d),
    Key(620,670,'Blue Button Pressed.png', 'Blue Button Pressed 2.png', pygame.K_f)
]
