import os

FILENAME = 'dlugosc_pliku.txt'

file_size = os.path.getsize(FILENAME)
print(f'rozmiar pliku: {file_size}')

with open(FILENAME) as plik:
    total_chars = 0
    for line in plik:
        # linia z pliku
        total_chars += len(line)
    print(total_chars)