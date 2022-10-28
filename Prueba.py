
def es_impar(numero):
    resto = numero % 2
    if resto == 0: # El número es par
        return False
    else:
        return True

lista = (1, 3, 5, 4, 6, 8, 2, 10)
for numero in lista:
    print('Procesamos el numero', numero)
    respuesta = es_impar(numero)
    if respuesta : # respuesta == True
        print('El número es impar')
    else:
        print('El número es par')

#TAREA 1
# Funciones
# Damos un texto y lo ponga en mayuscula y hacer test unitario
# Para poner mayus usamos

# texto = 'hola'
# texto.upper()

def mayuscula(texto):
    return texto.upper()

# Damos un texto y cuenta las palabras que contiene. Hacer test también

# texto.split() -> Dividir un texto en palabras: Lista
# len(lista) <- longitud (Numero de palabras)

def numero_palabras(texto):
    return len(texto.split())

















