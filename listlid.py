import random

names = [
    "kacik", "ancik", "kikcik", "vojtik", "vojtik2", "tercik", "adik", "kubik",
    "davik", "karlik", "filik", "marcik", "davcik", "ivcik"
]
prepick = []

#to be done
count = int(input("Zadaj pocet ziakov: "))
#number of rounds
rounds = int(input("Zadaj pocet kolov: "))

while (int(rounds) > 0):
    while (count > len(names)):
        print("Zadal si viac ziakov ako je v zozname")
        count = int(input("Zadaj pocet ziakov: "))
    
    pick = []

    if (len(prepick) == len(names)):
        prepick = []
    print("round done")

    if(len(names) - len(prepick) < count):
        print("Zostalo malo ziakov")
        pick = names
        pick = [fruit for fruit in pick if fruit not in prepick]
        print(pick)
    
    choice = random.choice(names)

    while (len(pick) < count):
        while (choice in prepick):
            choice = random.choice(names)
        prepick.append(choice)
        pick.append(choice)

    print(pick)
    rounds = rounds - 1