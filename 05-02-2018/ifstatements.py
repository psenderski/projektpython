a = 0
b = 2.34
text = 'abc'

if b > a:
    print('b > a')
elif b == a:
    print('b == a')
else:
    print('b < a')

result = a > b
print(type(result), result)

if text:
    print('text is not empty')

x = 1
y = 2
z = 3

#@ todo: if 'a' < 'h' < 'z'
if x < y < z:
    print('hurra!')

something = 'abc'
another = 'xyz'

if something == 'abc' and another == 'xyz':
    print('Strings are the same')

is_rest_equal_to_zero = 4 % 2

if not is_rest_equal_to_zero:
    print('the number is even')

name = 'Jan'
lastname = 'Kowalski'

if name == 'Jan' or lastname == 'Kowalski':
    print('siema!')

