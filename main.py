import json
import pygame
import random


from game_entities import *

COLOURS = {
    'HTML Gainsboro' : (220, 220, 220),
    'Mango' : (244, 187, 68)
}

FOOD_WIDTH, FOOD_HEIGHT = 5, 5

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
    entities['Foods'] = []


    while run:
        clock.tick(settings['global']['game-fps'])
        run = handle_events()

        while len(entities['Foods']) < settings['game']['max-num-food']:
            food = Food(random.randint(0, settings['global']['game-width']), 
            random.randint(0, settings['global']['game-height']), 
            FOOD_WIDTH, 
            FOOD_HEIGHT, 
            COLOURS['Mango'])
            entities['Foods'].append(food)

        draw(root, entities)

    pygame.quit()

if __name__ == '__main__':
    main()


