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
from DISClib.DataStructures import listiterator as it 
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
                                      comparefunction=compareCaracteristicas)
    Arbol2 = om.newMap(omaptype='RBT',
                                      comparefunction=compareCaracteristicas)
    Arbol3 = om.newMap(omaptype='RBT',
                                      comparefunction=compareCaracteristicas)
    Arbol4 = om.newMap(omaptype='RBT',
                                      comparefunction=compareCaracteristicas)
    Arbol5 = om.newMap(omaptype='RBT',
                                      comparefunction=compareCaracteristicas)
    Arbol6 = om.newMap(omaptype='RBT',
                                      comparefunction=compareCaracteristicas)
    Arbol7 = om.newMap(omaptype='RBT',
                                      comparefunction=compareCaracteristicas)
    Arbol8 = om.newMap(omaptype='RBT',
                                      comparefunction=compareCaracteristicas)
    Arbol9 = om.newMap(omaptype='RBT',
                                      comparefunction=compareCaracteristicas)

    m.put(analyzer["Caracteristica"], "instrumentalness", Arbol1)
    m.put(analyzer["Caracteristica"], "liveness", Arbol2)
    m.put(analyzer["Caracteristica"], "speechiness", Arbol3)
    m.put(analyzer["Caracteristica"], "danceability", Arbol4)
    m.put(analyzer["Caracteristica"], "valence", Arbol5)
    m.put(analyzer["Caracteristica"], "loudness", Arbol6)
    m.put(analyzer["Caracteristica"], "tempo", Arbol7)
    m.put(analyzer["Caracteristica"], "acousticness", Arbol8)
    m.put(analyzer["Caracteristica"], "energy", Arbol9)

def AppCaracteristica(analyzer, cancion):

    tabla = analyzer["Caracteristica"]
    instrumentalness = cancion["instrumentalness"]
    liveness = cancion["liveness"]
    speechiness = cancion["speechiness"]
    danceability = cancion["danceability"]
    valence = cancion["valence"]
    loudness = cancion["loudness"]
    tempo = cancion["tempo"]
    acousticness = cancion["acousticness"]
    energy = cancion["energy"]

    #arbol1
    Entry1 = m.get(tabla, "instrumentalness")
    Arbol1 = me.getValue(Entry1)

    contiene = om.contains(Arbol1, instrumentalness)
    if contiene:
        Entry1 = om.get(Arbol1, instrumentalness)
        Lista = me.getValue(Entry1)
        lt.addLast(Lista, cancion)
    else:
        Lista = lt.newList()
        lt.addLast(Lista, cancion)

    om.put(Arbol1, instrumentalness, Lista)

    #arbol2
    Entry2 = m.get(tabla, "liveness")
    Arbol2 = me.getValue(Entry2)

    contiene = om.contains(Arbol2, liveness)
    if contiene:
        Entry2 = om.get(Arbol2, liveness)
        Lista = me.getValue(Entry2)
        lt.addLast(Lista, cancion)
    else:
        Lista = lt.newList()
        lt.addLast(Lista, cancion)

    om.put(Arbol2, liveness, Lista)

    #arbol3
    Entry3 = m.get(tabla, "speechiness")
    Arbol3 = me.getValue(Entry3)

    contiene = om.contains(Arbol3, speechiness)
    if contiene:
        Entry3 = om.get(Arbol3, speechiness)
        Lista = me.getValue(Entry3)
        lt.addLast(Lista, cancion)
    else:
        Lista = lt.newList()
        lt.addLast(Lista, cancion)

    om.put(Arbol3, speechiness, Lista)

    #arbol4
    Entry4 = m.get(tabla, "danceability")
    Arbol4 = me.getValue(Entry4)

    contiene = om.contains(Arbol4, danceability)
    if contiene:
        Entry4 = om.get(Arbol4, danceability)
        Lista = me.getValue(Entry4)
        lt.addLast(Lista, cancion)
    else:
        Lista = lt.newList()
        lt.addLast(Lista, cancion)

    om.put(Arbol4, danceability, Lista)

    #arbol5
    Entry5 = m.get(tabla, "valence")
    Arbol5 = me.getValue(Entry5)

    contiene = om.contains(Arbol5, valence)
    if contiene:
        Entry5 = om.get(Arbol5, valence)
        Lista = me.getValue(Entry5)
        lt.addLast(Lista, cancion)
    else:
        Lista = lt.newList()
        lt.addLast(Lista, cancion)

    om.put(Arbol5, valence, Lista)

    #arbol6
    Entry6 = m.get(tabla, "loudness")
    Arbol6 = me.getValue(Entry6)

    contiene = om.contains(Arbol6, loudness)
    if contiene:
        Entry6 = om.get(Arbol6, loudness)
        Lista = me.getValue(Entry6)
        lt.addLast(Lista, cancion)
    else:
        Lista = lt.newList()
        lt.addLast(Lista, cancion)

    om.put(Arbol6, loudness, Lista)

    #arbol7
    Entry7 = m.get(tabla, "tempo")
    Arbol7 = me.getValue(Entry7)

    contiene = om.contains(Arbol7, tempo)
    if contiene:
        Entry7 = om.get(Arbol7, tempo)
        Lista = me.getValue(Entry7)
        lt.addLast(Lista, cancion)
    else:
        Lista = lt.newList()
        lt.addLast(Lista, cancion)

    om.put(Arbol7, tempo, Lista)

    #arbol8
    Entry8 = m.get(tabla, "acousticness")
    Arbol8 = me.getValue(Entry8)

    contiene = om.contains(Arbol8, acousticness)
    if contiene:
        Entry8 = om.get(Arbol8, acousticness)
        Lista = me.getValue(Entry8)
        lt.addLast(Lista, cancion)
    else:
        Lista = lt.newList()
        lt.addLast(Lista, cancion)

    om.put(Arbol8, acousticness, Lista)

    #arbol9
    Entry9 = m.get(tabla, "energy")
    Arbol9 = me.getValue(Entry9)

    contiene = om.contains(Arbol9, energy)
    if contiene:
        Entry9 = om.get(Arbol9, energy)
        Lista = me.getValue(Entry9)
        lt.addLast(Lista, cancion)
    else:
        Lista = lt.newList()
        lt.addLast(Lista, cancion)

    om.put(Arbol9, energy, Lista)

#req 1

def clasificar_caracteristicas(analyzer, caracteristica, minimo, maximo):
    Caracteristica = m.get(analyzer["Caracteristica"], caracteristica)
    arbol = me.getValue(Caracteristica)
    rango = om.values(arbol, minimo, maximo)
    iterador = it.newIterator(rango)
    total_de_eventos = 0
    tabla_de_hash = m.newMap()
    while it.hasNext(iterador):
        elemento = it.next(iterador)
        tamanio = lt.size(elemento)
        total_de_eventos += tamanio
        iterador1 = it.newIterator(elemento)
        while it.hasNext(iterador1):
            elemento1 = it.next(iterador1)
            if not m.contains(tabla_de_hash, elemento1["artist_id"]):
                m.put(tabla_de_hash, elemento1["artist_id"], 1)
    rta = lt.newList()
    artistas = m.size(tabla_de_hash)
    lt.addLast(rta, total_de_eventos)
    lt.addLast(rta, artistas)
    return rta
    
#req 2
def encontrar_festejar(analyzer,minimo_energy, maximo_energy,minimo_dance,maximo_dance):
    energy = m.get(analyzer["Caracteristica"], "energy")
    danceability = m.get(analyzer["Caracteristica"], "danceability")
    rango_energy = om.values(energy, minimo_energy, maximo_energy)
    rango_danceability = om.values(danceability, minimo_dance, maximo_dance)
    iterador_energy = it.newIterator(rango_energy)
    interador_danceability = it.newIterator(rango_energy)
    tabla_de_hash = 
    numero_pistas = 0
    while it.hasNext(iterador_energy) and it.hasNext(iterador_danceability):
        elemento_energy = it.next(iterador_energy)
        elemento_iterador_energy = it.next(iterador_iterador_energy)
        iterador_energy_1 = it.newIterator(elemento_energy)
        iterador_energy_2 = it.newIterator(elemento_energy)
        while it.hasNext(iterador_energy_1) and it.hasNext(iterador_danceability_2): #preguntar cupi
            elemento_energy_1 = it.next(iterador_energy_1)
            elemento_iterador_energy_2 = it.next(iterador_iterador_energy_2)
            m.put(tabla_de_hash, elemento_energy_1["reack_id"], 1)
            m.put(tabla_de_hash, elemento_iterador_energy_2["track_id"], 1)
            


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
    Key = me.getKey(date2)
    if (date1 == Key):
        return 0
    elif (date1 > Key):
        return 1
    else:
        return -1

def compareCaracteristicas(date1:float, date2:float):
    
    if (date1 == date2):
        return 0
    elif (date1 > date2):
        return 1
    else:
        return -1