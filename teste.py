import random




numero = random.randint(1,5)
lista = []
for i in range(0,numero):
        posx = random.randint(1,17)
        posy = random.choice([n for n in range(18) if n != 5])
        lista.append([posx, posy])


posx = 8
posy = 8



if any(item[0] == posx and item[1] == posy for item in lista):
                print("E", end=" ")

print (lista)