from mailbox import NotEmptyError


array = [1,2,3,4,'teste',False,True,0.1]

print(array)

##primeiro elemento 
print(array[0])

#ultimo elemento
print(array[-1])

#parte do array
print(array[1:3])

#numero de elementos
print(len(array))

array = [7,6,5,4,3,2,1]
#ordenar o array
array.sort()#primeiro ordena
print(array)#depois mostra
array = [7,6,5,4,3,2,1]
print(sorted(array))

#inserir elemento no primeiro
array.insert(0,999)
print(array)

#inserir no ultimo
array.append(456)
print(array)

#remover um item
array.remove(999)
print(array)

#remove mais rápido
array[1] = None 
print(array)

del array[1]
print(array)

#valor minimo
print(min(array))

#valor máximo
print(max(array))

array.sort()

import bisect
#buscar a posição do elemento
print(bisect.bisect(array, 5))

##adicionar um item
bisect.insort(array,888)
print(array)

#numeros sequenciais
array = range(100)
print(array)
print(list(array))

#array de duas dimenções
two_array = [[123,456],[789,321]]
print(two_array)

print(two_array[0][0])

a = [1,2,3]
b = a
print(a)
print(b)

b = list(a)
b[0] = 999
print(b)
print(a)

a = [{'teste':123,'bbb':456}]
b = a
b[0]['teste'] = 999

print(a)
print(b)

import copy 
a = [{'teste':123,'bbb':456}]
b = copy.copy(a)
b[0]['teste'] = 999
print(a)

#não cria ponteiro
a = [{'teste':123,'bbb':456}]
b = copy.deepcopy(a)
b[0]['teste'] = 999
print(a)

#inverter posição
a = [1,2,3,4]
tmp1 = a[1]
tmp2 = a[2]
a[2] = tmp1 
a[1] = tmp2
print(a)

#mais facil
a[2],a[1] = a[1],a[2]
print(a)







