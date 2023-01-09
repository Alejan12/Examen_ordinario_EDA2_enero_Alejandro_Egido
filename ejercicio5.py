objetos=["pistola","granada","pinganillo","sable de luz","pipas"]
def sacar_objetos(objetos):
    for objeto in range(len(objetos)):
        if objetos[objeto]=="sable de luz":
            print(objetos[:objeto],objetos[objeto])
sacar_objetos(objetos)
def determina(objetos):
    for i in range(len(objetos)):
        if objetos[i]=="sable de luz":
            contar=len(objetos[:i]+1 )
            print("El sable de luz esta en la mochila, se ha necesitada sacar {}".format(contar))
determina(objetos)