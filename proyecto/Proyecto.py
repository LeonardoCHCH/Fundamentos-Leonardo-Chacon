#PROYECTO PROGRAMACION LEONARDO CHACON CI:31895402, RAUL GONZALEZ CI:32324654

#funcion para ubicar la posicion del caracter en la contrasena
def ubicar_letra(letra, tipo_caracter):
    for i in range(len(tipo_caracter)):
        if letra == tipo_caracter[i]:
            return i


#funcion que encripta el mensaje por primer vez, simplemente revisa que tipo de caracter es, lo ubica en su respectiba libreria
#y lo mueve ciertos espacios adelante dependiendo de la clave, de tal forma que caiga en un caracter completamente distinto y se vaya encriptando poco a poco :)
def primera_encripcion(contrasena, key1):
    letra_nueva=""
    mayusculas = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    minusculas = "abcdefghijklmnopqrstuvwxyz"
    numeros = "0123456789"
    especiales = ".,<>/?'[]{}=+)(-_*&^%$#@!~`;:\|"
    contrasena_encriptada1 = ""
#aca saca el modulo con la longitud de la libreria respectiva de tal forma que si la clave hace que se pase de la cantidad de espacios posibles, de la vuelta y empiece desde el inicio
    for letra in contrasena:
        if letra in mayusculas:
            letra_nueva = (ubicar_letra(letra, mayusculas) + key1 ) % len(mayusculas)
            contrasena_encriptada1 += mayusculas[letra_nueva]
        elif letra in minusculas:
            letra_nueva = (ubicar_letra(letra, minusculas) + key1 ) % len(minusculas)
            contrasena_encriptada1 += minusculas[letra_nueva]
        elif letra in numeros:
            letra_nueva = (ubicar_letra(letra, numeros) + key1 ) % len(numeros)
            contrasena_encriptada1 += numeros[letra_nueva]
        elif letra in especiales:
            letra_nueva = (ubicar_letra(letra, especiales) + key1 ) % len(especiales)
            contrasena_encriptada1 += especiales[letra_nueva]
        else:
            letra_nueva = " "
            contrasena_encriptada1 += letra_nueva
    return contrasena_encriptada1
#segunda encripcion tomando el ultimo digito de la cedula como la nueva clave
def segunda_encripcion(contrasena, key_cedula):
    letra_nueva=""
    mayusculas = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    minusculas = "abcdefghijklmnopqrstuvwxyz"
    numeros = "0123456789"
    especiales = ".,<>/?'[]{}=+)(-_*&^%$#@!~`;:\|"
    contrasena_encriptada2 = ""

    for letra in contrasena:
        if letra in mayusculas:
            letra_nueva = (ubicar_letra(letra, mayusculas) + key_cedula ) % len(mayusculas)
            contrasena_encriptada2 += mayusculas[letra_nueva]
        elif letra in minusculas:
            letra_nueva = (ubicar_letra(letra, minusculas) + key_cedula ) % len(minusculas)
            contrasena_encriptada2 += minusculas[letra_nueva]
        elif letra in numeros:
            letra_nueva = (ubicar_letra(letra, numeros) + key_cedula ) % len(numeros)
            contrasena_encriptada2 += numeros[letra_nueva]
        elif letra in especiales:
            letra_nueva = (ubicar_letra(letra, especiales) + key_cedula ) % len(especiales)
            contrasena_encriptada2 += especiales[letra_nueva]
        else:
            letra_nueva = " "
            contrasena_encriptada2 += letra_nueva
    return contrasena_encriptada2
#y las dos desencripciones donde basicamente en vez de sumar la clave se le resta para poder llegar a la posicion original de la letra
def primera_desencripcion(contrasena, key_cedula):
    letra_nueva=""
    mayusculas = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    minusculas = "abcdefghijklmnopqrstuvwxyz"
    numeros = "0123456789"
    especiales = ".,<>/?'[]{}=+)(-_*&^%$#@!~`;:\|"
    contrasena_desencriptada1 = ""

    for letra in contrasena:
        if letra in mayusculas:
            letra_nueva = (ubicar_letra(letra, mayusculas) - key_cedula ) % len(mayusculas)
            contrasena_desencriptada1 += mayusculas[letra_nueva]
        elif letra in minusculas:
            letra_nueva = (ubicar_letra(letra, minusculas) - key_cedula ) % len(minusculas)
            contrasena_desencriptada1 += minusculas[letra_nueva]
        elif letra in numeros:
            letra_nueva = (ubicar_letra(letra, numeros) - key_cedula ) % len(numeros)
            contrasena_desencriptada1 += numeros[letra_nueva]
        elif letra in especiales:
            letra_nueva = (ubicar_letra(letra, especiales) - key_cedula ) % len(especiales)
            contrasena_desencriptada1 += especiales[letra_nueva]
        else:
            letra_nueva = " "
            contrasena_desencriptada1 += letra_nueva
    return contrasena_desencriptada1

def segunda_desencripcion(contrasena, key1):
    letra_nueva=""
    mayusculas = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    minusculas = "abcdefghijklmnopqrstuvwxyz"
    numeros = "0123456789"
    especiales = ".,<>/?'[]{}=+)(-_*&^%$#@!~`;:\|"
    contrasena_desencriptada2 = ""

    for letra in contrasena:
        if letra in mayusculas:
            letra_nueva = (ubicar_letra(letra, mayusculas) - key1 ) % len(mayusculas)
            contrasena_desencriptada2 += mayusculas[letra_nueva]
        elif letra in minusculas:
            letra_nueva = (ubicar_letra(letra, minusculas) - key1 ) % len(minusculas)
            contrasena_desencriptada2 += minusculas[letra_nueva]
        elif letra in numeros:
            letra_nueva = (ubicar_letra(letra, numeros) - key1 ) % len(numeros)
            contrasena_desencriptada2 += numeros[letra_nueva]
        elif letra in especiales:
            letra_nueva = (ubicar_letra(letra, especiales) - key1 ) % len(especiales)
            contrasena_desencriptada2 += especiales[letra_nueva]
        else:
            letra_nueva = " "
            contrasena_desencriptada2 += letra_nueva
    return contrasena_desencriptada2
def calcular_dificultad_letras(contrasena):
    puntos = 0
    mayusculas = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    minusculas = "abcdefghijklmnopqrstuvwxyz"
    numeros = "0123456789"
    caracteres_especiales = ".,<>/?'[]{}=+)(-_*&^%$#@!~`;:\|"
    primer_especial = True
    for letra in contrasena:
        puntos += 1
        if letra in mayusculas:
            puntos += 1
        elif letra in minusculas:
            puntos += 1
        elif letra in caracteres_especiales:
            if primer_especial:
                puntos += 3
                primer_especial = False
            else:
                puntos += 2
    return puntos
def restar_puntos_dificultad(contrasena):
    se_repite = False
    for i in range(len(contrasena)-1):
        caracter = contrasena[i]
        caracter_consecuente = contrasena [i+1]
        if (caracter.isdigit()) and (caracter_consecuente.isdigit()) or (caracter == caracter_consecuente) or (caracter.isspace()) and (caracter_consecuente.isspace()):
            puntaje_total = calcular_dificultad_letras(contrasena) - 5
            return puntaje_total

def declarar_dificultad(contrasena):
    puntaje = restar_puntos_dificultad(contrasena)
    if puntaje <= 15:
        return "Dificultad Debil"
    elif puntaje > 15 and puntaje <= 20:
        return "Dificultad Moderada"
    elif puntaje > 20 and puntaje <= 35:
        return "Dificultad Buena"
    elif puntaje > 35 and puntaje < 100:
        return "Dificultad excelente"
    elif puntaje > 99:
        return "Dificultad indescifrable"


#declaramos las variables y usamos las funciones
archivo = open('contrasena.txt', 'r')
contrasena = archivo.read()
key1 = int(input("Ingrese un digito, el cual sera usado como la clave de encripcion de su mensaje: "))
cedula = int(input("Ingrese su cedula: "))
key_cedula = cedula % 10

primer_encripcion = primera_encripcion(contrasena, key1)
contrasena_encriptada = segunda_encripcion(primer_encripcion, key_cedula)
print("Su contrasena encriptada es : ", contrasena_encriptada)

primer_desencripcion = primera_desencripcion(contrasena_encriptada, key1)
contrasena_desencriptada = segunda_desencripcion(primer_desencripcion, key_cedula)

archivo_salida = open('ArchivoDeSalida.txt', 'w')
archivo_salida.write(str(contrasena_encriptada) + ' | ' + str(declarar_dificultad(contrasena)) + ' | ' + str(restar_puntos_dificultad(contrasena)) + ' | ' + str(key1) + ' | ' + str(primer_encripcion) + ' | ' + str(key_cedula))
archivo.close()
archivo_salida.close()

