import random
def generar():
    legiones = ['FL', 'TF', 'TK', 'CT', 'FN', 'FO']
    stroomtroper=[]
    for i in range(2000):
        numeros= str(random.randint(100,999))
        batallon= random.choice(legiones)
        soldado= f"{batallon}-{numeros}"
        stroomtroper.append(soldado)
    return stroomtroper

