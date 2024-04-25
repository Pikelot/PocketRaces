import time
from misc import *
from classes import *
from arma import *
from sistema_combate import batalha
from mapgen import print_map

#global menu, rules, run 
run = True
menu = True
play = False
rules = False
key = False
battle = False
game = True

map_width = 17
map_height = 10
#mapa = 

def salvar(posx, posy):
    status = [
        str(heroi.nome),
        str(heroi.vida),
        str(heroi.dano),
        str(posx),
        str(posy)
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

def painel_menu():
    menu = True
    rules = False

    while menu:
        #menu()
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

            nome = input('# Qual o seu nome? ') #escolhendo o nome do jogador
            
            pos_x = 0 #Posição inicial do jogador
            pos_y = 0

            heroi = herói(nome=nome, vida=100, dano=10,) #atribui o nome ao objeto heroi

            menu = False

            return True, heroi, pos_x, pos_y
        
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
                pos_x = int(load_list[3][:-1])
                pos_y = int(load_list[4][:-1])
                limpar()
                
                heroi = herói(nome=nome, vida= HP, dano=ATK,)

                desenho()
                print("Bem vindo de volta", nome)
                desenho()
                input('> Pressione Enter para continuar ')
                
                menu = False
                return True, heroi, pos_x, pos_y

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

def combate_resultado():
        
    resultado = batalha(heroi.nome, heroi.vida, heroi.dano, heroi.weapon)
    print(resultado)
            #print(resultado)
    if resultado == 0: 
                    limpar()
                    print('Parabéns, você venceu :)')
                    input('# ')
                    
                    return False

    elif resultado == 1:
                    
                    limpar()
                    print('Você morreu :(')
                    input('# ')
                    
                    return False
    elif resultado ==2:
                    
                    limpar()
                    input('# ')
                    print('Hoje a covardia venceu, você viverá para mais um dia :)')
                    
                    return False
    elif 0 == resultado[0]: 
                    
                    limpar()
                    print('Parabéns, você venceu :)')

                    input('# ')
                    
                    return True, resultado[1]

while game:
    
    #função do menu principal
    result = painel_menu()

    #recolhendo dados da função do menu principal
    
    play = result[0]
    heroi = result[1]
    pos_x = result[2]
    pos_y = result[3]

    while play:
        
        #interface e gameplay base do jogo    
            parado = True

            limpar()
            salvar(pos_x, pos_y) #autosave

            #entrando em batalha
            
            while parado:
                limpar()
                
                encontrou = random.randint(0,2)

                desenho()
                print("Nome:",heroi.nome)
                
                desenho()

                print(f"Dano: {heroi.dano} + {heroi.weapon.dano}", end=' ')
                print(f"Arma equipada: {heroi.weapon.nome}" )
                print(f"Vida: {heroi.vida}", end="")
                print(" W:Cima A:Esquerda S:Baixo D:Direita")
                desenho()

                print_map(pos_x, pos_y, map_width, map_height,)

                desenho()
                choice = input("# ")

                if choice.upper() == 'W':
                      pos_y -= 1
                if choice.upper() == 'A':
                      pos_x -= 1
                if choice.upper() == 'S':
                      pos_y += 1
                if choice.upper() == 'D':
                      pos_x += 1      

                if encontrou == 0:
                    parado = False
                    battle = True

                      
                print('Enquanto andava pela dungeon você encontra um inimigo')

            #if dest == '0': #sair do jogo
            #    
            #    play = False
            #    menu = True
            #    salvar(pos_x, pos_y)
            
            while battle:    
                limpar()

                print('Enquanto andava pela dungeon você encontra um inimigo')
                input("# ")

                limpar()

                resultado = combate_resultado()
                
                if resultado != False:
                    #Caso algo tenha sido dropado, equipar
                    
                    print("Ufa, sobreviveu a essa!")
                    desenho()
                    print("Você encontrou: ", end="")
                    print(f"X-| {resultado[1].nome} |-X")
                    desenho()

                    print("Você deseja equipar? S/N?\n")
                    choice = input("# ")
                    
                    if choice.upper() == "S":
                        heroi.equipar(resultado[1])

                    parado = True
                    battle = False

                else:
                    print("Ufa, sobreviveu a essa!")
                    parado = True
                    battle = False
                    input("# ")