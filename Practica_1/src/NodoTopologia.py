import simpy
import time
from Nodo import *
from Canales.CanalBroadcast import *

# La unidad de tiempo
TICK = 1


class NodoTopologia(Nodo):
    ''' Implementa la interfaz de Nodo para el algoritmo de Broadcast.'''

    def __init__(self, id_nodo, vecinos, canal_entrada, canal_salida, mensaje=None):
	#Tú código aquí
        self.id_nodo = id_nodo
        self.vecinos = vecinos
        self.canal_entrada = canal_entrada
        self.canal_salida = canal_salida
        self.proc_conocidos= {id_nodo}
        self.canales_conocidos = set()
        for vecino in vecinos:
            self.canales_conocidos.add(tuple(sorted([self.id_nodo, vecino])))

    def topologia(self, env):
        # Tú código aquí
        return
