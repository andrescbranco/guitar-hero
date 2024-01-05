import pygame
import os
from keys import keys
from pygame import mixer
from lives_tracker import LivesTracker

WIDTH,HEIGHT = 1080, 720
FPS = 60

pygame.font.init()

score = 0
streak = 0


WIN = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("Guitar Hero")

RECT = pygame.Rect(385,0, 280, 720)
venue_frames = [pygame.image.load(os.path.join('Assets/GIF', f'frame_{i:02}_delay-0.1s.png')) for i in range(45)]

lives_tracker = LivesTracker(WIN)

def draw_window(venue_frame):
    VENUE = pygame.transform.scale(venue_frame, (1080,720))
    WIN.fill((255,255,255))
    WIN.blit(VENUE, (0,0))
    pygame.draw.rect(WIN,(0,0,0),RECT)
    k = pygame.key.get_pressed()
    lives_tracker.draw()
    global score
    draw_score(score)
    global streak
    draw_streak(streak)

    for key in keys:
        if k[key.key]:
            button = pygame.image.load(os.path.join('Assets', key.image_2))
            pygame.transform.scale(button,(40,20))
            WIN.blit(button,(key.x,key.y))
            key.handled = False
        if not k[key.key]:
            button = pygame.image.load(os.path.join('Assets', key.image_1))
            pygame.transform.scale(button,(40,20))
            WIN.blit(button,(key.x,key.y))
            key.handled = True

    for rect in map_rect:
        button = pygame.image.load(os.path.join('Assets', rect[1]))
        WIN.blit(button, rect[0])
        rect[0].y += 3
        if rect[0].y >= 720:
            lives_tracker.lose_life()
            streak = 0
            map_rect.remove(rect)

        for key in keys:
            if key.rect.colliderect(rect[0]) and not key.handled:
                map_rect.remove(rect)
                key.handled = True
                score += 10 
                streak += 1
                break
        
            
    pygame.display.update()

def draw_score(score):
    font = pygame.font.Font("PixeloidSans-mLxMm.ttf", 30)
    score_text = font.render(f'Score: {score}', True, (255, 255, 255)) 
    WIN.blit(score_text, (20, 500))

def draw_streak(streak):
    font = pygame.font.Font("PixeloidSans-mLxMm.ttf", 30)
    streak_text = font.render(f'Streak: {streak}', True, (255, 255, 255))
    WIN.blit(streak_text, (20, 550)) 

def load(map):

    button_mapping = {
        0 : 'Green Button 0.png',
        1: 'Red Button.png',
        2:'Yellow Button 1.png',
        3:'Blue Button 1.png'
    }

    rects = []
    # mixer.music.load('Music/' + map + '.mp3')
    # mixer.music.play()
    f = open(map + '.txt', 'r')
    data = f.readlines()

    for y in range(len(data)):
        for x in range(len(data[y])):
            if data[y][x] == '0' and x in button_mapping:
                image = button_mapping[x]
                rect = pygame.Rect(keys[x].x + 10, y*-100, 30, 30)
                rects.append((rect, image))

    return rects

map_rect = load('Eslabo Armado, Peso Pluma - Ella Baila Sola')


def display_game_over(WIN):
    font = pygame.font.Font("PixeloidSans-mLxMm.ttf", 60)
    game_over_text = font.render('Game Over', True, (255, 0, 0))
    WIN.blit(game_over_text, (WIDTH // 2 - game_over_text.get_width() // 2, HEIGHT // 2 - game_over_text.get_height() // 2))
    pygame.display.update()

def main():
    frame_count = 0
    game_over = False

    clock = pygame.time.Clock()
    run = True
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
    
        if lives_tracker.is_game_over():
            game_over = True
            display_game_over(WIN)
            break

        current_frame = venue_frames[int (frame_count/10) % len(venue_frames)]
        frame_count += 1

        draw_window(current_frame)

    if game_over:
        pygame.time.wait(3000)

    pygame.quit()

if __name__ == "__main__":
    main()