digits = {
    'cztery': 4,
    'dwa': '2'
}

digit = input('Podaj liczbe: ')

try:
   result = digits[digit] - digits['dwa']
except Exception as error:
    print(f'nie ma takiego klucza jak: {error}')
finally:
    print('goodbye')