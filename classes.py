class character:
    def __init__(self, nome: str, vida: int, dano: int) -> None:
        self.nome = nome
        self.vida = vida
        self.vidamax = vida
        self.dano = dano

    def atacar(self, target) -> None:
        target.vida -= self.dano
        target.vida = max(target.vida, 0)
