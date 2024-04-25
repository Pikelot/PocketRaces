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
        #print(self.weapon.nome)
        target.vida -= dano_causado
        target.vida = max(target.vida, 0)

class herói(character):
    def __init__(self, nome: str, vida: int, dano: int,) -> None:
        super().__init__(nome=nome, vida=vida, dano=dano)
        
        #self.posx = posx
        #self.posy = posy

        self.default_weapon = self.weapon

    def equipar(self, weapon) -> None:
        self.weapon = weapon
        #print("Você equipou", self.weapon.nome)
        #input('# ')

    def dropar(self) -> None:
        print("Você desequipou", self.weapon)
        input('# ')

        self.weapon = self.defaltweapon

class inimigo(character):
    def __init__(self, nome: str, vida: int, dano: int, weapon, drop) -> None:
        super().__init__(nome=nome, vida=vida, dano=dano,)
        self.weapon = weapon
        self.drop = drop
#goblin = character(nome='goblin', vida=51, dano= 51, weapon= espada_de_madeira)
#print(goblin.weapon.nome)