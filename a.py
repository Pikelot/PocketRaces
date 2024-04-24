#from PIL import Image
#img = Image.open("sheep.png")
#img.show()


#print("""
#///           ///       ///                         
#                            //////  ///*///////*  ///                           
#                             /////  ////**///**///                              
#                                  ////////******//                              
#                                  //////////////**                              
#                                    //////   /////                              
#                                **** ///  ///  /                                
#                             //********        ******                           
#                            ///     ***********     ///                         
#                            ////    ***********   /////                         
#                                    ////**/////                                 
#                                  //////////////                                
#                                ///////     //////                              
#                             ,,,/////        /////,,,                
#""")


while run:
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
            
            heroi = herói(nome=nome, vida=100, dano=10) #atribui o nome ao objeto heroi

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
                limpar()
                
                heroi = herói(nome=nome, vida= HP, dano=ATK)

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
  
        while play:
            
            limpar()
            salvar() #autosave

            desenho()
            print("Nome:",heroi.nome)
            desenho()
            
            print(f"Dano: {heroi.dano} + {heroi.weapon.dano}", end=' ')
            print(f"Arma equipada: {heroi.weapon.nome}" )
            print(f"Vida: {heroi.vida}")
            desenho()

            #entrando em batalha
            print('Enquanto andava pela floresta você encontra um inimigo')

            dest = input("# ")

            if dest == '0': #sair do jogo
                
                play = False
                menu = True
                salvar()
            
            if dest =='1': #debug pra entrar em combate
                
                play = False
                battle = True
                
                resultado = batalha(heroi.nome, heroi.vida, heroi.dano, heroi.weapon)
                #print(resultado)
                if resultado == 0 or 0 in resultado: 
                    limpar()
                    print('Parabéns, você venceu :)')
                    if resultado == list:
                        heroi.equipar(resultado[1])
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