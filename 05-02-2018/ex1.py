a = 1
b = 2
c = 7
result = a + b
print(result)
result = a - b
print(result)
result = a * 2
print(result)
result = c / b
print(result)
result = c // b
print(result)

z = 4.23
print(type(b))
print(type(z))

z_int = int(z)
print(type(z_int), z_int)

# @TODO: sprawdzić co znaczy ^ w Pythonie
result = b ** 4
print(result)

#print('before', c)
#c -= 2
#c *= 4
#c /= 6
#print('after', c)

c = c % 2
print(c)

text = 'Ala ma kota'
eng = "Tom's house"
eng2 = 'Tom\'s house'
print(eng2)
letter_a = text[0]
print(letter_a)
lenght = len(text)
print(lenght)
# slices
something = text[4:8]
print(something)
something2 = text[-4:-1]
print(something2)
steps = text[0:10:2]
dunno = text[0:15]
text2 = text[::-1]
print(steps)
print(text[0:15])
print(id(text))
print(id(dunno))
print(text2)
print(text2.upper())
print(text2.lower())
text = 'O' + text[1:]
text = text[:4] + 'M' + text[5:]
print(text)
text3 = "Ala ma kot, kot bardzo lubi Ale"
old = 'kot'
new = 'pies'
count = 1
replaced = text3.replace(old, new, count)
print(text3, id(text3))
print(replaced, id(replaced))