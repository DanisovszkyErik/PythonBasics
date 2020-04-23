a = 12
b = 3

print(a + b) #15
print(a - b) #9
print(a * b) #36
print(a / b) #4.0
print(a // b) # osztás egéész részét adja vissza
print(a % b) #0 maradékod adja vissza

print()

for i in range(1, 6):
    print(i * 2)


print()

print(a + b / 3 - 4 * 12)
print(a + (b / 3) - (4 * 12))
print((((a +b) / 3)- 4)* 12)
print((((a + b) / 3 - 4) * 12))

c = a + b
d = c / 3
e = d - 4

print(e * 12)


print()
print(a / (b * a) / b)