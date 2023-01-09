def mochila(precios,pesos,volumen):
    if len(precios)==0 or volumen==0:
        return 0
    if pesos[-1]>volumen:
        return mochila(precios[:-1, pesos[:-1],volumen])
    
    return max(precios[-1] + mochila(precios[:-1],pesos[:-1],volumen - pesos[-1]),mochila(precios[:-1],pesos[:-1],volumen))

precio=[103, 60, 70, 5, 15] 
pesos=[12, 23, 11, 15, 7]
peso_maximo = 100
print("El numero máximo de objetos que puede llevar en la mochila sin que exceda el máximo son: {} objetos".format(mochila(precio,pesos,peso_maximo)))
