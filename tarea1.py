

# Funciones

# Damos un texto y lo ponga en mayuscula y hacer test unitario
# Para poner mayus usamos texto.upper()

#texto = 'hola me llamo Cristian'
#print('El texto en mayúscula es:', texto.upper())

# Damos un texto y cuenta las palabras que contiene. Hacer test también

# texto.split() #-> Dividir un texto en palabras: Hace una lista
# len(texto.split) #<- longitud (Numero de palabras, cuenta las palabras de la lista en este caso)
#letras = len(palabras)

#print('El mensaje tiene:', len(texto.split()), 'palabras')

# Si queremos contar el número de letras que tiene una palabra, usamos el comando len() de esta forma:

#textoString = 'hola'
#print('La palabra', textoString, 'contiene', len(textoString), 'palabras')

def mayuscula(texto):
    return texto.upper()

def numero_palabras(texto):
    return len(texto.split())