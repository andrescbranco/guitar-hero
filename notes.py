# from pygame import mixer
# import pygame

# class Note:

    # def __init__(self, music):
    #     self.music = music
    
    # def load(map):
    #     mixer.music.load(map + '.wav')
    #     mixer.music.play()
    #     f = open('./Music/' + map + '.txt', 'r')
    #     data = f.readlines()

    #     for y in range(len(data)):
    #         for x in range(len(data[y])):
    #             if data[x][y] == '0':
    #                 pygame.draw.rect(WIN, (100,0,0), (x*20,y*20,20,20),)

    # load('Ella Baila Sola - (Video Oficial) - Eslabon Armado y Peso Pluma - DEL Records 2023')



#     def draw(self, screen):
#         screen.blit(self.image, (self.x, self.y))

#     def update(self):
#         self.y += note_speed  # Define note_speed based on game speed

# # Load note images
# note_image = pygame.image.load('path_to_note_image.png')

# # Initialize notes
# notes = [Note(start_x, start_y, note_image) for _ in range(number_of_notes)]  # Define these variables as needed

# # In game loop:
# for note in notes:
#     note.update()
#     note.draw(screen)