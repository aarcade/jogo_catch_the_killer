import pygame
import sys
from pygame.locals import *

mainClock = pygame.time.Clock()

# definicao das cores
preto = (0, 0, 0)
branco = (255, 255, 255)
cinza = (210, 210, 210)
cinza_escuro = (128, 128, 128)
verde_escuro = (35, 60, 17)
transparent = (0, 0, 0, 0)
vermelho = (255, 0, 0)

# inicializa o pygame e cria uma tela
pygame.init()
pygame.font.init()
altura = 1300
largura = 750
tela = pygame.display.set_mode((altura, largura))
pygame.display.set_caption('JOGO')
## carrega musica
som = pygame.mixer_music.load('Project - Patrick Patrikios.mp3')
pygame.mixer.music.play(-1)
## definição das direções
mov = 0
dir = 0
click = False
running = True


##escreve texto com a letra com sangue
def draw_text1(surface, text, size, x, y, color):
    font = pygame.font.Font('Halloween Too.ttf', size)
    text_surface = font.render(text, True, color)
    textrect = text_surface.get_rect()
    textrect.midtop = (x, y)
    surface.blit(text_surface, textrect)


## escreve texto com a letra Avaca Davra
def draw_text2(surface, text, size, x, y, color):
    ##escreve texto
    font = pygame.font.Font('Avaca Davra.ttf', size)
    textobj = font.render(text, True, color)
    textrect = textobj.get_rect()
    textrect.midtop = (x, y)
    surface.blit(textobj, textrect)


def menu():
    while True:
        global click
        tela.fill((preto))
        ## carrega imagem do menu
        background = pygame.transform.scale(pygame.image.load('menu.jpg').convert(), [1300, 750])
        background_rect = background.get_rect()
        tela.blit(background, background_rect)
        ## pega a posição dos botões
        mx, my = pygame.mouse.get_pos()
        botao1 = pygame.Rect(532, 375, 240, 45)
        botao2 = pygame.Rect(532, 427, 240, 48)
        botao3 = pygame.Rect(532, 483, 240, 45)
        if botao1.collidepoint((mx, my)):
            if click:
                apresentacao()
        if botao2.collidepoint((mx, my)):
            if click:
                instrucao()
        if botao3.collidepoint((mx, my)):
            if click:
                som()
        pygame.draw.ellipse(tela, preto, botao1)
        pygame.draw.ellipse(tela, cinza, botao2)
        pygame.draw.ellipse(tela, cinza, botao3)
        draw_text1(tela, "CATCH THE KILLER", 60, int(altura / 2), int((largura / 4) + 8), verde_escuro)
        draw_text2(tela, "START", 35, int(altura / 2), int((largura / 2) + 5), cinza_escuro)
        draw_text2(tela, "INSTRUCTIONS", 33, int(altura / 2), int((largura / 2) + 55), preto)
        draw_text2(tela, "SOUNDS", 30, int(altura / 2), int((largura / 2) + 110), preto)

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    pygame.quit()
                    sys.exit()
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True

        pygame.display.update()
        mainClock.tick(60)


def apresentacao():
    while True:
        global click
        tela.fill((preto))
        ## função menu
        background = pygame.transform.scale(pygame.image.load('fundo_apresentacao.jpeg').convert(),[1300, 750])
        background_rect = background.get_rect()
        tela.blit(background, background_rect)
        mx, my = pygame.mouse.get_pos()
        botao1 = pygame.Rect(1150, 60, 90, 48)

        if botao1.collidepoint((mx, my)):
            if click:
                game()
        pygame.draw.ellipse(tela, preto, botao1)
        draw_text2(tela, "START", 27, 1195, 70, cinza_escuro)
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    pygame.quit()
                    sys.exit()
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True
        for event in pygame.event.get():
            if event.type == QUIT:
                running = False
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    running = False

        pygame.display.update()
        mainClock.tick(60)


def instrucao():
    running = True
    while running:
        tela.fill((preto))
        tela.fill((branco))
        background = pygame.transform.scale(pygame.image.load('instrucao.jpeg'), [1300,750])
        background_rect = background.get_rect()
        tela.blit(background, background_rect)


        click = False
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    running = False
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True

        pygame.display.update()
        mainClock.tick(60)


def som():
   running = True
   while running:

       tela.fill((0, 0, 0))
       px, py = pygame.mouse.get_pos()
       botao1 = pygame.Rect(440, 189, 100, 45)
       botao2 = pygame.Rect(750, 189, 100, 45)
       if botao1.collidepoint((px, py)):
           if click:
               pygame.mixer.music.unpause()
       if botao2.collidepoint((px, py)):
           if click:
               pygame.mixer.music.pause()
       pygame.draw.ellipse(tela, verde_escuro, botao1)
       pygame.draw.ellipse(tela, verde_escuro, botao2)
       draw_text1(tela, "MUSICA",  40, int(altura / 2), int((largura /6) + 8), branco)
       draw_text1(tela, "ON", 35,490, 190, branco)
       draw_text1(tela, "OFF", 35,795,190, branco)
       click = False
       for event in pygame.event.get():
           if event.type == QUIT:
               pygame.quit()
               sys.exit()
           if event.type == KEYDOWN:
               if event.key == K_ESCAPE:
                   running = False
           if event.type == MOUSEBUTTONDOWN:
               if event.button == 1:
                   click = True
       pygame.display.update()
       mainClock.tick(60)



def game():
    relogio = pygame.time.Clock()
    # carrega imagens
    cenario = pygame.image.load('floresta.jpg')
    cenario = pygame.transform.scale(cenario, [1350, 750])
    pergamino = pygame.image.load('pergamino.png')
    pergamino = pygame.transform.scale(pergamino, [100, 100])
    pergamino2 = pygame.image.load('pergamino2.png')
    pergamino2 = pygame.transform.scale(pergamino2, [100, 100])
    pergamino3 = pygame.image.load('pergamino3.png')
    pergamino3 = pygame.transform.scale(pergamino3, [80, 80])
    machado = pygame.image.load('machado.png')
    machado = pygame.transform.scale(machado, [100, 100])


    pos_pergamino_x = -200
    pos_machado_y = 500
    pergamino2_x = -100
    pergamino3_x = -120

    vel_dragao = 9
    vel_machado = 0

    pontos = 0

    fonte = pygame.font.Font(None, 60)

    while True:
        global click
        relogio.tick(24)  # fps
        tela.fill((branco))
        tela.blit(cenario, (0, 0))
        tela.blit(machado, (675, pos_machado_y))
        tela.blit(pergamino, (pos_pergamino_x, 30))
        tela.blit(pergamino2, (pergamino2_x, 150))
        tela.blit(pergamino3, (pergamino3_x, 60))
        # placar
        if pontos > 0:
            texto = fonte.render(str(pontos), True, (255, 255, 255))
            tela.blit(texto, (1200, 200))
        pygame.display.flip()

        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                rodando = False
                print("Você fez %d pontos" % pontos)
            if evento.type == pygame.KEYDOWN:
                vel_machado = 10

        pos_pergamino_x += vel_dragao
        if pos_pergamino_x > 1300:
            pos_pergamino_x = -200
        pergamino2_x += 14
        if pergamino2_x > 1300:
            pergamino2_x = -120
        pergamino3_x += 12
        if pergamino3_x > 1300:
            pergamino3_x= -100
        if vel_machado > 0:
            pos_machado_y = pos_machado_y - vel_machado
            if pos_machado_y< -120:
                pos_machado_y = 378
                vel_machado = 0
            if pos_machado_y<=100:
                efeito=pygame.mixer_music.load('efeito_sonoro.mp3')
                pygame.mixer.music.play(1)
            if pos_machado_y>= 98:
                efeito = pygame.mixer_music.load('efeito_sonoro.mp3')
                pygame.mixer.music.pause()



        if pos_machado_y<= 100 and pos_pergamino_x > 560 and pos_pergamino_x < 800:
            pontos = pontos + 10
            pos_pergamino_x = -200

        if pontos > 20:
            ganhando()

        if pontos >= 10:
            mx, my = pygame.mouse.get_pos()
            botao1 = pygame.Rect(1150, 60, 90, 48)

            if botao1.collidepoint((mx, my)):
                perdendo()

            pygame.draw.ellipse(tela, preto, botao1)
            draw_text2(tela, "CONTINUAR", 20, 1195, 70, cinza_escuro)

            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        pygame.quit()
                        sys.exit()
                if event.type == MOUSEBUTTONDOWN:
                    if event.button == 1:
                        click = True

            pygame.display.update()
            mainClock.tick(60)
            for event in pygame.event.get():
                if event.type == QUIT:
                    running = False
                if event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        running = False

            pygame.display.update()
            mainClock.tick(60)


def perdendo():
    running = True
    click = False
    while running:
        tela.fill((preto))
        background = pygame.transform.scale(pygame.image.load('perdendo.jpg').convert(), [1300, 750])
        background_rect = background.get_rect()
        tela.blit(background, background_rect)
        mx, my = pygame.mouse.get_pos()
        botao1 = pygame.Rect(1150, 60, 90, 48)
        if botao1.collidepoint((mx, my)):
            if click:
                assassino()
        pygame.draw.ellipse(tela, preto, botao1)
        draw_text2(tela, "CONTINUE", 21, 1195, 70, cinza_escuro)
        click = False
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    running = False
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True
        pygame.display.update()
        mainClock.tick(60)


def ganhando():
    running = True
    click=False
    while running:
        tela.fill((preto))
        background = pygame.transform.scale(pygame.image.load('ganhando.jpg').convert(), [1300, 750])
        background_rect = background.get_rect()
        tela.blit(background, background_rect)
        mx, my = pygame.mouse.get_pos()
        botao1 = pygame.Rect(1150, 60, 90, 48)
        if botao1.collidepoint((mx, my)):
            dicas()
        pygame.draw.ellipse(tela, preto, botao1)
        draw_text2(tela, "CONTINUAR", 20,1195, 70, cinza_escuro)
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    pygame.quit()
                    sys.exit()
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True
        pygame.display.update()
        mainClock.tick(60)
        for event in pygame.event.get():
            if event.type == QUIT:
                running = False
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    running = False

        pygame.display.update()
        mainClock.tick(60)


def assassino():
    while True:
        pygame.init()
        pygame.font.init()
        altura = 1300
        largura = 750
        tela = pygame.display.set_mode((altura, largura))
        pygame.display.set_caption('JOGO')

        tela.fill((preto))
        background = pygame.transform.scale(pygame.image.load('assassinos.jpg').convert(), [1300, 750])
        background_rect = background.get_rect()
        tela.blit(background, background_rect)
        tela.blit(background, background_rect)

        mx, my = pygame.mouse.get_pos()
        botao1 = pygame.Rect(140, 610, 240, 45)
        botao2 = pygame.Rect(540, 610, 240, 45)
        botao3 = pygame.Rect(990, 610, 230, 40)
        if botao1.collidepoint((mx, my)):
            if click:
                ganhou()
        if botao2.collidepoint((mx, my)):
            if click:
                perdeu()
        if botao3.collidepoint((mx, my)):
            if click:
                perdeu()

        pygame.draw.ellipse(tela, cinza_escuro, botao1)
        pygame.draw.ellipse(tela, cinza_escuro, botao2)
        pygame.draw.ellipse(tela, cinza_escuro, botao3)
        draw_text2(tela, "WHO IS THE KILLER ? ", 40, 680, 69, vermelho)
        draw_text2(tela, "VICTORIA", 40, 250, 611, verde_escuro)
        draw_text2(tela, "ROSALIE", 40, 650, 611, verde_escuro)
        draw_text2(tela, "SETH", 40, 1090, 611, verde_escuro)

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    running = False
        pygame.display.update()
        mainClock.tick(60)


def dicas():
    while True:
        global click
        global running
        pygame.init()
        pygame.font.init()
        altura = 675
        largura = 900
        tela = pygame.display.set_mode((altura, largura))
        pygame.display.set_caption('Jogo')
        tela.fill((branco))
        background = pygame.image.load('dicas.jpg')
        background_rect = background.get_rect()
        tela.blit(background, background_rect)

        mx, my = pygame.mouse.get_pos()
        botao1 = pygame.Rect(550, 60, 90, 48)

        if botao1.collidepoint((mx, my)):
            if click:
                assassino()
        pygame.draw.ellipse(tela, preto, botao1)
        draw_text2(tela, "CONTINUE", 20, 595, 75, cinza_escuro)

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    pygame.quit()
                    sys.exit()
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True
            if event.type == QUIT:
                running = False
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    running = False

        pygame.display.update()
        mainClock.tick(60)
def perdeu():
    while True:
        global running
        tela.fill((0, 0, 0))
        ## função menu
        background = pygame.transform.scale(pygame.image.load('game_over.jpeg').convert(), [1300, 750])
        background_rect = background.get_rect()
        tela.blit(background, background_rect)
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    running = False
        pygame.display.update()
        mainClock.tick(60)
def ganhou():
    while True:
        global running
        tela.fill((0, 0, 0))
        ## função menu
        background = pygame.transform.scale(pygame.image.load('floresta_preto_branco.JPG').convert(), [1300, 750])
        background_rect = background.get_rect()
        tela.blit(background, background_rect)
        draw_text2(tela, "PARABÉNS!", 100, 700, 200, verde_escuro)
        draw_text2(tela, "VOCÊ ADIVINHOU QUEM É O ASSASSINO!", 80, 650, 80, verde_escuro)
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    running = False
        pygame.display.update()
        mainClock.tick(60)
menu()
