immutable_var = 1, 2, 3, 'q', 'w', 'e', False
print('immutable_var: ', immutable_var)
# immutable_var[3] = 'r' - кортеж является неизменным набором объектов, поэтому в нем нельзя изменить отдельные элементы
mutable_list = [4, 5, 't', 'y', True]
mutable_list[4] = False
print('mutable_list: ', mutable_list)
