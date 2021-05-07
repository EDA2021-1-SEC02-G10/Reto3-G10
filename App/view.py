"""
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
from DISClib.DataStructures import listiterator as it
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
        minimo = float(input("Cúal es el valor mínimo de la caracteristica de contenido?"))
        maximo = float(input("Cúal es el valor mínimo de la caracteristica de contenido?"))
        rta = controller.clasificar_caracteristicas(analyzer, caracteristica, minimo, maximo)
        print(rta)

    elif int(inputs[0]) == 4:
        minimo_energy = float(input("Qué valor minimo quiere de la caractersitica energy?"))
        maximo_energy = float(input("Qué valor maximo quiere de la caracteristica energy?"))
        minimo_dance = float(input("Qué valor minimo quiere de la caractersitica danceability?"))
        maximo_dance = float(input("Qué valor maximo quiere de la caractersitica danceability?"))
        variable = "energy"
        variable_2 = "danceability"
        rta = controller.encontrar_pistas_unicas(analyzer,minimo_energy, maximo_energy,minimo_dance,maximo_dance,variable,variable_2)
        print(rta)
    
    elif int(inputs[0]) == 5:
        minimo_instrumental = float(input("Qué valor minimo quiere de la caractersitica instrumentalness?"))
        maximo_instrumental = float(input("Qué valor maximo quiere de la caractersitica instrumentalness?"))
        minimo_tempo = float(input("Qué valor minimo quiere de la caractersitica tempo?"))
        maximo_tempo = float(input("Qué valor maximo quiere de la caractersitica tempo?"))
        variable = "instrumentalness"
        variable_2 = "tempo"
        rta = controller.encontrar_pistas_unicas(analyzer,minimo_instrumental, maximo_instrumental,minimo_tempo,maximo_tempo,variable,variable_2)
        print(rta)
    elif int(inputs[0]) == 6:
        booleano = float(input("quiere agregar un genero?:"))
        if booleano == 1 :
                nombre = input("nombre unico para el nuevo genero musical?")
                valor_minimo = float(input("Qué valor minimo del tempo del nuevo genero musical?"))
                valor_maximo = float(input("Qué valor maximo del tempo del nuevo genero musical?"))
                print(nombre)
                rta = controller.encontrar_generos_musicales(analyzer,nombre,booleano,nombre,valor_minimo,valor_maximo)
                print(rta)
        nombre ="x"
        valor_minimo = 0
        valor_maximo = 1
        genero_1 = "Reggae"
        print("Reggae:")
        rta_Reggae = controller.encontrar_generos_musicales(analyzer,genero_1,booleano,nombre,valor_minimo,valor_maximo)
        print(rta_Reggae)

        genero_2 = "Down_tempo"
        print("Down_tempo:")
        rta_Down_tempo = controller.encontrar_generos_musicales(analyzer,genero_2,booleano,nombre,valor_minimo,valor_maximo)
        print(rta_Down_tempo)

        genero_3 = "Chill_out"
        print("Chill_out:")
        rta_Chill_out = controller.encontrar_generos_musicales(analyzer,genero_3,booleano,nombre,valor_minimo,valor_maximo)
        print(rta_Chill_out)

        genero_4 = "Hip_hop"
        print("Hip_hop:")
        rta_Hip_hop = controller.encontrar_generos_musicales(analyzer,genero_4,booleano,nombre,valor_minimo,valor_maximo)
        print(rta_Hip_hop)

        genero_5 = "Jazz_and_funk"
        print("Jazz_and_funk:")
        rta_Jazz_and_funk = controller.encontrar_generos_musicales(analyzer,genero_5,booleano,nombre,valor_minimo,valor_maximo)
        print(rta_Jazz_and_funk)

        genero_6 = "Pop"
        print("Pop:")
        rta_Pop = controller.encontrar_generos_musicales(analyzer,genero_6,booleano,nombre,valor_minimo,valor_maximo)
        print(rta_Pop)

        genero_7 = "R&B"
        print("R&B:")
        rta_R_B = controller.encontrar_generos_musicales(analyzer,genero_7,booleano,nombre,valor_minimo,valor_maximo)
        print(rta_R_B)

        genero_8 = "Rock"
        print("Rock:")
        rta_Rock = controller.encontrar_generos_musicales(analyzer,genero_8,booleano,nombre,valor_minimo,valor_maximo)
        print(rta_Rock)

        genero_9 = "Metal"
        print("Metal:")
        rta_Metal = controller.encontrar_generos_musicales(analyzer,genero_9,booleano,nombre,valor_minimo,valor_maximo)
        print(rta_Metal)

    elif int(inputs[0]) == 7:
        minimo_dia = input("Qué valor minimo quiere de la hora de dia?")
        maximo_dia = input("Qué valor maximo quiere de la hora de dia?")

    else:
        sys.exit(0)
sys.exit(0)
