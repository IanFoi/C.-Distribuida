def k_merge():
    return []

def cuadricula(arr,cantidad_nodos):
    #cuadricula = [[]] * cantidad_nodos NO es correcto
    cuadricula =  [[] for _ in range(cantidad_nodos)]
    '''Implementar'''

    return cuadricula


def busqueda_binaria(arr,elemento):
    """
    Algoritmo secuencial de busqueda binaria, recibe un arreglo ordenado y un elemento a buscar, regresa True si el elemento se encuentra en el arreglo, False en caso contrario.
    """

    low = 0
    high = len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == elemento:
            return True
        elif arr[mid] < elemento:
            low = mid + 1
        else:
            high = mid - 1
    return False






'''Pruebas locales 
ar1 = [1,2,3,4,5] 
n_c_1 = 5
c1 =  cuadricula(ar1,n_c_1)


ar2= [1,2,3,4]
n_c_2 = 5
c2 =  cuadricula(ar2,n_c_2)

ar3= [1,2,3,4]
n_c_3 = 8
c3 = cuadricula(ar3,n_c_3)


ar4= [1,2,3,4,5,6,7,8]
n_c4 = 4
c4 =  cuadricula(ar4,n_c4)



ar5= [1,2,3,4,5,6,7,8,9,10,11,12,13]
n_c5 = 5
c5 =  cuadricula(ar5,n_c5)

'''
