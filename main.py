import json
from game_entities import *
import pygame


COLOURS = {
    'HTML Gainsboro' : (220, 220, 220),
    'Mango' : (244, 187, 68)
}

def draw(window, entities):
    window.fill(COLOURS['HTML Gainsboro'])

    foods = entities['Foods']

    for food in foods:
        food_rect = pygame.Rect(food.x, food.y, food.w, food.h)
        pygame.draw.rect(window, food.colour, food_rect)

    pygame.display.update()

def root_surface(settings):
    root = pygame.display.set_mode(
        (settings['game-width'], settings['game-height']))
    pygame.display.set_caption("Turrent-AI")

    return root

def handle_events():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            return  False
    return True

def main():
    
    with open('settings.json') as settings_file:
        settings = json.load(settings_file)
    
    root = root_surface(settings['global'])

    clock = pygame.time.Clock()
    run = True

    entities = {}
    food = Food(50, 50, 50, 50, COLOURS['Mango'])
    entities['Foods'] = []
    entities['Foods'].append(food)

    while run:
        clock.tick(settings['global']['game-fps'])
        run = handle_events()
        draw(root, entities)

    pygame.quit()

if __name__ == '__main__':
    main()


