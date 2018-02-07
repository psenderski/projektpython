# @TODO: pobierz od użytkownika dowolną liczbę lub znak
# @TODO: i sprawdź czy wprowadzone dane to liczba lub litera
# @TODO: wyświetl stosowny komunikat dla np. 'wprowadziłeś dane typu: liczba'
data = input('Podaj liczbe lub litere: ')
#data.isalpha()
#data.isdigit()

if data.isdigit():
    print('Podałeś liczbę')
    print('Bye')
elif data.isalpha():
    print('Podałeś literę')
    print('Bye')
else:
    print('HELP')