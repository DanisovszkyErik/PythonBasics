splitString = "This string has been \n split over \n serevral \n lines"
print(splitString)

tabbedString = '1\t2\t3\t4\t5'
print(tabbedString)

#Ha a stringet kiszeretnénk iratni amiben van egy idézet akkor ahoz \-t kell használni
print('The pet shop owner said "No, no, \'e\'s uh,...he\'s resting".')
#or fordítva is működik
print("The pet shop owner said \"No, no, 'e's uh,.. he's resting\".")

#Három időzöjel között nem kell speciális karakter mivel engedélyezve van benne a dupla, és az egyedüli idézőjel is
print("""The pet shop owner said "No, no, \
'e's uh,...he's resting".""")

#Három idézőjelnél az enter utés uj sornak számít kiiratáskor WOOOW
anotherSplitString = """This string has been \
split over \
several \
lines"""

print(anotherSplitString)

print("""Number 1\tThe Larch
Number 2\tThe Horse ChestNut""")


print("C:\\Users\\timbuchalka\\notes.txt")
#az r a raw string vagyis nyers szoveget jelenti így semmilyen escape charactert nem néz!!
print(r"C:\Users\timbuchalka\n\t\otes.txt")

