#Santiago Castro Zuluaga - Reto 2 (Sumas)

import random
import time
import matplotlib.pyplot as plt

k = 100 #Numero de capturas

def funcion1(lista, busqueda):
  valores_suma = []
  for i in lista:
    for j in lista:
      if i + j == busqueda:
        valores_suma.append([i ,j])
  return valores_suma

def funcion2(lista, busqueda):
  valores_suma = []
  for i in lista:
    complemento = busqueda - i
    if complemento in lista:
        valores_suma.append([i, complemento])
  return valores_suma

def funcion3(lista, busqueda):
  valores_suma = []
  lista_ordenada = sorted(lista)

  for i in lista_ordenada:
      complemento = busqueda - i
      if busqueda_binaria(lista_ordenada, complemento):
          valores_suma.append([i, complemento])
  return valores_suma

def busqueda(lista, busqueda): # Busqueda (Llamando las funciones) (Todos las muestras por pantalla estan comentadas para ahorro de recuersos pero si es necesario es quitarle el comentario y se mostraran los tiempos de cada busqueda por cada numero)
  
  funcionC1 = []
  funcionC2 = []
  funcionC3 = []

   # Tiempo Funcion 1
  tiempo_tiempoFuncion1 = 0
  for _ in range(k):
    inicio_tiempoFuncion1 = time.time()
    resultado_funcion1 = funcion1(lista, busqueda)
    fin_busqueda_funcion1 = time.time()
    tiempo_tiempoFuncion1 = fin_busqueda_funcion1 - inicio_tiempoFuncion1
    funcionC1.append(tiempo_tiempoFuncion1)
    
    #for i, resultado in enumerate(funcion1(lista, busqueda), 1):
      #print("Números", i, ":", resultado[1])

  
  #print("Búsqueda Funcion 1: ")
  #print(funcionC1)
  #print("Este es el tiempo que tardó en buscar los números " + str(tiempo_tiempoFuncion1))
  #print(" ")

   # Tiempo Funcion 2
  tiempo_tiempoFuncion2 = 0
  for _ in range(k):
    inicio_tiempoFuncion2 = time.time()
    resultado_funcion2 = funcion2(lista, busqueda)
    fin_busqueda_funcion2 = time.time()
    tiempo_tiempoFuncion2 = fin_busqueda_funcion2 - inicio_tiempoFuncion2
    funcionC2.append(tiempo_tiempoFuncion2)
    #for i, resultado in enumerate(funcion2(lista, busqueda), 1):
      #print("Número", i, ":", resultado[1])

  #print("Búsqueda Funcion 2: ")
  #print(funcionC2)
  #print("Este es el tiempo que tardó en buscar los números " + str(tiempo_tiempoFuncion2))
  #print(" ")

   # Tiempo Funcion 3
  tiempo_tiempoFuncion3 = 0
  for _ in range(k):
    inicio_tiempoFuncion3 = time.time()
    resultado_funcion3 = funcion3(lista, busqueda)
    fin_busqueda_funcion3 = time.time()
    tiempo_tiempoFuncion3 = fin_busqueda_funcion3 - inicio_tiempoFuncion3
    funcionC3.append(tiempo_tiempoFuncion3)
    #for i, resultado in enumerate(funcion3(lista, busqueda), 1):
      #print("Número", i, ":", resultado[1])

  #print("Búsqueda Funcion 3: ")
  #print(funcionC1)
  #print("Este es el tiempo que tardó en buscar los números " + str(tiempo_tiempoFuncion1))
  #print(" ")
  
  for i, resultado in enumerate(funcion1(lista, busqueda), 1): #Este es el resultado de la busqueda
    print("Números", i, ":", resultado[1])
    
  Graficar(funcionC1, funcionC2, funcionC3, k)

def busqueda_binaria(lista_ordenada, elemento):
  inicio, fin = 0, len(lista_ordenada) - 1
  while inicio <= fin:
    medio = (inicio + fin) // 2
    valor_medio = lista_ordenada[medio]

    if valor_medio == elemento:
        return True
    elif valor_medio < elemento:
        inicio = medio + 1
    else:
        fin = medio - 1
    return False

def Graficar(funcionC1, funcionC2, funcionC3, k):
  # Crear una lista con números de iteración para el eje x
  iteraciones = list(range(1, k + 1))

  # Graficar los tiempos de búsqueda
  plt.plot(iteraciones, funcionC1, label='Búsqueda Funcion 1')
  plt.plot(iteraciones, funcionC2, label='Búsqueda Funcion 2')
  plt.plot(iteraciones, funcionC3, label='Búsqueda Funcion 3')


  # Configurar la gráfica
  plt.title('Tiempos de Búsqueda')
  plt.xlabel('Iteración')
  plt.ylabel('Tiempo (segundos)')
  plt.legend()  # Agregar leyenda

  # Guardar la gráfica como una imagen
  nombre_archivo = f"grafica_{iteraciones[-1]}.png"
  plt.savefig(nombre_archivo)

  # Mostrar la gráfica
  plt.show()    #Si se quiere seguir en el menu se tiene que comentar ya que almostrar la grafica el programa se cierra para mostrarlos datos en vivo

def main():
  aux = 1
  datos_ingresados = input("Ingrese la serie de datos separados por comas: ")
  lista = [int(dato) for dato in datos_ingresados.split(',')]
    
  while aux == 1:
      print("------------------------------------------")
      print("\nMenú:")
      print("1. Buscar")
      print("2. Salir")

      opcion = input("Selecciona una opción (1/2): ")

      if opcion == '1':
          #Busqueda tiempos
          aux2 = int(input("Ingrese el número que desea buscar: "))
          busqueda(lista, aux2)
      elif opcion == '2':
        print("Gracias por usar el programa")
        break
      else:
          print("Opción no válida. Por favor, elige 1, 2 o 3.")

if __name__ == "__main__":
    main()