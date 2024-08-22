my_dict = {'Pavel': 1985, 'Milana': 2014, 'Rodion': 2009}
print(my_dict)
print(my_dict['Pavel'])
print(my_dict.get('Anton', "Нет такого"))
my_dict.update({'Natasha': 1959, 'Yulia': 1984})
a = my_dict.pop('Milana')
print(a)
print(my_dict)

print()
my_set = {1, 1, 22, 22, 23, 'пыль', "пыль", True}
print(my_set)
#print(type(my_set))
my_set.add("book")
my_set.add((280, 55))
my_set.remove(22)
print(my_set)