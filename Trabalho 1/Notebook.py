from Computador import Computador

class Notebook(Computador):
    def __init__(self, modelo=None, cor=None, preco=None, tempoDeBateria=None):
        super().__init__(modelo, cor, preco)
        self.__tempoDeBateria = tempoDeBateria

    def getInformacoes(self):  
        return super().getInformacoes() + f"\nTempo de Bateria: {self.__tempoDeBateria}h"

    def cadastrar(self, modelo, cor, preco, tempoDeBateria):
        self.modelo = modelo
        self.cor = cor
        self.preco = preco
        self.__tempoDeBateria = tempoDeBateria