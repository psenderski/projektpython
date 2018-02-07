data = input('Podaj liczbe lub litere: ')

while not data.isalpha() and not data.isdigit():
    print('Podales zle dane, podaj jeszcze raz')
    data = input('Podaj liczbe lub litere: ')

if data.isdigit():
    print('Podałeś liczbę')
elif data.isalpha():
    print('Podałeś literę')
print('bye!')