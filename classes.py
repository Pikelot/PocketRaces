from arma import mãos



class character:
    def __init__(self, nome: str, vida: int, dano: int,) -> None:
        
        self.nome = nome
        self.vida = vida
        self.vidamax = vida
        self.dano = dano        
        self.weapon = mãos

    def atacar(self, target) -> None:
        dano_causado = self.dano+self.weapon.dano
        target.vida -= dano_causado
        target.vida = max(target.vida, 0)



#goblin = character(nome='goblin', vida=51, dano= 51, weapon= espada_de_madeira)
#print(goblin.weapon.nome)