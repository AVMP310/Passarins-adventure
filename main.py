import pygame
pygame.init()
pygame.mixer.init()

# Janela do jogo
janela = pygame.display.set_mode([0,0])
imagem_fundo_nao_pronta = pygame.image.load(r"C:\Users\Glauciane\Desktop\Arthur Coisas\vscode\Passarin's adventure\jogoteste.imagem.png")
imagem_fundo = pygame.transform.scale(imagem_fundo_nao_pronta, janela.get_size())
pygame.display.set_caption('Tche Tche')

# Personagens & Músicas & Sons
protagonista = pygame.image.load(r"C:\Users\Glauciane\Desktop\Arthur Coisas\vscode\Passarin's adventure\passarinpronto.png")
antagonista = pygame.image.load(r"C:\Users\Glauciane\Desktop\Arthur Coisas\vscode\Passarin's adventure\passarin mal.png")
playlist = ["c:\\Users\\Glauciane\\Desktop\\Arthur Coisas\\vscode\\Passarin's adventure\\passarin.piado.mp3", "c:\\Users\\Glauciane\\Desktop\\Arthur Coisas\\vscode\\Passarin's adventure\\passarinmal.piado.mp3"]

# Posição dos passarinhos
pos_y_player = 436
pos_x_player = 486
pos_y_inimigo = -50
pos_x_inimigo = 0

# Velocidade dos passarinhos
vel_player = 1

# Condições necessárias para o jogo
passarin_atiran = False
loop = True

# Loop do jogo
while loop:

    for events in pygame.event.get():
        if events.type == pygame.QUIT:
            loop = False
    # Reação às teclas pressionadas
    teclas = pygame.key.get_pressed()
    if teclas[pygame.K_UP]:
        pos_y_player -= vel_player
    if teclas[pygame.K_z]:
        passarin_atiran = True
        pygame.mixer.music.load(playlist[0])
        pygame.mixer.music.play()
    if teclas[pygame.K_DOWN]:
        pos_y_player += vel_player
    if teclas[pygame.K_LEFT]:
        pos_x_player -= vel_player
    if teclas[pygame.K_RIGHT]:
        pos_x_player += vel_player
    if teclas[pygame.K_s]:
        pos_y_inimigo += vel_player
    if teclas[pygame.K_w]:
        pos_y_inimigo -= vel_player
    if teclas[pygame.K_d]:
        pos_x_inimigo += vel_player
    if teclas[pygame.K_a]:
        pos_x_inimigo -= vel_player

    # Área em teste

    # Não deixa o player sair do cenário
        #pos_y_player = 592
    # if pos_y_player >= 200:
    #     pos_y_player = 200
    if pos_x_player <= -35:
        pos_x_player = -35

    # Área em teste
    
    # if pos_x_player >= 400:
    #    pos_x_player = 400
    # Não deixa o inimigo/player 2 sair do cenário
    # print(pos_x_inimigo)
    # if pos_y_inimigo >= 148:
    #    pos_y_inimigo = 148
    # if pos_y_inimigo <= -73:
    #    pos_y_inimigo = -73
    # Desenha o cenário e os personagens
    janela.blit(imagem_fundo, (0,0))
    janela.blit(protagonista, (pos_x_player, pos_y_player))
    janela.blit(antagonista, (pos_x_inimigo, pos_y_inimigo))
    pygame.display.update()

print(pos_x_player)
print(pos_y_player)

print("Fim do jogo")
    