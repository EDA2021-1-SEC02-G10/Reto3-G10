﻿"""
 * Copyright 2020, Departamento de sistemas y Computación, Universidad
 * de Los Andes
 *
 *
 * Desarrolado para el curso ISIS1225 - Estructuras de Datos y Algoritmos
 *
 *
 * This program is free software: you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation, either version 3 of the License, or
 * (at your option) any later version.
 *
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 *
 * You should have received a copy of the GNU General Public License
 * along withthis program.  If not, see <http://www.gnu.org/licenses/>.
 """

import config as cf
import sys
import controller
from DISClib.ADT import list as lt
assert cf


"""
La vista se encarga de la interacción con el usuario
Presenta el menu de opciones y por cada seleccion
se hace la solicitud al controlador para ejecutar la
operación solicitada
"""

def printMenu():
    print("Bienvenido")
    print("1- Inicializar Analizador")
    print("2- Cargar información")
    print("3- Cuantas reproducciones se tienen en el sistema")
    print("4- Encontrar música para festejar")
    print("5- Encontrar música para estudiar")
    print("6- Estudiar los géneros musicales")
    print("7- Indicar el género musical más escuhcado en el tiempo")
    print("0- Salir")

catalog = None

"""
Menu principal
"""
while True:
    printMenu()
    inputs = input('Seleccione una opción para continuar\n')
    if int(inputs[0]) == 1:
        print("Inicializando ....")
        cont = controller.init()

    elif int(inputs[0]) == 2:
        print("\nCargando información ....")
        analyzer = controller.loadData(cont, "context_content_features-small")
    
    elif int(inputs[0]) == 3:
        caracteristica = input("Qué caracteristica quiere buscar?")
        minimo = input("Cúal es el valor mínimo de la caracteristica de contenido?")
        maximo = input("Cúal es el valor mínimo de la caracteristica de contenido?")
        rta = controller.clasificar_caracteristicas(analyzer, caracteristica, minimo, maximo)
        print(rta)

    elif int(inputs[0]) == 4:
        minimo_energy = input("Qué valor minimo quiere de la caractersitica energy?")
        maximo_energy = input("Qué valor maximo quiere de la caracteristica energy?")
        minimo_dance = input("Qué valor minimo quiere de la caractersitica danceability?")
        maximo_dance = input("Qué valor maximo quiere de la caractersitica danceability?")
        rta = controller.encontrar_pistas_unicas(analyzer,minimo_energy, maximo_energy,minimo_dance,maximo_dance)
        lista = controller.encontrar_5_videos(analyzer,minimo_energy, maximo_energy,minimo_dance,maximo_dance)
        print(lista)
    
    elif int(inputs[0]) == 5:
        minimo_instrumental = input("Qué valor minimo quiere de la caractersitica instrumentalness?")
        maximo_instrumental = input("Qué valor maximo quiere de la caractersitica instrumentalness?")
        minimo_tempo = input("Qué valor minimo quiere de la caractersitica tempo?")
        maximo_tempo = input("Qué valor maximo quiere de la caractersitica tempo?")
    
    elif int(inputs[0]) == 6:
        pass

    elif int(inputs[0]) == 7:
        minimo_dia = input("Qué valor minimo quiere de la hora de dia?")
        maximo_dia = input("Qué valor maximo quiere de la hora de dia?")

    else:
        sys.exit(0)
sys.exit(0)
