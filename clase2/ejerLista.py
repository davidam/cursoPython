lista = ["apple", "banana", "cherry", "orange", "kiwi"]
print(lista)
milista2 = sorted(lista, key=str.lower)
print(milista2)
lista.insert(2, "mango")
print(lista)
lista.remove("banana")
lista.remove("cherry")
print(lista)
lista.extend(["banana", "cherry"])
print(lista)
del lista[0]
print(lista)
print(lista[-1])
