import os,time
from misc import *
from classes import character
from sistema_combate import batalha
from personagens import goblin

run = True
menu = True
play = False
rules = False
key = False
battle = False

#mapa = 

def salvar():
    status = [
        str(heroi.nome),
        str(heroi.dano),
        str(heroi.vida),
        #str(elix),
        #str(gold),
        #str(x),
        #str(y),
        #str(key)
    ]

    file = open("load.txt", "w")

    for items in status:
        file.write(items + '\n')
    
    file.close()

while run:
    while menu:
        
        limpar()
        
        desenho()
        print("1, Novo jogo")
        print("2, Carregar jogo")
        print("3, Regras")
        print("4, Sair")
        desenho()

        if rules:
            
            limpar()
            
            rules = False
            choice = ""
            
            desenho()
            print('Bem vindo a Pocket Races')
            input("> ")
            desenho()

        else:
            choice = input("# ")
            desenho()

        #################################
        
        if choice == "1":
            
            limpar()

            #elix = 0
            #gold = 0
            #pot = 0
            #x = 0
            #y = 0
            #key = 0

            nome = input('# Qual o seu nome? ') #escolhendo o nome do jogador
            
            heroi = character(nome=nome, vida=100, dano=10) #atribui o nome ao objeto heroi

            menu = False
            play = True
        
        elif choice == "2":
            
            limpar()
            print('Carregando...')
            
            time.sleep(1)
            try:
                f = open('load.txt', 'r') #carregando o load
                load_list = f.readlines()
                
                nome = load_list[0][:-1]
                HP = int(load_list[1][:-1])
                ATK = int(load_list[2][:-1])
                #pot = int(load_list[3][:-1])
                #elix = int(load_list[4][:-1])
                #gold = int(load_list[5][:-1])
                #x = int(load_list[6][:-1])
                #y = int(load_list[7][:-1])
                #key = bool(load_list[8][:-1])
                limpar()
                
                heroi = character(nome=nome, vida= HP, dano=ATK)

                desenho()
                print("Bem vindo de volta", nome)
                desenho()
                input('> Pressione Enter para continuar ')
                
                menu = False
                play = True

            except OSError:
                limpar()
                print("Sem arquivo de salvamento...")
                input("# ")
            
            except ValueError:
                limpar()
                print("Arquivo de salvamento está corrompido...")
                input("# ")
            
            except IndexError:
                limpar()
                print("Arquivo de salvamento está corrompido...")
                input("# ")

        elif choice == "3":
            rules = True
            pass
        
        elif choice == "4":
            quit()
        ################################
########################################      
        while play:
            
            limpar()
            salvar() #autosave
            
            desenho()
            print("Nome:",heroi.nome)
            desenho()
            print(f"Dano: {heroi.dano} \nVida: {heroi.vida}")
            desenho()

            #entrando em batalha
            print('Enquanto andava pela floresta você encontra um:',goblin.nome)

            dest = input("# ")
            
            if dest == '0': #sair do jogo
                play = False
                menu = True
                salvar()
            
            if dest =='1': #debug pra entrar em combate
                
                play = False
                battle = True
                
                resultado = batalha(heroi.nome, heroi.vida, heroi.dano)
                
                if resultado == 0: 
                    
                    limpar()
                    print('Parabéns, você venceu :)')
                    input('# ')
                    battle = False
                    play = True

                elif resultado == 1:
                    
                    limpar()
                    print('Você morreu :(')
                    input('# ')
                    battle = False
                    play = False
                    menu = True

                elif resultado ==2:
                    
                    limpar()
                    input('# ')
                    print('Hoje a covardia venceu, você viverá para mais um dia :)')
                    battle = False
                    play = True