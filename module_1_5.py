immutable_var = (1, 2, True, 'pensil')
print(immutable_var)
print(type(immutable_var))
# Кортеж относится к неизменяемым типам данных, поэтому нельзя изменить значения элементов кортежа.
mutable_list = [1, 2, 'book', 'mouse', 'barrel']
print(mutable_list)
print(type(mutable_list))
mutable_list[2] = 'magazine'
print(mutable_list)
