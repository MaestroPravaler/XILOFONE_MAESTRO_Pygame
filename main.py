#encoding: utf-8
##################################################################
## XILOFONE - VITÓRIA
##################################################################
## BIBLIOTECAS PARA EXPORTAR PARA EXECUTÁVEL
## COPIAR O ARQUIVO setup.py para todas as aplicações que desejar
## transformar em exe (fazer as configurações necessárias nele)
## rodar o comando | python setup.py build |
#################################################################

#################################################################
## BIBLIOTECAS EXCENCIAIS
#################################################################
import pygame as pg
from pygame import mixer
##################################################################
pg.init()  ## INICIALIZAÇÃO DO PYGAME
### DEFININDO NOTAS DO XILOFONE (DO4 A FÁ6) #############
do5 = pg.mixer.Sound('data/do5.wav')
re5 = pg.mixer.Sound('data/re5.wav')
mi5 = pg.mixer.Sound('data/mi5.wav')
fa5 = pg.mixer.Sound('data/fa5.wav')
sol5 = pg.mixer.Sound('data/sol5.wav')
la5 = pg.mixer.Sound('data/la5.wav')
si5 = pg.mixer.Sound('data/si5.wav')
do6 = pg.mixer.Sound('data/do6.wav')
re6 = pg.mixer.Sound('data/re6.wav')
mi6 = pg.mixer.Sound('data/mi6.wav')
fa6 = pg.mixer.Sound('data/fa6.wav')
##########################################################
##### DEFININDO AS CORES #################################
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
ORANGE = (240, 159, 10)
YELLOW = (239, 247, 5)
GREEN = (0, 255, 0)
BLUE = (5, 215, 247)
INDIGO = (53, 5, 247)
VIOLET = (158, 5, 247)
##########################################################
## POSICIONANDO AS TECLAS DO XILOFONE ####################
do5_t = pg.Rect(10,50,80,400)
re5_t = pg.Rect(95,55,80,390)
mi5_t = pg.Rect(180,60,80,380)
fa5_t = pg.Rect(265,65,80,370)
sol5_t = pg.Rect(350,70,80,360)
la5_t = pg.Rect(435,75,80,350)
si5_t = pg.Rect(520,80,80,340)
do6_t = pg.Rect(605,85,80,330)
re6_t = pg.Rect(690,90,80,320)
mi6_t = pg.Rect(775,95,80,310)
fa6_t = pg.Rect(860,100,80,300)

##########################################################
## DEFININDO AS PROPRIEDADES DA TELA
screen = pg.display.set_mode([950, 480]) ## TAMANHO DA JANELA
pg.display.set_caption("VITÓRIA XILOFONE") ## TITULO DA JANELA

Icon = pg.image.load('data/icone.png') ## TROCAR O ICONE
pg.display.set_icon(Icon)

janelaLoop = True  ## colocar a janela em loop
clock = pg.time.Clock()
if __name__ == "__main__":
    while janelaLoop:
        clock.tick(60)
        ## COMPOSIÇÃO DO CENTRO DA TELA
        screen.fill([171, 128, 65]) ## COR DE FUNDO MODELO rgb

        #########################################################################
        ## CABEÇALHO ###
        pg.draw.rect(screen, BLACK, [0, 0, 950, 40])  ## ÁREA DO CABEÇALHO
        font = pg.font.SysFont(None, 55) ## FONTE DO TÍTULO
        text = font.render('Vitória Xilofone', True, WHITE)  ## TÍTULO CENTRALIZADO
        screen.blit(text, [320, 5])  ##  IMPRIMINDO NA TELA
        #########################################################################
        ## DESENHO DAS TECLAS DO XILOFONE  ###
        pg.draw.rect(screen, RED, do5_t) ## DO5
        pg.draw.rect(screen, ORANGE, re5_t)  ## RE5
        pg.draw.rect(screen, YELLOW, mi5_t)  ## DÓ5
        pg.draw.rect(screen, GREEN, fa5_t)  ## DÓ5
        pg.draw.rect(screen, BLUE, sol5_t)  ## DÓ5
        pg.draw.rect(screen, INDIGO, la5_t)  ## DÓ5
        pg.draw.rect(screen, VIOLET, si5_t)  ## DÓ5
        pg.draw.rect(screen, RED, do6_t)  ## DÓ5
        pg.draw.rect(screen, ORANGE, re6_t)  ## DÓ5
        pg.draw.rect(screen, YELLOW, mi6_t)  ## DÓ5
        pg.draw.rect(screen, GREEN, fa6_t)  ## DÓ5
        ## ESCRITA DENTRO DAS NOTAS
        font = pg.font.SysFont(None, 55)  ## FONTE DO TÍTULO

        DO = font.render('DÓ', True, BLACK)  ## TÍTULO CENTRALIZADO
        screen.blit(DO, [20, 60])  ##  IMPRIMINDO NA TELA
        screen.blit(DO, [615, 95])
        DO_L = font.render('a', True, BLACK)  ## TÍTULO CENTRALIZADO
        screen.blit(DO_L, [35, 410])  ##  IMPRIMINDO NA TELA
        DO_L2 = font.render('k/z', True, BLACK)
        screen.blit(DO_L2, [620, 375])

        RE = font.render('RÉ', True, BLACK)  ## TÍTULO CENTRALIZADO
        screen.blit(RE, [105, 65])  ##  IMPRIMINDO NA TELA
        screen.blit(RE, [700, 100])
        RE_L = font.render('s', True, BLACK)  ## TÍTULO CENTRALIZADO
        screen.blit(RE_L, [125, 405])  ##  IMPRIMINDO NA TELA
        RE_L2 = font.render('x', True, BLACK)
        screen.blit(RE_L2, [715, 370])

        MI = font.render('MI', True, BLACK)  ## TÍTULO CENTRALIZADO
        screen.blit(MI, [195, 70])  ##  IMPRIMINDO NA TELA
        screen.blit(MI, [790, 105])
        MI_L = font.render('d', True, BLACK)  ## TÍTULO CENTRALIZADO
        screen.blit(MI_L, [205, 400])  ##  IMPRIMINDO NA TELA
        MI_L2 = font.render('c', True, BLACK)
        screen.blit(MI_L2, [805, 365])

        FA = font.render('FA', True, BLACK)  ## TÍTULO CENTRALIZADO
        screen.blit(FA, [280, 75])  ##  IMPRIMINDO NA TELA
        screen.blit(FA, [875, 110])
        FA_L = font.render('f', True, BLACK)  ## TÍTULO CENTRALIZADO
        screen.blit(FA_L, [295, 395])  ##  IMPRIMINDO NA TELA
        FA_L2 = font.render('v', True, BLACK)
        screen.blit(FA_L2, [895, 360])

        SOL = font.render('SOL', True, BLACK)  ## TÍTULO CENTRALIZADO
        screen.blit(SOL, [352, 80])  ##  IMPRIMINDO NA TELA
        SOL_L = font.render('g', True, BLACK)  ## TÍTULO CENTRALIZADO
        screen.blit(SOL_L, [385, 380])  ##  IMPRIMINDO NA TELA

        LA = font.render('LÁ', True, BLACK)  ## TÍTULO CENTRALIZADO
        screen.blit(LA, [450, 85])  ##  IMPRIMINDO NA TELA
        LA_L = font.render('h', True, BLACK)  ## TÍTULO CENTRALIZADO
        screen.blit(LA_L, [465, 375])  ##  IMPRIMINDO NA TELA

        SI = font.render('SÍ', True, BLACK)  ## TÍTULO CENTRALIZADO
        screen.blit(SI, [540, 90])  ##  IMPRIMINDO NA TELA
        SI_L = font.render('j', True, BLACK)  ## TÍTULO CENTRALIZADO
        screen.blit(SI_L, [555, 370])  ##  IMPRIMINDO NA TELA


        ######################################################################
        ## FOOTER ####
        pg.draw.rect(screen, BLACK, [0, 460, 950, 25]) ## ÁREA DO CABEÇALHO
        font = pg.font.SysFont(None, 20) ## FONTE DO TÍTULO
        text = font.render('Copyright ® RobsonMaestro / 2020.', True, WHITE)  ## TÍTULO CENTRALIZADO
        screen.blit(text, [350, 465])  ##  IMPRIMINDO NA TELA
        #######################################################################
        ## INTERAÇÃO COM AS TECLAS DO XILOFONE (LÓGICA) ####

        for event in pg.event.get():
            if event.type == pg.QUIT: ## FECHAR A APLICAÇÃO
                janelaLoop = False

            #######################################################
            ## TOCAR UTILIZANDO O MOUSE ###
            if event.type == pg.MOUSEBUTTONDOWN: ## APERTA O BOTÃO DO MOUSE
                if do5_t.collidepoint(pg.mouse.get_pos()):
                    do5.play()
                elif re5_t.collidepoint(pg.mouse.get_pos()):
                    re5.play()
                elif mi5_t.collidepoint(pg.mouse.get_pos()):
                    mi5.play()
                elif fa5_t.collidepoint(pg.mouse.get_pos()):
                    fa5.play()
                elif sol5_t.collidepoint(pg.mouse.get_pos()):
                    sol5.play()
                elif la5_t.collidepoint(pg.mouse.get_pos()):
                    la5.play()
                elif si5_t.collidepoint(pg.mouse.get_pos()):
                    si5.play()
                elif do6_t.collidepoint(pg.mouse.get_pos()):
                    do6.play()
                elif re6_t.collidepoint(pg.mouse.get_pos()):
                    re6.play()
                elif mi6_t.collidepoint(pg.mouse.get_pos()):
                    mi6.play()
                elif fa6_t.collidepoint(pg.mouse.get_pos()):
                    fa6.play()

            #######################################################
            ## TOCAR UTILIZANDO O TECLADO ###
            if event.type == pg.KEYDOWN: ## QUANDO APERTA A TECLA
                if event.key == pg.K_a:
                    do5.play() #C5
                if event.key == pg.K_s:
                    re5.play() #D5
                if event.key == pg.K_d:
                    mi5.play() #E5
                if event.key == pg.K_f:
                    fa5.play() #F5
                if event.key == pg.K_g:
                    sol5.play() #G5
                if event.key == pg.K_h:
                    la5.play() #A5
                if event.key == pg.K_j:
                    si5.play() #B5
                if event.key == pg.K_k:
                    do6.play() #C6
                if event.key == pg.K_z:
                    do6.play() #C6
                if event.key == pg.K_x:
                    re6.play() #D6
                if event.key == pg.K_c:
                    mi6.play() #E6
                if event.key == pg.K_v:
                    fa6.play() #F6

        pg.display.update()  ## LOOP DO APLICATIVO

