# Función para devolver la pila que
# contiene la suma de dos números
def SumaListas(Lista1, Lista2):
    resultadoCola = []
    suma = 0
    remanente = 0

    while (len(Lista1) != 0 and len(Lista2) != 0):
        # Calcular la suma de la parte superior
        # elementos de ambas pilas
        suma = (remanente + Lista1[-1] + Lista2[-1])

        # Empuje la suma en la pila
        resultadoCola.append(suma % 10)

        # Almacenar el acarreo o remanente o sobreante de la division
        remanente = suma // 10

        # Pop los elementos superiores
        Lista1.pop(-1)
        Lista2.pop(-1)

        # Pop los elementos superiores
    while (len(Lista1) != 0):
        suma = remanente + Lista1[-1]
        resultadoCola.append(suma % 10)
        remanente = suma // 10
        Lista1.pop(-1)

    # Si lista2 no está vacío
    while (len(Lista2) != 0):
        suma = remanente + Lista2[-1]
        resultadoCola.append(suma % 10)
        remanente = suma // 10
        Lista2.pop(-1)

    # Si queda carry
    while (remanente > 0):
        resultadoCola.append(remanente)
        remanente //= 10

    # Invierta la pila para que
    # dígito más significativo es
    # en la parte inferior de la pila
    resultadoCola = resultadoCola[::-1]

    return resultadoCola


# Función para mostrar la pila resultante
def display(res):
    s = ""
    for i in res:
        s += str(i)

    print(s)



# código de conductor
lista1 = [  9]
# = [6,6]

lista2 = [ 9]


# Llamada de función
res = SumaListas(lista1, lista2)
print(res)


display(res)

# Este código es aportado por Shivam Singh