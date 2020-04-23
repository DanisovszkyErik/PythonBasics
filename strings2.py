#stringek mint tömbök(ugyanugy mint c#
parrot = "Norwegian Blue"

print(parrot)

print(parrot[3])

print(parrot[4] + "\n" + parrot[9] + "\n" + parrot[3]
      + "\n" + parrot[6] + "\n" + parrot[8])


print()


# minusz indexelés az -1től kezdődik!!
print(parrot[-11] + "\n" + parrot[-10] + "\n" + parrot[-5] + "\n" + parrot[-11]
      + "\n" + parrot[-8] + "\n" + parrot[-6])
print()
print(parrot[3-14] + "\n" + parrot[4-14] + "\n" + parrot[9-14] + "\n" + parrot[3-14]
      + "\n" + parrot[6-14] + "\n" + parrot[8-14])

print()


#kiirja az adott stingben lévő első 5 karaktert
print(parrot[0:6]) # Norweg
print(parrot[-14:6-14])
print(parrot[3:5])
print(parrot[3-14:5-14])
print(parrot[0:9])
print(parrot[-14:9-14])
print(parrot[10:])
print(parrot[10-14:])


print(parrot[:6])
print(parrot[-14:6-14])
print(parrot[6:])
print(parrot[6-14:])

print()
print()
print(parrot[-5:])
print()

print()

print(parrot[:6] + parrot[6:])
print(parrot[:6-14] + parrot[6-14:])


print(parrot[:])




letters = "abcdefghijklmnopqrstuvwxyz"



print(letters[23-26:])
print(letters)
print()

print(parrot[-4:-2]) #result: Bl
print(parrot[-4:12]) #result: Bl




print()

#tehát ez a sor azt csinálja, hogy megadhatjuk a szeletnél hogy milyen nagyságaal lépjen
#itt 0:6 az hogy 0- az 5. karakterig mennyink el es a 2 az az hogy milyen lepesekkel
print(parrot[0:6:2]) #Nre
print(parrot[0:6:3]) #Nw
print(parrot[0:7:3]) #Nwi

number = "9,223;372:036 854,775;807"

separators = number[1::4]
print(separators)

values = "".join(char if char not in separators else " " for char in number).split()
print([int(val) for val in values])