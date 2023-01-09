import random
def generar():
    legiones = ['FL', 'TF', 'TK', 'CT', 'FN', 'FO']
    stroomtroper=[]
    for i in range(2000):
        numeros= str(random.randint(100,999))
        batallon= random.choice(legiones)
        soldado= f"{batallon}-{numeros}"
        stroomtroper.append(soldado)
        
    soldado={}
    for trooper in stroomtroper:
        numeros=trooper[-3:]
        if numeros not in soldado:
            soldado[numeros]=[]
        soldado[numeros].append(trooper)
    soldado_legio={}
    for trooper in stroomtroper:
        legion=stroomtroper[:2]
        if legion not in soldado_legio:
            soldado_legio[legion]=[]
        soldado_legio[legion].append(trooper)

