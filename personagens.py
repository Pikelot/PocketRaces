from classes import *
from arma import *

goblin = inimigo(
    nome="Goblin", 
    vida= 20,
    dano=5,
    weapon=mãos,
    drop=espada_de_madeira
    )

slime = inimigo(
    nome="Slime",
    vida=50,
    dano=10,
    weapon=mãos,
    drop=palito_de_fosforo)

lobo_selvagem = inimigo(
    nome="Lobo Selvagem",
    vida=50,
    dano=10,
    weapon=mãos,
    drop=espada_de_madeira)

esqueleto = inimigo(
    nome="Esqueleto",
    vida=70,
    dano=10,
    weapon=espada_de_madeira,
    drop=espada_de_madeira)

Hobgoblin = inimigo(
    nome="Hobgoblin",
    vida=100,
    dano=8,
    weapon=tronco_de_madeira,
    drop=tronco_de_madeira)
