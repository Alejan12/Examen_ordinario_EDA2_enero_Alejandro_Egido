class Artefactovalioso:
    def __init__(self,nombre,peso,precio,caducidad):
        self.nombre=nombre
        self.peso=peso
        self.precio=precio
        self.caducidad=caducidad
    def __str__(self):
        return "El objeto {} pesa {} con un precio {} y fecha de caducidad {}".format(self.nombre,self.peso,self.precio,self.caducidad)
a=Artefactovalioso("a",5,4,10)
b=Artefactovalioso("b",4,2,1,)
lista=[a,b]
def catalogar(lista):
    for cosa in lista:
        print(type(cosa).__name__,cosa.__dict__) 
catalogar(lista)