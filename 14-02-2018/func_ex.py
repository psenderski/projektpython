def infinite_arguments(*args):
    print(args)
    print(type(args))

infinite_arguments(1, 2, 3, 4, 5)

print(sum([1, 2]))

#@ TODO: napisz funkcje ktora przyjmuje dowolna liczbe argumentow liczbowych
#@ TODO: i wyswietla na ekranie ich sume

def improved_sum(*args):
    print(sum(args))

improved_sum(1, 2, 3, 4, 5)
improved_sum(*[1, 2, 3])

x, y, z, *something = (1, 2, 3, 4, 5, 6)
*nevermind, a, b = (1, 10, 20, 30, 40)
print(nevermind)
print(a, b)

def foo(a, b, *args):
    """
    Foo function simply prints given arguments.
    :param a:
    :param b:
    :param args:
    :return:
    """
    print(a, b, args)

foo(1, 2)
foo(1, 2, 3, 4, 5, 6)
foo(1, 2, *range(100))

def bar(**kwargs):
    for key, value in kwargs.items():
        print(f'{key} -> {value}')

bar(a=1, b=2, zxc=4)
my_dict = {'Kowalski': 123, 'Nowak': 456}
bar(**my_dict)

def baz(x, y, **kwargs):
    pass

print()


def improved_sum_with_return(*args):
    '''
    Sum any numbers
    :param args:
    :return:
    '''
    value = sum(args)
    return value

values_to_sum = [1, 2, 10, 15]
result = improved_sum_with_return(*values_to_sum)
print(result)

def compare(a, b):
    """
    Returns True if a > b
    :param a:
    :param b:
    :return:
    """
    return a > b

print(compare(1, 2))
print(compare(4, 2))

#@ TODO: kawałek kodu
# while not data.isalpha() and not data.isdigit():
#       print('Podales zle dane, podaj jeszcze raz')
# data = input('Podaj liczbe lub litere: ')
#@ TODO: zamien na funkcje