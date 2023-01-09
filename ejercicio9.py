from collections import deque
def camino_corto(grafo, inicio, fin):
    distancias = {vert: float("inf") for vert in grafo}
    distancias[inicio] = 0
    p_ver= {
        vert: None for vert in grafo
    }

    vertices = list(grafo.keys())

    while vertices:

        c_ver = min(
            vertices, key=lambda vertex: distancias[vertex])

    
        if c_ver == fin:
            path, c_ver = deque(), fin
            while c_ver is not None:
                path.appendleft(c_ver)
                c_ver = p_ver[c_ver]
                return path
            
    vertices.remove(c_ver)
    for vecino, distance in grafo[c_ver]["connections"].items():
        alternate_route = distancias[c_ver] + distance
        if alternate_route < distancias[vecino]:
            distancias[vecino] = alternate_route
            p_ver[vecino] = c_ver
grafo={}
print("El camino mas corto entre Tatooine hasta Dagobah es {}".format(camino_corto(grafo,"Tatooine","Dagobah")))
print("El camino mas corto entre Alderaan hasta Endor es {}".format(camino_corto(grafo,"Alderaan","Endor")))
"El camino mas corto entre Holth hasta Tatooine es {}".format(camino_corto(grafo,"Holth","Tatooine")
