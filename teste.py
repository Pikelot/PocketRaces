from arma import mãos, espada_de_madeira

from classes import *
import json

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

a = {
        'nome': 'a',
        'vida': 10,
        'dano': 10,
        'weapon': {
            'nome': 'joao',
            'tipo': 'oi',
            'dano': 100,
            'valor': 10,
            'dropc': 10
        }
}

print (a['weapon']['nome'])

quit()

print()

nome = 'joao'

hero = herói(nome=nome, vida=100, dano=10,)

#dicionario_personagem = {
#    'nome': hero.nome,
#    'vida': hero.vida,
#    'dano': hero.dano
#}


#print(dicionario_personagem)
input('#')

heroi_arq = heroi_para_dict(hero)

with open('objeto_salvo2.json', 'w') as arquivo:
    json.dump(heroi_arq, arquivo)

with open('objeto_salvo.json', 'r') as arquivo:
    arma_recuperada_dict = json.load(arquivo)
    arq_1 = arma_recuperada_dict[0]
    arq_2 = arma_recuperada_dict[1]

    print(arq_1['nome'])