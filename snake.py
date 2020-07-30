# Inspired in https://www.youtube.com/watch?v=H4TXHI9BRCQ

import pygame
import random
from numbers_to_scoreboard import get_numbers_to_scoreboard
from pygame.locals import *

UP = 0
RIGHT = 1
DOWN = 2
LEFT = 3
KEYDOWN = 2
KEY_UP = 273
KEY_DOWN = 274
KEY_RIGHT = 275
KEY_LEFT = 276

# Retorna uma posição aleatoria da grid, sendo alinhando com o padrão de 10x10
def random_grid_position():
  x = random.randint(0, 590)
  y = random.randint(0, 590)

  # Usando // é feita uma divisão interia, ou seja [17 / 5 = 3]
  return (x//10 * 10, y//10 * 10)

# Verifica se houve colisão entre 2 celulas
def check_colision(pos1, pos2):
  return (pos1[0] == pos2[0]) and (pos1[1] == pos2[1])

# Pega a nova posição da cobra
def new_snake_position(actual_pos, direction):
  if direction in [DOWN, RIGHT]:
    new_position = actual_pos + 10

    # Caso tenha saido da tela
    if new_position >= 600:
      new_position = 0
  if direction in [UP, LEFT]:
    new_position = actual_pos - 10

    # Caso tenha saido da tela
    if new_position < 0:
      new_position = 590

  return new_position

# Retorna os Dados para a Exibição do Score
def get_scoreboard(score):
  string_score = str(score)

  scoreboard = []

  for index, number in enumerate(string_score):
    scoreboard.insert(len(scoreboard), get_numbers_to_scoreboard(int(number), index))

  return scoreboard

# Comando obrigatório, "instancia" o pygame
pygame.init()

# Monta a tela, passando uma "tupla" com as dimensões
screen = pygame.display.set_mode((600, 600))

# Define um titulo para a janela
pygame.display.set_caption("Snake")

# Define a cobra
snake = [(200, 200), (210, 200), (220, 200)]
# Define o corpo da cobra
# Define que as dimensões de cada "quadradinho" da cobra será 10x10
snake_skin = pygame.Surface((10, 10))
# Define a cor da cobra, usando RGB
snake_skin.fill((4,125,55))

# Define a textura da maçã
apple = pygame.Surface((10, 10))
# Define a cor da maçã
apple.fill((255,0,0))
# Define a posição da maçã, usando 590 como limite, pq a tela tem 600 e a maçã tem 10
apple_pos = random_grid_position()

# Define a textura do score
score_texture = pygame.Surface((10, 10))
score_texture.fill((255,255,255))

# Define a direção que a cobra está andando
my_direction = LEFT

# Define um objeto clock, para controlar o limite de fps
clock = pygame.time.Clock()

# Define o contador pontos
score = 0

# Define o placar
scoreboard = get_scoreboard(score)

# Inicia o Loop Principal do jogo
while True:
  # Limite a 20 fps
  clock.tick(20)

  # Faz um loop pelos eventos
  for event in pygame.event.get():
    # Sai do jogo
    if event.type == QUIT:
      pygame.quit()
    # Controles para movimentar a cobra
    # As verificações também impedem que ela se mova na direção oposta da atual
    if event.type == KEYDOWN:
      if event.key == KEY_UP and my_direction != DOWN:
        my_direction = UP
      if event.key == KEY_DOWN and my_direction != UP:
        my_direction = DOWN
      if event.key == KEY_LEFT and my_direction != RIGHT:
        my_direction = LEFT
      if event.key == KEY_RIGHT and my_direction != LEFT:
        my_direction = RIGHT

  # Verifica se houve colisão da cobra com a maçã
  # Isso acontece antes da cobra se mover, para que não dê nenhum bug
  if check_colision(snake[0], apple_pos):
    # Altera a posição da maçã
    apple_pos = random_grid_position()
    # Adiciona uma nova celula a cobra
    snake.append((snake[len(snake) - 1][0], snake[len(snake) - 1][1]))

  # Verifica se a cabeça colidiu com alguma parte da cobra
  for index, pos in enumerate(snake):
    # Ignora a propria cabeça
    if index != 0:
      # Caso tenha colidido, finaliza o jogo
      if check_colision(snake[0], pos):
        pygame.quit()

  # Movimenta a cobra
  if my_direction == UP:
    snake.insert(0, (snake[0][0], new_snake_position(snake[0][1], UP)))
  if my_direction == DOWN:
    snake.insert(0, (snake[0][0], new_snake_position(snake[0][1], DOWN)))
  if my_direction == LEFT:
    snake.insert(0, (new_snake_position(snake[0][0], LEFT), snake[0][1]))
  if my_direction == RIGHT:
    snake.insert(0, (new_snake_position(snake[0][0], RIGHT), snake[0][1]))

  # Remove o ultimo elemento do array, para dar a impressão de que a cobra se mexeu
  snake.pop(len(snake) - 1)

  # Calcula o novo placar
  new_score = len(snake) - 3

  # Verifica se o score foi alterado
  if new_score != score:
    score = new_score
    scoreboard = get_scoreboard(score)

  # Limpa a tela
  screen.fill((0,0,0))

  # Renderiza o placar
  for number in scoreboard:
    for pos in number:
      screen.blit(score_texture, pos)

  # Renderiza a maçã
  screen.blit(apple, apple_pos)

  # Renderiza a cobra
  for pos in snake:
    # Renderiza cada "quadradinho" da cobra, passando sua "textura" e posição
    screen.blit(snake_skin, pos)

  # Atualiza os dados da tela
  pygame.display.update()
