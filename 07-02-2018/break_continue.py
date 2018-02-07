counter = 0
value = input('Podaj liczbe: ')
value = int(value)

# @TODO: wyświetl na ekran wartość counter
# @TODO: wyświetl tylko jeśli counter jest nieparzysty
while counter < value:
    if counter % 2:
        print(counter)
        counter += 1
    elif value > 1000:
        break
    else:
        counter += 1
        continue
print('bye')
