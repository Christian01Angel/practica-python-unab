"""Desarrollar una clase que represente un punto en el plano y tenga los siguientes métodos: inicialiozar los
valores de x e y que llegan como parametros, imprimir en que cuadrante se encuentra dicho punto"""


class Punto:
    def __init__(self, x, y):
        self.puntoX = x
        self.puntoY = y

    def imprimir(self):
        print(f'El punto Q({self.puntoX}, {self.puntoY}) tiene valor de x: {self.puntoX} y valor de y: {self.puntoY}')

    def cuadrante(self):
        if self.puntoX >0 and self.puntoY>0:
            print('Estas en el primer cuadrante')
        elif self.puntoX<0 and self.puntoY>0:
            print('Estas en el segundo cuadrante')
        elif self.puntoX<0 and self.puntoY <0:
            print('Estas en el tercer cuadrante')
        elif self.puntoX>0 and self.puntoY<0:
            print('Estas en el cuarto cuadrante')
        elif self.puntoX>0 and self.puntoY == 0:
            print('Estas sobre el eje de las X positivas entre el primer y el cuarto cuadrante')
        elif self.puntoX == 0 and self.puntoY > 0:
            print('Estas sobre el eje de las Y positivas entre el primer y el segundo cuadrante')
        elif self.puntoX <0 and self.puntoY == 0:
            print('Estas sobre el eje de las X negativas entre el segundo y el tercer cuadrante')
        elif self.puntoX == 0 and self.puntoY < 0:
            print('Estas sobre el eje de las Y negativas entre el tercer y el cuarto cuadrante')
        else:
            print('Valores desconocidos')


#main
puntoA = Punto(5, 4)
puntoA.imprimir()
puntoA.cuadrante()
puntoB = Punto(-2, 3)
puntoB.imprimir()
puntoB.cuadrante()
puntoC = Punto(-2, -3)
puntoC.imprimir()
puntoC.cuadrante()
puntoD = Punto(2, -3)
puntoD.imprimir()
puntoD.cuadrante()
puntoE = Punto(2, 0)
puntoE.imprimir()
puntoE.cuadrante()
puntoF = Punto(0, 3)
puntoF.imprimir()
puntoF.cuadrante()
puntoG = Punto(-2, 0)
puntoG.imprimir()
puntoG.cuadrante()
puntoH = Punto(0, -3)
puntoH.imprimir()
puntoH.cuadrante()

