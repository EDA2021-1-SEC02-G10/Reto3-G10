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
    analyzer["genreHash"] = m.newMap()

    analyzer["Fechas"] = om.newMap(omaptype='RBT',
                                      comparefunction=compareHour)
    
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
    instrumentalness = float(cancion["instrumentalness"])
    liveness = float(cancion["liveness"])
    speechiness = float(cancion["speechiness"])
    danceability = float(cancion["danceability"])
    valence = float(cancion["valence"])
    loudness = float(cancion["loudness"])
    tempo = float(cancion["tempo"])
    acousticness = float(cancion["acousticness"])
    energy = float(cancion["energy"])

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
    
    artistas = m.size(tabla_de_hash)
    return "Total de autores:", artistas, "Total de reproducciones:", total_de_eventos
    
#req 2 

def encontrar_pistas_unicas_req_2(analyzer,minimo_energy, maximo_energy,minimo_dance,maximo_dance,variable,variable_2):
    energy = m.get(analyzer["Caracteristica"], variable)
    danceability = m.get(analyzer["Caracteristica"], variable_2)

    arbol_energy = me.getValue(energy)
    arbol_danceability = me.getValue(danceability)    
    rango_energy = om.values(arbol_energy,minimo_energy,maximo_energy)    
    rango_danceability = om.values(arbol_danceability,minimo_dance,maximo_dance)

    iterador_energy = it.newIterator(rango_energy)
    iterador_danceability = it.newIterator(rango_danceability)

    tabla_de_hash= m.newMap()
    N_track = 0
    while it.hasNext(iterador_energy) or it.hasNext(iterador_danceability):
        elemento_energy = it.next(iterador_energy)
        elemento_danceability = it.next(iterador_danceability)

        iterador_1 = it.newIterator(elemento_energy)
        iterador_2 = it.newIterator(elemento_danceability)
        
        while it.hasNext(iterador_1) and it.hasNext(iterador_2):
            elemento_energy_1 = it.next(iterador_1)
            elemento_danceability_1 = it.next(iterador_2)
            if m.contains(tabla_de_hash, elemento_energy_1["track_id"]) == False and m.contains(tabla_de_hash, elemento_danceability_1["track_id"]) == False and float(elemento_energy_1[variable_2]) > minimo_dance and float(elemento_energy_1[variable_2]) < maximo_dance and float(elemento_danceability_1[variable]) > minimo_energy and float(elemento_danceability_1[variable]) < maximo_energy:
                m.put(tabla_de_hash,elemento_danceability_1["track_id"], elemento_danceability_1) 
                m.put(tabla_de_hash, elemento_energy_1["track_id"], elemento_energy_1)
                N_track += 1
    lista = m.valueSet(tabla_de_hash)
    iterador_3 = it.newIterator(lista)  
    j = 1
    lista_final = lt.newList()
    while  j <= 5:
        elemento = it.next(iterador_3)
        dato = "El Track ID es", elemento["track_id"], "con un Energy de ", elemento["energy"], "y un Danceability de ", elemento["danceability"]
        lt.addLast(lista_final,dato)
        j+=1
    return ("Número unico de Track:", N_track, "Cinco pistas en orden aleatorio:", lista_final)

# req 3

def encontrar_pistas_unicas_req_3(analyzer,minimo_instrumentalness, maximo_instrumentalness,minimo_tempo,maximo_tempo,variable,variable_2):
    instrumentalness = m.get(analyzer["Caracteristica"], variable)
    tempo = m.get(analyzer["Caracteristica"], variable_2)

    arbol_instrumentalness = me.getValue(instrumentalness)  
    arbol_tempo = me.getValue(tempo)             
    rango_instrumentalness = om.values(arbol_instrumentalness,minimo_instrumentalness,maximo_instrumentalness)    
    rango_tempo = om.values(arbol_tempo,minimo_tempo,maximo_tempo)

    iterador_instrumentalness = it.newIterator(rango_instrumentalness)
    iterador_tempo = it.newIterator(rango_tempo)

    tabla_de_hash= m.newMap()
    N_track = 0
    while it.hasNext(iterador_instrumentalness) or it.hasNext(iterador_tempo):
        elemento_instrumentalness = it.next(iterador_instrumentalness)
        elemento_tempo = it.next(iterador_tempo)

        iterador_1 = it.newIterator(elemento_instrumentalness)
        iterador_2 = it.newIterator(elemento_tempo)
        
        while it.hasNext(iterador_1) and it.hasNext(iterador_2):
            elemento_instrumentalness_1 = it.next(iterador_1)
            elemento_tempoy_1 = it.next(iterador_2)
            if m.contains(tabla_de_hash, elemento_instrumentalness_1["track_id"]) == False and m.contains(tabla_de_hash, elemento_tempo_1["track_id"]) == False and float(elemento_instrumentalness_1[variable_2]) > minimo_tempo and float(elemento_energy_1[variable_2]) < maximo_tempo and float(elemento_tempo_1[variable]) > minimo_instrumentalness and float(elemento_tempo_1[variable]) < maximo_instrumentalness:
                m.put(tabla_de_hash,elemento_tempo_1["track_id"], elemento_tempo_1) 
                m.put(tabla_de_hash, elemento_instrumentalness_1["track_id"], elemento_instrumentalness_1)
                N_track += 1
    lista = m.valueSet(tabla_de_hash)
    iterador_3 = it.newIterator(lista)  
    j = 1
    lista_final = lt.newList()
    while  j <= 5:
        elemento = it.next(iterador_3)
        dato = "El Track ID es", elemento["track_id"], "con un Instrumentalness de ", elemento["instrumentalness"], "y un Tempo de ", elemento["Tempo"]
        lt.addLast(lista_final,dato)
        j+=1
    return ("Número unico de Track:", N_track, "Cinco pistas en orden aleatorio:", lista_final)
    
# req 4
def crearHastGenre(analyzer):
    tabla_de_hash = analyzer["genreHash"]
    m.put(tabla_de_hash,"Reggae",(60,90))
    m.put(tabla_de_hash,"Down_tempo",(70,100))
    m.put(tabla_de_hash,"Chill_out",(90,120))
    m.put(tabla_de_hash,"Hip_hop",(85,115))
    m.put(tabla_de_hash,"Jazz_and_funk",(120,125))
    m.put(tabla_de_hash,"Pop",(100,130))
    m.put(tabla_de_hash,"R&B",(60,80))
    m.put(tabla_de_hash,"Rock",(110,140))
    m.put(tabla_de_hash,"Metal",(100,160))
    return 

def nuevo_genero(analizer,minValue,nombre,maxValue):
    m.put(analizer["genreHash"],nombre,(minValue,maxValue))

def findTuple(analyzer,genero):
    tuplx = me.getValue(m.get(analyzer["genreHash"],genero))
    return tuplx

def encontrar_generos_musicales(analyzer,genero,option,nombre,minValue,maxValue):
    if option == 1:
        nuevo_genero(analyzer,minValue,nombre,maxValue)
        intervalo = findTuple(analyzer,genero)
    caracteristica = m.get(analyzer["Caracteristica"], "tempo")
    arbol = me.getValue(caracteristica)
    intervalo = findTuple(analyzer,genero)
    rango = om.values(arbol,intervalo[0],intervalo[1])
    i = 0
    eventos = 0
    iterador = it.newIterator(rango)
    tabla_de_hash = m.newMap()
    while it.hasNext(iterador):
        elemento = it.next(iterador)
        tamanio = lt.size(elemento)
        eventos += tamanio
        iterador_1 = it.newIterator(elemento)
        while it.hasNext(iterador_1):
            elemento_1 = it.next(iterador_1)
            if not m.contains(tabla_de_hash, elemento_1["artist_id"]):
                m.put(tabla_de_hash,elemento_1["artist_id"],elemento_1)
                i += 1
    
    lista = m.valueSet(tabla_de_hash)
    iterador_3 = it.newIterator(lista)
    j = 0
    lista_final = lt.newList()
    while it.hasNext(iterador_3) and j<=10:
        elemento_2 = it.next(iterador_3)
        lt.addLast(lista_final,elemento_2)
        j += 1
    return ("Número de eventos: ", eventos,"Número de Artistas : ", i, "Artistas unicos: ", lista_final)

# req 5
def Appfechas (analyzer, fecha):
    key = fecha["created_at"]
    key = datetime.datetime.strptime(key, '%Y-%m-%d %H:%M:%S')
    key = key.time()
    Arbol  = analyzer["Fechas"]
    verificador = om.contains(Arbol, key)
    
    if verificador:
        Entry = om.get(Arbol, key)
        Lista = me.getValue(Entry)
    else: 
        Lista = lt.newList()
    lt.addLast(Lista, fecha)
    om.put(Arbol, key, Lista)
    
    
def genero_mas_escuchado(analyzer, minimo_dia, maximo_dia):
    arbol = me.getValue(analyzer["Fechas"])
    rango = om.values(arbol, minimo, maximo)
    
    return analyzer["Fechas"]

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

def compareHour (hour1,hour2):
    if (hour1.hour == hour2.hour) and (hour1.minute == hour2.minute):
        return 0
    elif (hour1.hour > hour2.hour):
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