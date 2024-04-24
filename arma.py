class weapon:
    def __init__(self, nome: str, tipo: str, dano: int, valor: int) -> None:
        self.nome = nome
        self.tipo = tipo
        self.dano = dano
        self.valor = valor

mãos = weapon(nome='Mãos', tipo="Desarmado", dano=5, valor=0)

#mãos = weapon(nome="Mãos",
#                           tipo="Desarmado",
#                           dano=0,
#                           valor=0)

#espada_de_madeira = weapon(nome="Espada de Madeira",
#                           tipo="Espada Curta",
#                           dano=5,
#                           valor=0)
#
#tronco_de_madeira = weapon(nome="Tronco de madeira",
#                           tipo="Arma de duas mãos",
#                           dano=10,
#                           valor=0)

#palito_de_fosforo = weapon(nome="Palito de fósforo",
##                           tipo="Varinha",
#                           dano=5,
#                           valor=0)
