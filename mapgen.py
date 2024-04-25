# Função para imprimir o mapa
def print_map(player_x, player_y, map_width, map_height):
    for y in range(map_height):
        for x in range(map_width):
            if x == player_x and y == player_y:
                print("P", end=" ")  # Onde o jogador está
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
