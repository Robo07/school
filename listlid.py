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
  if (len(prepick) == len(names)):
    prepick = []
    print("round done")

  pick = random.choice(names)

  while (pick in prepick):
    pick = random.choice(names)
  prepick.append(pick)

  print(pick)
  rounds = rounds - 1