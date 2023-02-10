def Nombre_edad():
  print("1. Programa de nombre y edad")
  nombre = input("Por favor ingresa tu nombre: ")
  edad = int(input("Por favor ingresa tu edad: "))
  print(f"Hola {nombre}!, tu edad es: {edad}")
  print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
Nombre_edad()

def Area_circulo():
  print("2. Programa de radio del círculo")
  radio = int(input("Escriba el radio del círculo: "))
  area = (3.14159265359 * radio**2)
  redondeado = round(area, 2)
  print (f"El área del círculo es: {redondeado}cm")
  print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
Area_circulo()

def Numeros_aleatorios():
  print("3. Programa de números aleatorios")
  import random
  cantidad_numeros = int(input("Cúantos números aleatorios quiere generar?: "))
  lista_numero = []
  for i in range(cantidad_numeros):
    num_random = random.randint(1,100)
    lista_numero.append(num_random)
  print(f"La lista de numeros es: {lista_numero}")
  print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
Numeros_aleatorios()

def Numero_par_impar():
  print("4. Programa de números pares e impares")
  ingresar_numero = int(input("Digite el número para ver si es par o impar: "))
  if ingresar_numero % 2 == 0:
    print(f"El número: {ingresar_numero} es par")
  else: print(f"El número: {ingresar_numero} es impar")
  print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
Numero_par_impar()

def GradosF_aCelsius():
  print("5. Programa de conversión de Fahrenheit a Celsius")
  gradosF = int(input("Ingrese los grados en Fahrenheit: "))
  formulaCelsius = (gradosF - 32) / 1.8
  redondeado = round(formulaCelsius, 4)
  print(f"{gradosF} Fahrenheit equivalen a {redondeado} Celsius")
  print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
GradosF_aCelsius()

def Suma_lista():
  print("6. Programa de suma de elementos en una lista")
  import random
  lista = []
  cantidad = int(input("Ingresa la cantidad de números que quieres generar: "))
  for i in range(cantidad):
    numeros_random = random.randint(1,300)
    lista.append(numeros_random)
  sumatotal = sum(lista)
  print(lista)
  print(f"La suma de los números de la lista es: {sumatotal}")
  print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
Suma_lista()

def Numero_mayor_menor():
  print("7. Programa de numero menor o mayor")
  import random
  listanum = []
  cantidadnum = int(input("Ingresa la cantidad de números que quieres generar: "))
  for i in range(cantidadnum):
    numerosrandom = random.randint(1,100)
    listanum.append(numerosrandom)
  print(f"La lista es: {listanum}")
  numero_menor = listanum[0]
  numero_mayor = listanum[0]
  for i in range(len(listanum)):
      numero = listanum[i]
      if numero < numero_menor:
        numero_menor = numero
      if numero > numero_mayor:
        numero_mayor = numero
  print(f"El numero mayor es: {numero_mayor}")
  print(f"El numero menor es: {numero_menor}")
  print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
Numero_mayor_menor()

def Invertir_elementos():
  print("Programa de invertir lista")
  import random
  lista = []
  tamaño = 5
  for i in range(tamaño):
    numeros = random.randint(0,100)
    lista.append(numeros)
  print(f"La lista normal es: {lista}")
  print("La lista invertida es: ",list(reversed(lista)))
  print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
Invertir_elementos()

def Matriz():
  print("Programa de matriz")
  import random
  matriz = []
  for i in range(4):
      fila = []
      for j in range(4):
          fila.append(random.randint(1,100))
      matriz.append(fila)

  for fila in matriz:
      print(fila)
  print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
Matriz()


def Factorial_numero():
  print("Programa de factorial")
  num = int(input("Ingresa un numero para sacar el factorial: "))
  factorial = 1
  for i in range(1,num+1):
    factorial = factorial * i
  print(factorial)
  print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
Factorial_numero()


def Numeros_pares_1a100():
  print("Programa de numeros pares 0-100")
  lista = []
  for i in range(102):
    if i % 2 == 0:
      lista.append(i)
    else: None
  print(f"La lista de numeros pares es: {lista}")
  print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
Numeros_pares_1a100()

def imprimir():
  print("Programa de imprimir numeros 1-10")
  for i in range(11):
    print(i)
  print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
imprimir()


def Calculadora():
  print("Programa de calculadora")
  numero1 = int(input("Ingrese el primer numero: "))
  numero2 = int(input("Ingrese el segundo numero: "))
  suma =  numero1 + numero2
  resta = numero1 - numero2
  multiplicacion = numero1 * numero2
  division = numero1/numero2
  print(f"{numero1} + {numero2} es: {suma}")
  print(f"{numero1} - {numero2} es: {resta}")
  print(f"{numero1} * {numero2} es: {multiplicacion}")
  print(f"{numero1} / {numero2} es: {division}")
  print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
Calculadora()


def Media_aritmetica():
  print("Programa de media aritmética")
  import random
  lista = []
  num = 11
  for i in range(num):
    numero = random.randint(0,19)
    lista.append(numero)
  print(lista)
  suma = sum(lista)
  formula_media = round(suma / num, 3)
  print(f"La media aritmetica es: {formula_media}")
  print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
Media_aritmetica()


def palindromo():
  print("Programa de palindromos")
  palabra = input("Escribe una palabra: ")
  if palabra == palabra[::-1]:
    print(f"La palabra: {palabra} es palindroma")
  else: print(f"La palabra: {palabra} no es palindroma")
  print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
palindromo()