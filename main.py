import pygame

def main():
    pygame.init()
    screen_x = 1280
    screen_y = 720
    screen = pygame.display.set_mode((screen_x, screen_y))
    clock = pygame.time.Clock()
    running = True
    
    mouse_is_down = False

    screen.fill((255,255,255))
    while running:
        # poll for events
        # pygame.QUIT event means the user clicked X to close your window
        for event in pygame.event.get():
            print(event)

            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_is_down = True
            if event.type == pygame.MOUSEBUTTONUP:
                mouse_is_down = False
            if event.type == pygame.MOUSEMOTION:
                if mouse_is_down:
                    pos = pygame.mouse.get_pos()
                    pygame.draw.rect(screen, (0,0,8), (pos[0], pos[1], 10, 10))
            if event.type == pygame.QUIT:
                running = False

        
        pygame.display.flip()
        clock.tick(60)  # limits FPS to 60

    pygame.quit()

main()