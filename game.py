import random

import pygame
import pygame.examples.midi
import pytmx
import pyscroll
from math import sqrt
from math import pow

from mermaid import Player
from menu import *

red = (255, 0, 0)




class Game:

    def __init__(self):
        # definir si notre jeu a commencé ou non
        self.is_playing = False
        # creer la fenetre du jeu
        self.screen = pygame.display.set_mode((800, 800))
        self.life_index = 500
        icon = pygame.image.load('asperia.jpg')
        pygame.display.set_icon(icon)
        pygame.display.set_caption("WAH - tresor hunting ")

        # charger la carte (tmx)
        tmx_data = pytmx.util_pygame.load_pygame('map.tmx')
        map_data = pyscroll.data.TiledMapData(tmx_data)
        map_layer = pyscroll.orthographic.BufferedRenderer(map_data, self.screen.get_size())
        map_layer.zoom = 1




        # generer un joueur
        player_position = tmx_data.get_object_by_name("pp")
        self.player = Player(player_position.x, player_position.y)

        #definir une liste qui va stocker les rectangles de collision
        self.walls = []

        for obj in tmx_data.objects:
            if obj.type == "collision":
                self.walls.append(pygame.Rect(obj.x, obj.y, obj.width, obj.height))

        # dessiner le groupe de calques
        self.group = pyscroll.PyscrollGroup(map_layer=map_layer, default_layer=10)
        self.group.add(self.player)

        # cree la position du tresor
        self.tresor_position_x = random.randrange(32, 766, 23)
        self.tresor_position_y = random.randrange(112, 681, 18)
        self.tresor = 30


    def calcul_distance (self):
        distance = sqrt(pow(self.tresor_position_x-self.player.position.x, 2) + pow(self.tresor_position_y-self.player.position.y,2))

    def message_to_screen(self, msg, color):
        self.screen_text = self.font.render(msg, True, color)
        screen.blit(self.screen_text, [400, 400])

    message_to_screen("You lose")


    def handle_input(self):

        pressed = pygame.key.get_pressed()
        if pressed[pygame.K_UP]:
            self.player.position
            x_old = self.player.position[0]
            y_old = self.player.position[1]
            old_distance = sqrt(pow(self.tresor_position_x - x_old, 2) + pow(self.tresor_position_y - y_old, 2))
            self.player.move_up()
            self.player.change_animation('up')
            x_new = self.player.position[0]
            y_new = self.player.position[1]
            new_distance = sqrt(pow(self.tresor_position_x - x_new, 2) + pow(self.tresor_position_y - y_new, 2))
            if old_distance < new_distance:
                print("NO, GO BACK!")
            elif old_distance > new_distance:
                print("YES, KEEP GOING!")
            if x_new == self.tresor_position_x and y_new == self.tresor_position_y:
                print("YOU WON!!!!")

            self.life_index = self.life_index - 4
            print(self.life_index)

        elif pressed[pygame.K_DOWN]:
            self.player.position
            x_old = self.player.position[0]
            y_old = self.player.position[1]
            old_distance = sqrt(pow(self.tresor_position_x - x_old, 2) + pow(self.tresor_position_y - y_old, 2))
            self.player.move_down()
            self.player.change_animation('down')
            x_new = self.player.position[0]
            y_new = self.player.position[1]
            new_distance = sqrt(pow(self.tresor_position_x - x_new, 2) + pow(self.tresor_position_y - y_new, 2))
            if old_distance < new_distance:
                print("NO, GO BACK!")
            elif old_distance > new_distance:
                print("YES, KEEP GOING!")
            if x_new == self.tresor_position_x and y_new == self.tresor_position_y:
                print("YOU WON!!!!")
            self.life_index = self.life_index - 4
            print(self.life_index)

        elif pressed[pygame.K_LEFT]:
            self.player.position
            x_old = self.player.position[0]
            y_old = self.player.position[1]
            old_distance = sqrt(pow(self.tresor_position_x - x_old, 2) + pow(self.tresor_position_y - y_old, 2))
            self.player.move_left()
            self.player.change_animation('left')
            x_new = self.player.position[0]
            y_new = self.player.position[1]
            new_distance = sqrt(pow(self.tresor_position_x - x_new, 2) + pow(self.tresor_position_y - y_new, 2))
            if old_distance < new_distance:
                print("NO, GO BACK!")
            elif old_distance > new_distance:
                print("YES, KEEP GOING!")
            if x_new == self.tresor_position_x and y_new == self.tresor_position_y:
                print("YOU WON!!!!")
            self.life_index = self.life_index - 4
            print(self.life_index)


        elif pressed[pygame.K_RIGHT]:
            self.player.position
            x_old = self.player.position[0]
            y_old = self.player.position[1]
            old_distance = sqrt(pow(self.tresor_position_x - x_old, 2) + pow(self.tresor_position_y - y_old, 2))
            self.player.move_right()
            self.player.change_animation('right')
            x_new = self.player.position[0]
            y_new = self.player.position[1]
            new_distance = sqrt(pow(self.tresor_position_x - x_new, 2) + pow(self.tresor_position_y - y_new, 2))
            if old_distance < new_distance:
                print("NO, GO BACK!")
            elif old_distance > new_distance:
                print("YES, KEEP GOING!")
            if x_new == self.tresor_position_x and y_new == self.tresor_position_y:
                print("YOU WON!!!!")
            self.life_index = self.life_index - 4
            print(self.life_index)


    def update(self):
        self.group.update()

        #verification de la collision
        for sprite in self.group.sprites():
            if sprite.feet.collidelist(self.walls) > -1:
                sprite.move_back()

    font = pygame.font.SysFont(None, 25)



    def run(self, game=None):
        clock = pygame.time.Clock()
        font = pygame.font.Font(pygame.font.get_default_font(), 24)
        lives = 5
        heart_image = pygame.image.load('heart.png')


        # la boucle du jeu

        running = True
        x = 400
        y = 400

        tmx_data = pytmx.util_pygame.load_pygame('map.tmx')
        while running:

            screen = pygame.display.set_mode((800, 800))
            opening = pygame.image.load('asperia.jpg')


            self.player.save_location()
            self.handle_input()
            self.update()
            self.group.center(self.player.rect.center)
            self.group.draw(self.screen)


            # afficher le tresor
            pygame.draw.rect(self.screen, (255, 0, 0), (self.tresor_position_x, self.tresor_position_y, self.tresor, self.tresor))


            # lives
            for l in range(lives):
                screen.blit(heart_image, (0+ (l*50), 30))

            pygame.display.flip()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

            clock.tick(20)

        pygame.quit()

