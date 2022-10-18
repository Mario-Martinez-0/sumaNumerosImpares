from functools import  reduce

tamanoLista = int(input("Ingrese el tamaño de la lista: "))
numerosDeLista = []

for i in range(0, tamanoLista):
    numeroIngresados = int(input(f'ingrese el pais N°{i + 1}: ' ))
    numerosDeLista.append(numeroIngresados)

def numeroImpar(x):
    if x % 2:
        return True

    return False

resultado = filter(numeroImpar, numerosDeLista)
resul = resultado

def suma(a, b):

    return a + b

resu = reduce(suma, resultado)
print(resu)
