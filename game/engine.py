import pygame
import sys
import random
import settings

class Block(pygame.sprite.Sprite): # classe base
    def __init__(self, base_images_path, number_of_images, x_pos, y_pos):
        super().__init__()
        self.sprites = []

        for i in range(number_of_images):
            image_path = base_images_path + str(i + 1) + ".png"
            self.sprites.append(pygame.image.load(image_path))

        self.current_sprite = 0
        self.image = self.sprites[self.current_sprite]

        self.rect = self.image.get_rect()
        self.rect.center = [x_pos, y_pos]


class Spaceship(Block):
    def __init__(self, base_images_path, number_of_images, x_pos, y_pos, speed, sprite_speed):
        super().__init__(base_images_path, number_of_images, x_pos, y_pos)
        self.speed = speed  # define a velocidade da espaçonave
        self.sprite_speed = sprite_speed # define a velocidade da troca de sprites
        self.movement_y = 0  # define a movimentação da espaçonave no eixo y
        self.movement_x = 0  # define a movimentação da espaçonave no eixo x

    # função para limitar até onde a espaçonave pode ir
    def screen_constrain(self):
        if self.rect.top <= 0:  
            self.rect.top = 0
        if self.rect.bottom >= settings.screen_height:
            self.rect.bottom = settings.screen_height 
        if self.rect.left <= 0:
            self.rect.left = 0
        if self.rect.right >= settings.screen_width:
            self.rect.right = settings.screen_width
    
    def update(self):
        self.rect.y += self.movement_y  # movimenta a espaçonave np eixo y
        self.rect.x += self.movement_x  # movimenta a espaçonave no eixo x
        
        self.current_sprite += self.sprite_speed

        if self.current_sprite >= len(self.sprites):
            self.current_sprite = 0

        self.image = self.sprites[int(self.current_sprite)]
        
        self.screen_constrain() 


class GameManager():
    def __init__(self, spaceship_group):
        self.spaceship_group = spaceship_group
    
    def run_game(self):
        # Desenha os objetos do jogo
        self.spaceship_group.draw(settings.screen)

        # Atualiza os objetos do jogo
        self.spaceship_group.update()