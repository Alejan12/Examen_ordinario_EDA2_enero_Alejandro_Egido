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
    for vecino, distancia in grafo[c_ver]["connections"].items():
        otra_ruta = distancias[c_ver] + distancia
        if otra_ruta < distancias[vecino]:
            distancias[vecino] = otra_ruta
            p_ver[vecino] = c_ver
grafo={
    "Alderaan": ["Endor", "Hoth", "Tatooine", "Yavin IV"],
    "Endor": ["Alderaan", "Dagobah", "Hoth", "Kamino", "Kashyyyk"],
    "Dagobah": ["Endor", "Mustafar", "Kashyyyk"],
    "Hoth": ["Alderaan", "Endor", "Naboo", "Yavin IV"],
    "Tatooine": ["Alderaan", "Naboo", "Scarif", "Geonosis", "Sullust"],
    "Kamino": ["Endor", "Mustafar", "Onderon"],
    "Naboo": ["Hoth", "Tatooine", "Scarif", "Coruscant", "Onderon"],
    "Mustafar": ["Dagobah", "Kamino", "Geonosis"],
    "Scarif": ["Tatooine", "Naboo", "Utapau"],
    "Bespin": ["Coruscant", "Utapau", "Sullust"],
    "Coruscant": ["Naboo", "Bespin"],
    "Geonosis": ["Tatooine", "Mustafar"],
    "Kashyyyk": ["Endor", "Dagobah"],
    "Utapau": ["Scarif", "Bespin"],
    "Onderon": ["Naboo", "Kamino"],
    "Yavin IV": ["Alderaan", "Hoth"],
    "Sullust": ["Bespin", "Tatooine"]
}

print("El camino mas corto entre Tatooine hasta Dagobah es {}".format(camino_corto(grafo,"Tatooine","Dagobah")))
print("El camino mas corto entre Alderaan hasta Endor es {}".format(camino_corto(grafo,"Alderaan","Endor")))
print("El camino mas corto entre Holth hasta Tatooine es {}".format(camino_corto(grafo,"Holth","Tatooine")))


