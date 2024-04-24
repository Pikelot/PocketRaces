import os,random,arma
from personagens import goblin

def limpar():
    os.system("cls")

def desenho():
    print('%*------------------------------*%')

def dropcalc(drop_chance):
    chance = 100 * drop_chance

    rolagem = random.randint(0,100)
    
    if rolagem <= chance:
        print("Um inimigo dropou um item")
        input("#")
        return 0
    else:
        return 1

print(goblin.drop.dropc)