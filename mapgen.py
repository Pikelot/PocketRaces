# Função para imprimir o mapa
import random
from personagens import *


def geração_en():
    #quais = [goblin,slime,esqueleto,Hobgoblin,lobo_selvagem]
    #inimigos_escolhidos = []
    #for i in range(0,numero):
    #    inimigos_escolhidos.append(random.choice(quais))
    
    numero = random.randint(1,5)
    lista = []
    
    for i in range(0,numero):
        posx = random.randint(1,17)
        posy = random.choice([n for n in range(1,10) if n != 5])
        lista.append([posx, posy])
        #print(lista)
        #input('# ')
    
    return lista

#geração_en()


def print_map(player_x, player_y, map_width, map_height, lista):
    
    for y in range(map_height):
        for x in range(map_width):
            if x == player_x and y == player_y:
                print("P", end=" ")  # Onde o jogador está
            elif x == 0 and y == 6:
                print("S", end=" ")
            elif any(item[0] == x and item[1] == y for item in lista):  #Printa onde o inimigo está
                #print(x, y)
                print("E", end=" ")

            else:
                print(".", end=" ")  # Espaço vazio
            
        print()  # Nova linha
# Função principal