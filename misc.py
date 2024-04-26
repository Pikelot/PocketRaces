import os,random,arma
from personagens import goblin

def limpar():
    os.system("cls")

def heroi_para_dict(heroi):
    return {
        'nome': heroi.nome,
        'vida': heroi.vida,
        'dano': heroi.dano,
        'weapon': {
            'nome': heroi.weapon.nome,
            'tipo': heroi.weapon.tipo,
            'dano': heroi.weapon.dano,
            'valor': heroi.weapon.valor,
            'dropc': heroi.weapon.dropc
        }
    }

def desenho():
    print('%*------------------------------*%')

def dropcalc(drop_chance):
    chance = 100 * drop_chance

    rolagem = random.randint(0,100)
    
    if rolagem <= chance:
        return 0
    else:
        return 1