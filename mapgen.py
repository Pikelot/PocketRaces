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
        posy = random.choice([n for n in range(18) if n != 5])
        lista.append([posx, posy])
        #lista[i] = (posx, posy)
    
    return lista

#geração_en()


def print_map(player_x, player_y, map_width, map_height, lista):
    
    for y in range(map_height):
        for x in range(map_width):
            if x == player_x and y == player_y:
                print("P", end=" ")  # Onde o jogador está
            elif x == 0 and y == 6:
                print("S", end=" ")
            elif any(item[0] == x and item[1] == y for item in lista):
                print("E", end=" ")
            #numero_de_inimigos, pos = geração_en()

            #for i in range(1,numero_de_inimigos):



            else:
                print(".", end=" ")  # Espaço vazio
            
        print()  # Nova linha
# Função principal
def main():
    map_width = 10
    map_height = 10
    player_x = 0  # Posição inicial do jogador
    player_y = 0

    while True:
        # Limpa o console para uma atualização limpa do mapa
        print("\033[H\033[J")
        
        # Imprime o mapa com a posição atual do jogador
        print_map(player_x, player_y, map_width, map_height)
        
        # Solicita ao jogador que insira um movimento
        move = input("Para onde você quer se mover? (W/A/S/D): ").upper()
