import pygame

# inicializando o pygame e a função mixer

pygame.init()
pygame.mixer.init()

# carregando todas as imagens usadas no jogo, o título do jogo e as dimensões da tela

janela = pygame.display.set_mode([1280, 720])
titulo = pygame.display.set_caption("Golzinho")

vencedor = pygame.image.load("vencedor.png")

placar1 = 0
placar1_img = pygame.image.load("0.png")

placar2 = 0
placar2_img = pygame.image.load("0.png")

placar10 = pygame.image.load("10.png")

torcida = pygame.mixer.music.load("torcida.mp3")  # carregando a música de fundo
pygame.mixer.music.play(-1)

chute = pygame.mixer.Sound("chute.wav")   # carregando o som do chute
apito = pygame.mixer.Sound("apito.wav")   # carregando o som do apito quando se faz um gol

mesa = pygame.image.load("campo.jpg")   # carregando a imagem da tela

jogador1 = pygame.image.load("jogador-1.png")
jogador1_y = 280    # posição em y do jogador 1
jogador1_movercima = False   # função de mover o jogador 1, se inicia com o valor falso
jogador1_moverbaixo = False

jogador2 = pygame.image.load("jogador-2.png")
jogador2_y = 280 # posição em y do jogador 2
jogador2_movercima = False # função de mover o jogador 2, se inicia com o valor falso
jogador2_moverbaixo = False

bola = pygame.image.load("bola.png")
bola_x = 600   # posição inicial em x da bola
bola_y = 320   # posição inicial em y da bola
bola_dir = -5   # direção inicial em x da bola, que nesse caso se move 3 pixels para esquerda
bola_dir_y = 5  # direção inicial em y da bola, se move 3 pixels para cima

jogando = True  # variável para controlar quando se está jogando ou não

# função do movimento do jogador 1
def mover_jogador1():
    global jogador1_y
    if jogador1_movercima:
        jogador1_y -= 5
    else:
        jogador1_y += 0

    if jogador1_moverbaixo:
        jogador1_y += 5
    else:
        jogador1_y -= 0

    if jogador1_y <= 35:
        jogador1_y = 35
    elif jogador1_y >= 525:
        jogador1_y = 525

# função do movimento do jogador 2
def mover_jogador2():
    global jogador2_y
    if jogador2_movercima:
        jogador2_y -= 5
    else:
        jogador2_y += 0

    if jogador2_moverbaixo:
        jogador2_y += 5
    else:
        jogador2_y -= 0

    if jogador2_y <= 35:
        jogador2_y = 35
    elif jogador2_y >= 525:
        jogador2_y = 525

# função do movimento da bola
def mover_bola():
    global bola_x
    global bola_y
    global bola_dir
    global bola_dir_y
    global placar2
    global placar1
    global placar2_img
    global placar1_img

    bola_x += bola_dir  # atribuindo a direção da bola em x
    bola_y += bola_dir_y  # atribuindo a direção da bola em y

# colisão da bola com o jogador 1
    if bola_x < 155:
        if jogador1_y < bola_y + 15:
            if jogador1_y + 158 > bola_y:
                bola_dir *= -1
                chute.play()

    # colisão da bola com o jogador 2
    if bola_x > 1050:
        if jogador2_y < bola_y + 25:
            if jogador2_y + 158 > bola_y:
                bola_dir *= -1
                chute.play()

# faz com que a bola bata e rebata nas laterais do campo
    if bola_y > 620:
        bola_dir_y *= -1
    elif bola_y <= 30:
        bola_dir_y *= -1

# indica quando o jogador 2 faz gol
    if bola_x < -60:
        bola_x = 600
        bola_y = 320
        bola_dir *= -1
        bola_dir_y *= -1
        placar2 += 1
        placar2_img = pygame.image.load(str(placar2) + ".png")
        apito.play()

    # indica quando o jogador 1 faz gol
    elif bola_x > 1350:
        bola_x = 600
        bola_y = 320
        bola_dir *= -1
        bola_dir_y *= -1
        placar1 += 1
        placar1_img = pygame.image.load(str(placar1) + ".png")
        apito.play()


# função que apresenta todas as figuras do jogo na tela
def sprites():

    if jogando:
        janela.blit(mesa, (0, 0))
        janela.blit(jogador1, (80, jogador1_y))
        janela.blit(jogador2, (1110, jogador2_y))
        janela.blit(bola, (bola_x, bola_y))
        janela.blit(placar1_img, (490, 75))
        janela.blit(placar2_img, (690, 75))
        mover_bola()
        mover_jogador2()
        mover_jogador1()
    else:
        janela.blit(mesa, (0, 0))
        janela.blit(vencedor, (340, 360))
        janela.blit(jogador1, (80, jogador1_y))
        janela.blit(jogador2, (1110, jogador2_y))
        janela.blit(placar1_img, (490, 75))
        janela.blit(placar2_img, (690, 75))


loop = True  # variável com valor verdadeiro que faz o loop rodar

# loop necessário para fazer o jogo rodar, controlar todos os movimentos dos jogadores, da bola,
# e fazer aparecer todos os componentes do jogo na tela
while loop:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            loop = False
        if evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_w:
                jogador1_movercima = True
            if evento.key == pygame.K_s:
                jogador1_moverbaixo = True

        if evento.type == pygame.KEYUP:
            if evento.key == pygame.K_w:
                jogador1_movercima = False
            if evento.key == pygame.K_s:
                jogador1_moverbaixo = False

        if evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_UP:
                jogador2_movercima = True
            if evento.key == pygame.K_DOWN:
                jogador2_moverbaixo = True

        if evento.type == pygame.KEYUP:
            if evento.key == pygame.K_UP:
                jogador2_movercima = False
            if evento.key == pygame.K_DOWN:
                jogador2_moverbaixo = False

    sprites() # função sendo chamada no loop
    if placar1 > 9 or placar2 > 9: # condição que indica o término do  jogo
        jogando = False
    if placar1 > 9:
        janela.blit(placar10, (490, 75)) # faz aparecer o placar 10 do jogador 1
    if placar2 > 9:
        janela.blit(placar10,(690, 75))  # faz aparecer o placar 10 do jogador 2
    pygame.display.update()  # função que atualiza sempre a tela
