def mochila(precios,pesos,volumen):
    if len(precios)==0 or volumen==0:
        return 0
    if pesos[-1]>volumen:
        return mochila(precios[:-1, pesos[:-1],volumen])
    
    return max(precios[-1])




precio=[103, 60, 70, 5, 15] 
pesos=[12, 23, 11, 15, 7]
peso_maximo = 100
