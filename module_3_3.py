def print_params(a=1, b='string', c=True):
    print(a, b, c)


print_params()  # вызов функции без аргументов
print_params(555)  # вызов функции с одним другим аргументом
print_params(879, 8555)  # вызов функции с двумя другими аргументами
print_params(9879, False, "вызов")  # вызов функции с тремя другими аргументами

print_params(b=25)

print_params(c=[1, 2, 3])

values_list = [True, "яблоко", 23]
print_params(*values_list)

values_dict = {'a': True, 'b': 5, 'c': 'номер'}
print_params(**values_dict)

values_list_2 = [54.32, 'Строка']
print_params(*values_list_2, 42)
