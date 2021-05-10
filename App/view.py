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
        print("")
        print(rta[2], rta[3])
        print(rta[0], rta[1])
        print("")

    elif int(inputs[0]) == 4:
        minimo_energy = float(input("Qué valor minimo quiere de la caractersitica energy?"))
        maximo_energy = float(input("Qué valor maximo quiere de la caracteristica energy?"))
        minimo_dance = float(input("Qué valor minimo quiere de la caracteristica danceability?"))
        maximo_dance = float(input("Qué valor maximo quiere de la caracteristica danceability?"))
        rta = controller.encontrar_pistas_unicas_req_2(analyzer,minimo_energy, maximo_energy,minimo_dance,maximo_dance)
        print("")
        print(rta[0], rta[1])
        print(rta[2])
        print(rta[3])
        print("")
    
    elif int(inputs[0]) == 5:
        minimo_instrumental = float(input("Qué valor minimo quiere de la caractersitica instrumentalness?"))
        maximo_instrumental = float(input("Qué valor maximo quiere de la caractersitica instrumentalness?"))
        minimo_tempo = float(input("Qué valor minimo quiere de la caracteristica tempo?"))
        maximo_tempo = float(input("Qué valor maximo quiere de la caracteristica tempo?"))
        rta = controller.encontrar_pistas_unicas_req_3(analyzer,minimo_instrumental, maximo_instrumental,minimo_tempo,maximo_tempo)
        print(rta)
        
    elif int(inputs[0]) == 6:
        booleano = 1
        if booleano == 1 :
                nombre = input("nombre unico para el nuevo genero musical?")
                valor_minimo = float(input("Qué valor minimo del tempo del nuevo genero musical?"))
                valor_maximo = float(input("Qué valor maximo del tempo del nuevo genero musical?"))
                print(nombre)
                rta = controller.encontrar_generos_musicales(analyzer,nombre,booleano,nombre,valor_minimo,valor_maximo)
        nombre ="x"
        valor_minimo = 0
        valor_maximo = 1
        genero_1 = "Reggae"
        print("Reggae:")
        rta_Reggae = controller.encontrar_generos_musicales(analyzer,genero_1,booleano,nombre,valor_minimo,valor_maximo)
        print(rta_Reggae[0],rta_Reggae[1])
        print(rta_Reggae[2],rta_Reggae[3])
        print(rta_Reggae[4])
        print(rta_Reggae[5])

        genero_2 = "Down_tempo"
        print("Down_tempo:")
        rta_Down_tempo = controller.encontrar_generos_musicales(analyzer,genero_2,booleano,nombre,valor_minimo,valor_maximo)
        print(rta_Down_tempo[0],rta_Down_tempo[1])
        print(rta_Down_tempo[2],rta_Down_tempo[3])
        print(rta_Down_tempo[4])
        print(rta_Down_tempo[5])

        genero_3 = "Chill_out"
        print("Chill_out:")
        rta_Chill_out = controller.encontrar_generos_musicales(analyzer,genero_3,booleano,nombre,valor_minimo,valor_maximo)
        print(rta_Chill_out[0],rta_Chill_out[1])
        print(rta_Chill_out[2],rta_Chill_out[3])
        print(rta_Chill_out[4])
        print(rta_Chill_out[5])

        genero_4 = "Hip_hop"
        print("Hip_hop:")
        rta_Hip_hop = controller.encontrar_generos_musicales(analyzer,genero_4,booleano,nombre,valor_minimo,valor_maximo)
        print(rta_Hip_hop[0],rta_Hip_hop[1])
        print(rta_Hip_hop[2],rta_Hip_hop[3])
        print(rta_Hip_hop[4])
        print(rta_Hip_hop[5])

        genero_5 = "Jazz_and_funk"
        print("Jazz_and_funk:")
        rta_Jazz_and_funk = controller.encontrar_generos_musicales(analyzer,genero_5,booleano,nombre,valor_minimo,valor_maximo)
        print(rta_Jazz_and_funk[0],rta_Jazz_and_funk[1])
        print(rta_Jazz_and_funk[2],rta_Jazz_and_funk[3])
        print(rta_Jazz_and_funk[4])
        print(rta_Jazz_and_funk[5])

        genero_6 = "Pop"
        print("Pop:")
        rta_Pop = controller.encontrar_generos_musicales(analyzer,genero_6,booleano,nombre,valor_minimo,valor_maximo)
        print(rta_Pop[0],rta_Pop[1])
        print(rta_Pop[2],rta_Pop[3])
        print(rta_Pop[4])
        print(rta_Pop[5])

        genero_7 = "R&B"
        print("R&B:")
        rta_R_B = controller.encontrar_generos_musicales(analyzer,genero_7,booleano,nombre,valor_minimo,valor_maximo)
        print(rta_R_B[0],rta_R_B[1])
        print(rta_R_B[2],rta_R_B[3])
        print(rta_R_B[4])
        print(rta_R_B[5])

        genero_8 = "Rock"
        print("Rock:")
        rta_Rock = controller.encontrar_generos_musicales(analyzer,genero_8,booleano,nombre,valor_minimo,valor_maximo)
        print(rta_Rock[0],rta_Rock[1])
        print(rta_Rock[2],rta_Rock[3])
        print(rta_Rock[4])
        print(rta_Rock[5])

        genero_9 = "Metal"
        print("Metal:")
        rta_Metal = controller.encontrar_generos_musicales(analyzer,genero_9,booleano,nombre,valor_minimo,valor_maximo)
        print(rta_Metal[0],rta_Metal[1])
        print(rta_Metal[2],rta_Metal[3])
        print(rta_Metal[4])
        print(rta_Metal[5])

    elif int(inputs[0]) == 7:
        minimo_dia = input("Qué valor minimo quiere de la hora de dia?")
        maximo_dia = input("Qué valor maximo quiere de la hora de dia?")
        rta = controller.genero_mas_escuchado(analyzer, minimo_dia, maximo_dia)
        print(rta)

    else:
        sys.exit(0)
sys.exit(0)
