"""
 * Copyright 2020, Departamento de sistemas y Computación,
 * Universidad de Los Andes
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
import model
import csv


"""
El controlador se encarga de mediar entre la vista y el modelo.
"""

# Inicialización del Catálogo de libros

def init():
    """
    Llama la funcion de inicializacion  del modelo.
    """
    # catalog es utilizado para interactuar con el modelo
    analyzer = model.newAnalyzer()
    model.actualizar_Caracteristica(analyzer)
    model.crearHastGenre(analyzer)
    return analyzer

# Funciones para la carga de datos

def loadData(analyzer, music):
    """
    Carga los datos de los archivos CSV en el modelo
    """
    Eventos_file1 = cf.data_dir + ("context_content_features-small.csv")
    Eventos_file2 = cf.data_dir + ("user_track_hashtag_timestamp-small.csv")
    Eventos_file3 = cf.data_dir + ("sentiment_values.csv")


    input_file1 = csv.DictReader(open(Eventos_file1, encoding="utf-8"),
                                delimiter=",")
    input_file2 = csv.DictReader(open(Eventos_file2, encoding="utf-8"),
                                delimiter=",")
    input_file3 = csv.DictReader(open(Eventos_file3, encoding="utf-8"),
                                delimiter=",")
    for cancion in input_file1:
        model.AppCaracteristica(analyzer, cancion)
    """for cancion in input_file2:
        #model.AppCaracteristica(analyzer, cancion)
    for cancion in input_file3:
        #model.AppCaracteristica(analyzer, cancion)"""
        
    return analyzer


# Funciones de ordenamiento

#req 1
def clasificar_caracteristicas(analyzer, caracteristica, minimo, maximo):
    return model.clasificar_caracteristicas (analyzer, caracteristica, minimo, maximo)

#req 2 
def encontrar_pistas_unicas_req_2(analyzer,minimo_energy, maximo_energy,minimo_dance,maximo_dance,variable,variable_2):
    return model.encontrar_pistas_unicas_req_2(analyzer,minimo_energy, maximo_energy,minimo_dance,maximo_dance,variable,variable_2)

#req 3
def encontrar_pistas_unicas_req_3(analyzer,minimo_instrumentalness, maximo_instrumentalness,minimo_tempo,maximo_tempo,variable,variable_2):
    return model.encontrar_pistas_unicas_req_3(analyzer,minimo_instrumentalness, maximo_instrumentalness,minimo_tempo,maximo_tempo,variable,variable_2)

#req 4
def encontrar_generos_musicales(analyzer,genero,booleano,nombre,valor_minimo,valor_maximo):
    return model.encontrar_generos_musicales(analyzer,genero,booleano,nombre,valor_minimo,valor_maximo)

# Funciones de consulta sobre el catálogo
