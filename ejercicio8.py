import heapq

def crear_arbol_huffman(frecuencias):
   
    arbol = [(freq, símbolo, None, None) for símbolo, freq in frecuencias.items()]
    heapq.heapify(arbol)
    while len(arbol) > 1:
        izquierda, derecha = heapq.heappop(arbol), heapq.heappop(arbol)
        nodo = (izquierda[0] + derecha[0], None, izquierda, derecha)
        heapq.heappush(arbol, nodo)
    return arbol[0]

def crear_tabla_codificación(arbol, prefixo=""):
    if arbol[1] is not None:
        return {arbol[1]: prefixo}
    tabla_izquierda = crear_tabla_codificación(arbol[2], prefixo + "0")
    tabla_derecha = crear_tabla_codificación(arbol[3], prefixo + "1")
    tabla_izquierda.update(tabla_derecha)
    return tabla_izquierda

def comprimir(mensaje, tabla_codificación):
    mensaje_comprimido = ""
    for símbolo in mensaje:
        mensaje_comprimido += tabla_codificación[símbolo]
    return mensaje_comprimido

def descomprimir(mensaje_comprimido, arbol):
    mensaje = ""
    nodo = arbol
    for bit in mensaje_comprimido:
        if bit == "0":
            nodo = nodo[2]
        else:
            nodo = nodo[3]
        if nodo[1] is not None:
            mensaje += nodo[1]
            nodo = arbol
    return mensaje
frecuencias={"A":0.2,"F":0.17,"1":0.13,"3":0.21,"0":0.05,"M":0.09,"T":0.15}
