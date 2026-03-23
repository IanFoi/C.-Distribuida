import simpy
from Nodo import *
from Canales.CanalBroadcast import *
from Auxiliares import *
#from NodoGenerador import NodoGenerador


TICK = 1
class NodoConvergcast(Nodo):
    '''Implementa la interfaz de Nodo para el algoritmo de convergcast.'''
    def __init__(self, id_nodo,vecinos,valor, canal_entrada, canal_salida, mensaje=None):
            self.id_nodo = id_nodo
            self.padre = None
            self.vecinos = vecinos
            self.canal_entrada = canal_entrada
            self.canal_salida = canal_salida
            self.mensaje = mensaje
            self.value =  valor #self.id_nodo #Como ejemplo para los test diremos que los valores recolectados seran los ids , no usamos un conjunto pues no sabemos que se vaya ahacer (la funcion f)
            #self.val_set = [self.value] Situacional
            self.val_set = {self.value}
            self.funcion = None 
            self.valor_final = None

    def toString(self):
        return f"Nodo : {self.id_nodo},valor: {self.value}, valores: {self.val_set}"

    def convergecast(self,env,f):

#       '''Implementar'''
        if self.id_nodo == 0 :
            self.padre = self.id_nodo 
            self.funcion =  f 
            yield env.timeout (TICK)
            mensaje =  ("INIT",self.id_nodo,set()) 
            self.canal_salida.envia(mensaje, self.vecinos)
        
        while True : 
            msg =  yield self.canal_entrada.get()
            #"INIT",id,set()
            
            #(estado, emisor (padre),informacion)
            if msg[0] == "INIT" :
                self.padre =  msg[1]
                if self.vecinos : #si hay hijos
                    msg_ = ("INIT",self.id_nodo,set())
                    self.canal_salida.envia(msg_, self.vecinos)
                
                else: #Comienzamos
                    msg_back =  ("BACK",self.id_nodo,self.val_set) 
                    self.canal_salida.envia(msg_back,[self.padre])
            else: #Back del convergecast
                
                self.val_set.update(msg[2]) 

                if self.padre != self.id_nodo :
                    msg_back =  ("BACK",self.id_nodo,self.val_set) 
                    self.canal_salida.envia(msg_back,[self.padre])
                
                else: #es la raiz 
                    self.value = f(self.val_set)


adyacencias_arbol_1 = [[1,2],[3,4,5],[6],[],[7],[],[],[8,9],[],[]]

Tiempo =  15

env  = simpy.Environment()
bc_pipe = CanalBroadcast(env)
grafica = []

for i in range(0,len(adyacencias_arbol_1)):
        grafica.append(NodoConvergcast(i,adyacencias_arbol_1[i],i,bc_pipe.crea_canal_de_entrada(),bc_pipe))


f = lambda estructura: sum(estructura) 

for nodo in grafica :
    env.process(nodo.convergecast(env,f))


env.run(until = Tiempo)


for nodo in grafica :
    print(nodo.toString())






