import sys
from pprint import pprint
import test
from package_example.functions import hello

print(sys.path)
print(test)

data = input('Podaj imie: ')

hello(data)
