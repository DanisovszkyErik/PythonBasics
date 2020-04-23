letters = "abcdefghijklmnopqrstuvwxyz"
backwards = letters[::-1]
print(backwards)

slice = letters[16:13:-1]
print(slice)
slice = letters[16-26:13-26:-1] # 10
print(slice)

print(letters[4::-1])
print(letters[4-26::-1])

print(letters[:25-8:-1])
print(letters[-1:25-8-26:-1])


#last 4 charcter
print(letters[-4:])
print(letters[-1:])
print(letters[0:1])
print(letters[0:5])



