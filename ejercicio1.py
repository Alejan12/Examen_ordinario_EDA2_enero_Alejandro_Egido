class Stormtrooper:
    def __init__(self,nombre,rango):
        self.nombre=nombre
        self.rango=rango
    def __str__(self):
        return "El stormtrooper {} se ha creado con exito".format(self.nombre)
class Datos(Stormtrooper):
    def __init__(self, nombre, rango,codigo,coherente,siglo,escuadra,trooper):
        super().__init__(nombre, rango)
        self.codigo=codigo
        self.coehrente=coherente
        self.siglo=siglo
        self.escuadra=escuadra
        self.trooper=trooper




soldado1=Datos("Pedro","soldado","TK",8,6,5,4)
soldado2=Datos("Jorge","cabo","FL",5,4,7,9)
soldado3=Datos("Ruben","Capitan","RM",1,7,4,5)
batallon=[soldado1,soldado2,soldado3]
print(soldado1)
def clasificacion(batallon):
    for miembro in batallon:
        print(type(miembro).__name__,miembro.__dict__)
clasificacion(batallon)


        