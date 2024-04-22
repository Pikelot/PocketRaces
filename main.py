import os,time

run = True
menu = True
play = False
rules = False
key = False

HP = 50
ATK = 3
pot = 1
elix = 0
gold = 0
x = 0
y = 0

#mapa = 

def salvar():
    status = [
        nome,
        str(HP),
        str(ATK),
        str(pot),
        str(elix),
        str(gold),
        str(x),
        str(y),
        str(key)
    ]

    file = open("load.txt", "w")

    for items in status:
        file.write(items + '\n')
    
    file.close()

def limpar():
    os.system("cls")

def desenho():
    print('%*------------------------------*%')

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

            nome = input('# Qual o seu nome? ') #escolhendo o nome do jogador

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
                pot = int(load_list[3][:-1])
                elix = int(load_list[4][:-1])
                gold = int(load_list[5][:-1])
                x = int(load_list[6][:-1])
                y = int(load_list[7][:-1])
                key = bool(load_list[8][:-1])
                limpar()
                
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
      
        while play:
            
            limpar()
            salvar() #autosave
            
            print(nome)
            
            dest = input("# ")
            if dest == '0':
                play = False
                menu = True
                salvar()