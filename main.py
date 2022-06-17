import pygame
from pygame.locals import *
from Modules import pytmx

tilemap0 = pytmx.TiledMap('Resources/grass/map1.tmx')

class colors:

    def __init__(self):

        self.palette = {

            'BLACK' : (0, 0, 0),
            'WHITE' : (255, 255, 255)

        }

    def get_color(self, color):
        return(self.palette[color])

class text:

    def __init__(self, string, position, color):

        self.font_name = 'arial'
        self.font_size = 12
        self.string = string
        self.position = position
        self.color = color

        self.set_font()
        self.render()

    def set_font(self):
        self.font = pygame.font.SysFont(self.font_name, self.font_size)

    def render(self):
        self.img = self.font.render(self.string, True, self.color)
        self.rect = self.img.get_rect()
        self.rect.topleft = self.position

    def draw(self, screen):
        screen.blit(self.img, self.rect)

class scene:

    def __init__(self):

        self.next_id = self

    def process_input(self, events, keys):
        pass

    def update(self):
        pass

    def render(self, screen):
        pass

    def handoff(self, next_id):
        self.next_id = next_id

    def stop(self):
        pygame.quit()

class menu(scene):

    def __init__(self):
        scene.__init__(self)

        self.txt0 = text('Puddle Lane', (10, 10), (colors().get_color('WHITE')))

    def process_input(self, events, keys):
        pass

    def update(self):
        pass

    def render(self, screen):

        self.txt0.draw(screen)

class game(scene):

    def __init__(self):
        scene().__init__()

    def process_input(self, events, keys):
        pass

    def update(self):
        pass

    def render(self, screen):
        pass

class app:

    def __init__(self):

        pygame.init()
        self.screen = pygame.display.set_mode((640, 480))
        pygame.display.set_caption('Puddle Lane Farm')
        
        self.clock = pygame.time.Clock()

    def main(self):

        self.active_scene = game()
        
        while self.active_scene != None:

            self.keys = pygame.key.get_pressed()
            self.filtered_events = []
            self.quit = False

            for event in pygame.event.get():

                if event.type == pygame.QUIT:
                    self.quit = True

                if self.quit == True:
                    self.active_scene.stop()
                else:
                    self.filtered_events.append(event)

            self.active_scene.process_input(self.filtered_events, self.keys)
            self.active_scene.update()
            self.active_scene.render(self.screen)

            self.active_scene = self.active_scene.next_id

            pygame.display.flip()
            self.clock.tick(24)

        pygame.quit()
        exit()

if __name__ == "__main__":
    app().main()