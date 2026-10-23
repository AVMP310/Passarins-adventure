import os
import pygame

pygame.init()
pygame.mixer.init()

# Variáveis globais

# Posição dos passarinhos
pos_y_player = 436
pos_x_player = 486
pos_y_inimigo = -50
pos_x_inimigo = 0

# Funções

def carregar_imagem(caminho):
    try:
        imagem = pygame.image.load(caminho)
        return imagem.convert_alpha()
    except pygame.error:
        print(f"Não foi possível carregar a imagem: {caminho}")
        superficie = pygame.Surface((40, 40))
        superficie.fill((255, 0, 0))
        return superficie


def atirar_player():
    global mostrar_fogo_player
    global pos_x_fogo
    global pos_y_fogo

    mostrar_fogo_player = True
    pos_x_fogo = pos_x_player + 20
    pos_y_fogo = pos_y_player + 10

def atirar_inimigo():
    global mostrar_fogo_inimigo
    global pos_x_fogo_inimigo
    global pos_y_fogo_inimigo

    mostrar_fogo_inimigo = True
    pos_x_fogo_inimigo = pos_x_inimigo + 20
    pos_y_fogo_inimigo = pos_y_inimigo + 10


# Janela do jogo
pasta_jogo = os.path.dirname(__file__)
janela = pygame.display.set_mode((800, 600))
imagem_fundo_nao_pronta = carregar_imagem(os.path.join(pasta_jogo, "jogoteste.imagem.png"))
imagem_fundo = pygame.transform.scale(imagem_fundo_nao_pronta, janela.get_size())
pygame.display.set_caption("Passarin's adventure")

# Personagens & Músicas & Sons
protagonista = carregar_imagem(os.path.join(pasta_jogo, "passarinpronto.png"))
antagonista = carregar_imagem(os.path.join(pasta_jogo, "passarin mal.png"))
playlist = [
    os.path.join(pasta_jogo, "passarin.piado.mp3"),
    os.path.join(pasta_jogo, "passarinmal.piado.mp3"),
]


# Velocidade dos passarinhos
vel_player = 10
vel_inimigo = 10

# Condições necessárias para o jogo
pos_x_fogo_inimigo = pos_x_inimigo
pos_y_fogo_inimigo = pos_y_inimigo
fogo = carregar_imagem(os.path.join(pasta_jogo, "Fogo do jogo.png"))
loop = True
mostrar_fogo_player = False
mostrar_fogo_inimigo = False
clock = pygame.time.Clock()

# Loop do jogo
while loop:
    for events in pygame.event.get():
        if events.type == pygame.QUIT:
            loop = False

    teclas = pygame.key.get_pressed()
    if teclas[pygame.K_SPACE]:
        atirar_player()
        mostrar_fogo_player = True
    if teclas[pygame.K_UP]:
        pos_y_player -= vel_player
    if teclas[pygame.K_DOWN]:
        pos_y_player += vel_player
    if teclas[pygame.K_LEFT]:
        pos_x_player -= vel_player
    if teclas[pygame.K_RIGHT]:
        pos_x_player += vel_player
    if teclas[pygame.K_s]:
        pos_y_inimigo += vel_inimigo
    if teclas[pygame.K_w]:
        pos_y_inimigo -= vel_inimigo
    if teclas[pygame.K_d]:
        pos_x_inimigo += vel_inimigo
    if teclas[pygame.K_a]:
        pos_x_inimigo -= vel_inimigo
    if teclas[pygame.K_z]:
        atirar_inimigo()
        mostrar_fogo_inimigo = True

    if pos_x_player <= -35:
        pos_x_player = -35

    if mostrar_fogo_player:
        pos_y_fogo -= 8
        if pos_y_fogo < 0:
            mostrar_fogo_player = False
    
    if mostrar_fogo_inimigo:
        pos_y_fogo_inimigo += 8
        if pos_y_fogo_inimigo > 600:
            mostrar_fogo_inimigo = False

    janela.blit(imagem_fundo, (0, 0))
    janela.blit(protagonista, (pos_x_player, pos_y_player))
    janela.blit(antagonista, (pos_x_inimigo, pos_y_inimigo))

    if mostrar_fogo_player:
        janela.blit(fogo, (pos_x_fogo, pos_y_fogo))

    if mostrar_fogo_inimigo:
        janela.blit(fogo, (pos_x_fogo_inimigo, pos_y_fogo_inimigo))

    pygame.display.update()
    clock.tick(60)

print(pos_x_player)
print(pos_y_player)
print("Fim do jogo")
