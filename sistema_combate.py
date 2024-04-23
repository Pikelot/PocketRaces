from personagens import goblin
from classes import character
from misc import *
import random




def batalha(nome, vida, dano):
    
    limpar()
    
    heroi = character(nome=nome, vida=vida, dano=dano)

    print(nome, 'VS', goblin.nome)
    print('Goblin lhe encara')
    while True:
        
        desenho()
        
        print(f'{heroi.nome}:\nVida:{heroi.vida}\nAtaque:{heroi.dano}')

        print(f'Goblin:\nVida:{goblin.vida}\nAtaque:{goblin.dano}')
        
        desenho()

        print('Digite 1 para atacar: ')
        print('Digite 2 para fugir: ')

        desenho()

        choice = input('# ')
        if choice == '1':    
            
            limpar()
            desenho()
            heroi.atacar(goblin)
            print(heroi.nome, "Acertou", goblin.nome, "Com a sua espada, causando", heroi.dano, "de dano")
            goblin.atacar(heroi)
            print(goblin.nome, "Acertou", heroi.nome, "Com o seu tacape, causando", goblin.dano, "de dano")
            desenho()
            input('# ')
            
        elif choice == '2':
            c = random.choice('0', '1')
            if c == '0':
                limpar()
                print('Você conseguiu fugir, ufa')
                return 2
            elif c == '1':
                limpar()
                print('Você não conseguiu fugir, o inimigo atacou novamente')
                goblin.atacar(heroi)

        if heroi.vida <= 0:
            return 1
        if goblin.vida <= 0:
            return 0
        
        limpar()
        print(nome, 'VS', goblin.nome)