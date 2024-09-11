import math

Svalce = 0
Vvalce = 0

while True:
    try:
        rpodstavy = float(input("Zadaj polomer podstavy valca: "))
        rvyska = float(input("Zadaj vysku valca: "))
        break
    except:
        print("Zadaj cele cislo")

Svalce = 2*math.pi*rpodstavy*rpodstavy + 2*math.pi*rpodstavy*rvyska
Vvalce = math.pi*rpodstavy*rpodstavy*rvyska

print("Povrch valca je: ", Svalce, "cm^2")
print("Objem valca je: ", Vvalce, "cm^3")