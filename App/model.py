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
 *
 * Contribuciones:
 *
 * Dario Correal - Version inicial
 """


import config
from DISClib.ADT import list as lt
from DISClib.ADT import orderedmap as om
from DISClib.DataStructures import mapentry as me
from DISClib.ADT import map as m
import datetime
assert config

"""
Se define la estructura de un catálogo de videos. El catálogo tendrá dos listas, una para los videos, otra para las categorias de
los mismos.
"""

# Construccion de modelos

def newAnalyzer():
    """ Inicializa el analizador

    Crea una lista vacia para guardar todos los crimenes
    Se crean indices (Maps) por los siguientes criterios:
    -Fechas

    Retorna el analizador inicializado.
    """
    analyzer = {'Caracteristica': None}
    analyzer["Caracteristica"] = m.newMap(numelements=30,
                                            prime=109345121,
                                            maptype='PROBING',
                                            loadfactor=0.5,
                                            comparefunction=compareDates)
    
    return analyzer

# Funciones para agregar informacion al catalogo

def actualizar_Caracteristica(analyzer):

    Arbol1 = om.newMap(omaptype='RBT',
                                      comparefunction=compareDates)
    Arbol2 = om.newMap(omaptype='RBT',
                                      comparefunction=compareDates)
    Arbol3 = om.newMap(omaptype='RBT',
                                      comparefunction=compareDates)
    Arbol4 = om.newMap(omaptype='RBT',
                                      comparefunction=compareDates)
    Arbol5 = om.newMap(omaptype='RBT',
                                      comparefunction=compareDates)
    Arbol6 = om.newMap(omaptype='RBT',
                                      comparefunction=compareDates)
    Arbol7 = om.newMap(omaptype='RBT',
                                      comparefunction=compareDates)
    Arbol8 = om.newMap(omaptype='RBT',
                                      comparefunction=compareDates)
    Arbol9 = om.newMap(omaptype='RBT',
                                      comparefunction=compareDates)

    m.put(analyzer["Caracteristica"], "instrumetalness", Arbol1)
    m.put(analyzer["Caracteristica"], "liveness", Arbol2)
    m.put(analyzer["Caracteristica"], "speechiness", Arbol3)
    m.put(analyzer["Caracteristica"], "danceability", Arbol4)
    m.put(analyzer["Caracteristica"], "Valence", Arbol5)
    m.put(analyzer["Caracteristica"], "Loudness", Arbol6)
    m.put(analyzer["Caracteristica"], "Tempo", Arbol7)
    m.put(analyzer["Caracteristica"], "Acousticness", Arbol8)
    m.put(analyzer["Caracteristica"], "Energy", Arbol9)

def AppCaracteristica(analyzer, cancion):

    tabla = analyzer["Caracteristica"]
    Instrumentalness = cancion["Instrumentalness"]
    liveness = cancion["liveness"]
    speechiness = cancion["speechiness"]
    danceability = cancion["danceability"]
    Valence = cancion["Valence"]
    Loudness = cancion["Loudness"]
    Tempo = cancion["Tempo"]
    Acousticness = cancion["Acousticness"]
    Energy = cancion["Energy"]

    Entry1 = m.get(tabla, "Instrumentalness")
    Arbol1 = me.getValue(Entry1)

    contiene = om.contains(Arbol1, Instrumentalness)
    if contiene:
        Entry1 = om.get(Arbol1, Instrumentalness)
        Lista = me.getValue(Entry1)
        lt.addLast(Lista, cancion)
    else:
        Lista = lt.newList()
        lt.addLast(Lista, cancion)

    om.put(Arbol1, Instrumentalness, Lista)
    return Arbol
    

#req 1

#def addautor()
# ==============================
# Funciones de Comparacion
# ==============================

def compareIds(id1, id2):
    """
    Compara dos crimenes
    """
    if (id1 == id2):
        return 0
    elif id1 > id2:
        return 1
    else:
        return -1

def compareDates(date1, date2):
    """
    Compara dos fechas
    """
    if (date1 == date2):
        return 0
    elif (date1 > date2):
        return 1
    else:
        return -1