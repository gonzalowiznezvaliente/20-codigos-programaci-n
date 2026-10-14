
# ==========================================
# 1. BIFURCACIONES (if / elif / else)
# ==========================================

# Algoritmo: Signo de un número
# Entrada: numero (número real o entero)
# Salida: texto ("positivo", "negativo" o "cero")
# Inicio
#   Si numero > 0 entonces Devolver "positivo"
#   Sino, si numero < 0 entonces Devolver "negativo"
#   Sino Devolver "cero"
# Fin
def signo_numero(numero):
    """Devuelve si un número es positivo, negativo o cero."""
    if numero > 0:
        return "positivo"
    elif numero < 0:
        return "negativo"
    else:
        return "cero"


# Algoritmo: Año bisiesto
# Entrada: anio (número entero)
# Salida: booleano (True o False)
# Inicio
#   Si (anio % 4 == 0 y anio % 100 != 0) o (anio % 400 == 0) entonces Devolver True
#   Sino Devolver False
# Fin
def es_bisiesto(anio):
    """Determina si un año es bisiesto."""
    if (anio % 4 == 0 and anio % 100 != 0) or (anio % 400 == 0):
        return True
    else:
        return False


# Algoritmo: El mayor de tres números
# Entrada: a, b, c (números)
# Salida: el mayor de los tres
# Inicio
#   Si a >= b y a >= c entonces Devolver a
#   Sino, si b >= a y b >= c entonces Devolver b
#   Sino Devolver c
# Fin
def mayor_de_tres(a, b, c):
    """Devuelve el mayor de tres números sin usar max()."""
    if a >= b and a >= c:
        return a
    elif b >= a and b >= c:
        return b
    else:
        return c


# Algoritmo: Categoría de envío según el peso
# Entrada: peso_kg (número real)
# Salida: texto con la categoría de envío
# Inicio
#   Si peso_kg <= 1 entonces Devolver "Sobre"
#   Sino, si peso_kg <= 5 entonces Devolver "Paquete pequeño"
#   Sino, si peso_kg <= 20 entonces Devolver "Paquete grande"
#   Sino Devolver "Voluminoso"
# Fin
def categoria_envio(peso_kg):
    """Clasifica un envío según su peso en kilos."""
    if peso_kg <= 1:
        return "Sobre"
    elif peso_kg <= 5:
        return "Paquete pequeño"
    elif peso_kg <= 20:
        return "Paquete grande"
    else:
        return "Voluminoso"



# ==========================================
# 2. ITERACIONES (for y while)
# ==========================================

# Algoritmo: Suma de pares entre 1 y n
# Entrada: n (entero positivo)
# Salida: suma de los números pares
# Inicio
#   suma <- 0
#   Para i desde 1 hasta n hacer
#       Si i % 2 == 0 entonces suma <- suma + i
#   Fin Para
#   Devolver suma
# Fin
def suma_pares(n):
    """Suma los números pares entre 1 y n."""
    suma = 0
    for i in range(1, n + 1):
        if i % 2 == 0:
            suma += i
    return suma


# Algoritmo: Factorial con bucle
# Entrada: n (entero no negativo)
# Salida: factorial de n (n!)
# Inicio
#   resultado <- 1
#   Para i desde 2 hasta n hacer resultado <- resultado * i
#   Devolver resultado
# Fin
def factorial_iterativo(n):
    """Calcula n! usando un bucle (versión iterativa)."""
    resultado = 1
    for i in range(2, n + 1):
        resultado *= i
    return resultado


# Algoritmo: Contar vocales de una palabra
# Entrada: palabra (texto)
# Salida: contador de vocales (entero)
# Inicio
#   contador <- 0
#   Para cada caracter en minúscula(palabra) hacer
#       Si caracter en "aeiou" entonces contador <- contador + 1
#   Devolver contador
# Fin
def contar_vocales(palabra):
    """Cuenta las vocales de una palabra, sin distinguir mayúsculas."""
    contador = 0
    vocales = "aeiou"
    for char in palabra.lower():
        if char in vocales:
            contador += 1
    return contador


# Algoritmo: Tabla de multiplicar
# Entrada: numero (entero)
# Salida: impresión por pantalla de la tabla del 1 al 10
# Inicio
#   Para i desde 1 hasta 10 hacer Imprimir numero x i = resultado
# Fin
def tabla_multiplicar(numero):
    """Imprime la tabla de multiplicar de un número, del 1 al 10."""
    for i in range(1, 11):
        print(f"{numero}x{i}={numero * i}")



# ==========================================
# 3. FUNCIONES
# ==========================================

# Algoritmo: Promedio de una lista de números
# Entrada: numeros (lista de números)
# Salida: media aritmética (número real)
# Inicio
#   Si la lista está vacía entonces devolver 0.0
#   Devolver suma(numeros) / longitud(numeros)
# Fin
def calcular_promedio(numeros):
    """Calcula la media aritmética de una lista de números."""
    if not numeros:
        return 0.0
    return sum(numeros) / len(numeros)


# Algoritmo: Texto en mayúsculas y número de palabras
# Entrada: frase (texto)
# Salida: frase en mayúsculas y número de palabras
# Inicio
#   frase_mayus <- mayúscula(frase)
#   num_palabras <- longitud(dividir(frase))
#   Devolver frase_mayus, num_palabras
# Fin
def analizar_frase(frase):
    """Devuelve la frase en mayúsculas junto con su número de palabras."""
    frase_mayus = frase.upper()
    num_palabras = len(frase.split())
    return frase_mayus, num_palabras


# Algoritmo: Validar contraseña
# Entrada: contrasena (texto), longitud_minima (entero, por defecto 8)
# Salida: booleano (True o False)
# Inicio
#   Devolver longitud(contrasena) >= longitud_minima
# Fin
def validar_contrasena(contrasena, longitud_minima=8):
    """Comprueba si una contraseña alcanza la longitud mínima exigida."""
    return len(contrasena) >= longitud_minima


# Algoritmo: Conversión de temperatura
# Entrada: celsius / fahrenheit
# Salida: temperatura convertida
# Inicio Celsius a Fahrenheit: Devolver (celsius * 9/5) + 32
# Inicio Fahrenheit a Celsius: Devolver (fahrenheit - 32) * 5/9
# Fin
def celsius_a_fahrenheit(celsius):
    """Convierte una temperatura de Celsius a Fahrenheit."""
    return (celsius * 9/5) + 32

def fahrenheit_a_celsius(fahrenheit):
    """Convierte una temperatura de Fahrenheit a Celsius."""
    return (fahrenheit - 32) * 5/9



# ==========================================
# 4. FUNCIONES RECURSIVAS
# ==========================================

# Algoritmo: Factorial recursivo
# Entrada: n (entero no negativo)
# Salida: factorial de n (n!)
# Inicio
#   Si n == 0 entonces Devolver 1
#   Sino Devolver n * factorial_recursivo(n - 1)
# Fin
def factorial_recursivo(n):
    """Calcula n! llamándose a sí misma (versión recursiva)."""
    if n == 0:
        return 1
    return n * factorial_recursivo(n - 1)


# Algoritmo: Sucesión de Fibonacci
# Entrada: n (entero no negativo)
# Salida: término n-ésimo de Fibonacci
# Inicio
#   Si n == 0 entonces devolver 0
#   Si n == 1 entonces devolver 1
#   Devolver fibonacci(n - 1) + fibonacci(n - 2)
# Fin
def fibonacci(n):
    """Devuelve el término n de la sucesión de Fibonacci."""
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)


# Algoritmo: Suma recursiva de una lista
# Entrada: numeros (lista de números)
# Salida: suma total de los elementos
# Inicio
#   Si la lista está vacía entonces devolver 0
#   Devolver primer_elemento + suma_lista(resto_de_la_lista)
# Fin
def suma_lista(numeros):
    """Suma los elementos de una lista de forma recursiva."""
    if not numeros:
        return 0
    return numeros[0] + suma_lista(numeros[1:])


# Algoritmo: Invertir una cadena de texto
# Entrada: texto (cadena de caracteres)
# Salida: texto invertido
# Inicio
#   Si longitud de texto <= 1 entonces devolver texto
#   Devolver invertir_texto(resto) + primer_caracter
# Fin
def invertir_texto(texto):
    """Invierte una cadena de texto de forma recursiva."""
    if len(texto) <= 1:
        return texto
    return invertir_texto(texto[1:]) + texto[0]



# ==========================================
# 5. EXCEPCIONES (try / except)
# ==========================================

# Algoritmo: División segura
# Entrada: a, b (números)
# Salida: resultado de la división o mensaje de error
# Inicio
#   Intentar: Devolver a / b
#   Capturar ZeroDivisionError: Devolver "Error: división entre cero"
# Fin
def division_segura(a, b):
    """Divide dos números controlando la división entre cero."""
    try:
        return a / b
    except ZeroDivisionError:
        return "Error: división entre cero"


# Algoritmo: Convertir texto a número
# Entrada: texto (cadena)
# Salida: número entero o mensaje de error
# Inicio
#   Intentar: Devolver entero(texto)
#   Capturar ValueError: Devolver "Error: no es un número"
# Fin
def convertir_a_entero(texto):
    """Convierte un texto a entero controlando el error de formato."""
    try:
        return int(texto)
    except ValueError:
        return "Error: no es un número"


# Algoritmo: Acceso seguro a una lista
# Entrada: lista, posicion (entero)
# Salida: elemento en la posición o mensaje de error
# Inicio
#   Intentar: Devolver lista[posicion]
#   Capturar IndexError: Devolver "Error: posición fuera de rango"
# Fin
def obtener_elemento(lista, posicion):
    """Accede a una posición de una lista controlando el error de rango."""
    try:
        return lista[posicion]
    except IndexError:
        return "Error: posición fuera de rango"


# Algoritmo: Calculadora con control de errores
# Entrada: texto_a, texto_b, operacion ("suma" o "division")
# Salida: resultado numérico o mensaje de error específico
# Inicio
#   Intentar convertir a float, operar según corresponda
#   Capturar errores de formato o división por cero
# Fin
def calculadora_segura(texto_a, texto_b, operacion):
    """Suma o divide dos textos numéricos controlando los errores posibles."""
    try:
        num_a = float(texto_a)
        num_b = float(texto_b)
        
        if operacion == "suma":
            return num_a + num_b
        elif operacion == "division":
            return num_a / num_b
    except ValueError:
        return "Error: valor no numérico"
    except ZeroDivisionError:
        return "Error: división entre cero"



# ==========================================
# BLOQUE DE PRUEBAS (__main__)
# ==========================================
if __name__ == "__main__":
    print("--- 1. Bifurcaciones ---")
    print(signo_numero(-5))
    print(es_bisiesto(2024))
    print(mayor_de_tres(4, 9, 2))
    print(categoria_envio(15))
    
    print("\n--- 2. Iteraciones ---")
    print(suma_pares(10))
    print(factorial_iterativo(5))
    print(contar_vocales('Programacion'))
    tabla_multiplicar(3)
    
    print("\n--- 3. Funciones ---")
    print(calcular_promedio([4, 8, 6]))
    print(analizar_frase('hola que tal'))
    print(validar_contrasena('abc123', 5))
    print(celsius_a_fahrenheit(0))
    
    print("\n--- 4. Recursivas ---")
    print(factorial_recursivo(5))
    print(fibonacci(6))
    print(suma_lista([1, 2, 3, 4]))
    print(invertir_texto('python'))
    
    print("\n--- 5. Excepciones ---")
    print(division_segura(10, 0))
    print(convertir_a_entero('hola'))
    print(obtener_elemento([1, 2, 3], 9))
    print(calculadora_segura('10', '0', 'division'))