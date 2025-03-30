import pygame

def draw(surface: pygame.Surface, p1: tuple[int,int], p2: tuple[int,int]):
    if p1 is None: #if  we can't draw a line, draw 1 point
        pygame.draw.rect(surface, pygame.Color('black'), (p2[0], p2[1], 1, 1))
    else:
        pygame.draw.aaline(surface, pygame.Color('black'), p1, p2)

def main():
    pygame.init()
    screen_x, screen_y = 1280 , 720
    screen = pygame.display.set_mode((screen_x, screen_y))
    screen.fill(pygame.Color('white'))
    
    clock = pygame.time.Clock()
    running = True
    
    mouse_is_down = False
    old_pos = None

    while running:
        for event in pygame.event.get():
            print(event)

            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_is_down = True
            if event.type == pygame.MOUSEBUTTONUP:
                mouse_is_down = False
                old_pos = None
            if event.type == pygame.MOUSEMOTION:
                if mouse_is_down:
                    new_pos = pygame.mouse.get_pos()
                    draw(screen, old_pos, new_pos)
                    old_pos = new_pos
            if event.type == pygame.QUIT:
                running = False

        pygame.display.flip()
        clock.tick(60)  # limits FPS to 60

    pygame.quit()

main()