
# APPEND
lista = [1, 2, 3, 4]
print(lista)

lista.append([5, 6, 7])
print(lista)

# EXTEND
lista_two = [7, 6, 5, 4]
print(lista_two)

lista_two.extend([3, 2, 1])
print(lista_two)
print("\n")

# # # RESULT # # #
#[1, 2, 3, 4]
#[1, 2, 3, 4, [5, 6, 7]]
#[7, 6, 5, 4]
#[7, 6, 5, 4, 3, 2, 1]

# INSERT
list_three = [1, 2, 3]
print(list_three)

list_three.insert(2, 'Hi')
print(list_three)

list_three.insert(4, 'blow your mind')
print(list_three)

print(list_three.index('blow your mind'))

list_three.insert(len(list_three), "comone loud")
print(list_three)