import random


nombre = random.randint(1, 1000000)
print("Devinez le nombre auquel je pense !")

while True:
    devin = int(input())
    if devin == nombre:
      print("Bravo !")
    elif devin < nombre:
      print("C'est un nombre plus grand")
    else : print("C'est un nombre plus petit")

