print("Today is a good day to lear Python")
print('Python is fun')
print("Python's string are easy to use")
print('We can even include "quotes" in strings')
print("hello"+ " world")
greetings = "Hello"
#bekérni dolgokat az input fugvémnnyel lehet a felhasználótól
name = "Tim"
space = ' '
print(greetings + name)
# if we want a space, we can add that too
print(greetings+space+ name)

#egy adott változónak a létrehuzás utána bármilyen értéket adhatunk
#tehát ha stringet adtunk neki először értékül attol másodszor adhatok neki intet értékül letsgoooo fos
age = 24

print(age)

print(type(greetings))
print(type(age))

age_in_words = "2 years"


#fstring használatával igy is lehet intet stringben kiirni!!!
print(name + f" is {age} years old.")
print(type(age))



print(f"Pi is approximately {22/7:12.50f}")

pi = 22/ 7
print(f"Pi is approximately {pi:12.50f}")


