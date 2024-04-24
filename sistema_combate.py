from personagens import *
from classes import character
from misc import *
import random


def escolher_inimigo():
    lista_de_inimigos = [goblin,Hobgoblin,esqueleto,lobo_selvagem,slime]
    inimigo_escolhido = random.choice(lista_de_inimigos)
    return inimigo_escolhido

def batalha(nome, vida, dano):
    inimigo = escolher_inimigo()

    limpar()
    heroi = character(nome=nome, vida=vida, dano=dano)

    print(nome, 'VS', inimigo.nome)
    print(f'{inimigo.nome} lhe encara')
    while True:
        
        desenho()
        
        print(f'{heroi.nome}:\nVida:{heroi.vida}\nAtaque:{heroi.dano}')

        print(f'{inimigo.nome}:\nVida:{inimigo.vida}\nAtaque:{inimigo.dano}')
        
        desenho()

        print('Digite 1 para atacar: ')
        print('Digite 2 para fugir: ')

        desenho()

        choice = input('# ')
        if choice == '1':    
            
            limpar()
            desenho()
            heroi.atacar(inimigo)
            print(heroi.nome, "Acertou", inimigo.nome, "Com a sua espada, causando", heroi.dano, "de dano")
            inimigo.atacar(heroi)
            print(inimigo.nome, "Acertou", heroi.nome, "Com o seu tacape, causando", inimigo.dano + inimigo.weapon.dano, "de dano")
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
        if inimigo.vida <= 0:
            return 0
        
        limpar()
        print(nome, 'VS', inimigo.nome)