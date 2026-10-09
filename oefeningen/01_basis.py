ls = ["Supermarkt","Slager","Bakker","Bart Smit", "Blokker"]

print(ls)

UitgavenDict = {

    "Supermarkt": 2.75,
    "Slager": 22,
    "Bakker" : 45,
    "Bart Smit" : 45 , 
    "Blokker": 2.75
}


print(UitgavenDict)

print(ls[2])

bedragSlager = UitgavenDict["Slager"]


print(bedragSlager)

print(type(UitgavenDict))
print(type(ls))


print(type(UitgavenDict["Bakker"]))
print(type(ls[1]))



totaal_getal = 0

for x in UitgavenDict:
    totaal_getal += UitgavenDict[x]


print(totaal_getal)

if totaal_getal > 50:
    print("Het bedrag ligt boven de 50 euro")
else:
    print("Het bedrag ligt onder de 50 euro")
