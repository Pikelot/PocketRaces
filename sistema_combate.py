from personagens import *
from classes import *
from misc import *
import random

def escolher_inimigo():
    #lista_de_inimigos = [goblin,Hobgoblin,esqueleto,lobo_selvagem,slime]
    #inimigo_escolhido = random.choice(lista_de_inimigos)
    
    inimigo_escolhido = goblin
    
    chosen = inimigo(
        nome=inimigo_escolhido.nome, 
        vida=inimigo_escolhido.vida, 
        dano=inimigo_escolhido.dano,
        weapon=inimigo_escolhido.weapon,
        drop=inimigo_escolhido.drop)

    return chosen

def batalha(nome, vida, dano, arma):
    inimigo = escolher_inimigo()
    #arma_atual = weapon

    #limpar()
    heroi = herói(nome=nome, vida=vida, dano=dano,)

    heroi.equipar(arma)
    
    print(nome, 'VS', inimigo.nome)
    print(f'{inimigo.nome} lhe encara')
    while True:
        
        desenho()

        print(f'{heroi.nome}:\nVida:{heroi.vida}\nAtaque:{heroi.dano}\n')

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
            print(heroi.nome, "Acertou", inimigo.nome, "Usando", heroi.weapon.nome, "causando", heroi.dano, "de dano")
            
            inimigo.atacar(heroi)
            print(inimigo.nome, "Acertou", heroi.nome, "usando", inimigo.weapon.nome, "causando", inimigo.dano + inimigo.weapon.dano, "de dano")
            
            desenho()
            input('# ')

        elif choice == '2':
            
            escolhas = [0,1]
            c = random.choice(escolhas)

            if c == 0:
                limpar()
                print('Você conseguiu fugir, ufa')
                return 2
            elif c == 1:
                limpar()
                print('Você não conseguiu fugir, o inimigo atacou novamente')
                goblin.atacar(heroi)

        if heroi.vida <= 0: #se o heroi morrer
            return 1
        
        if inimigo.vida <= 0: #se o inimigo morrer
            result = dropcalc(inimigo.drop.dropc)
            if result == 0:
                return 0, inimigo.drop
            else: 
                return 0
        limpar()
        print(nome, 'VS', inimigo.nome)