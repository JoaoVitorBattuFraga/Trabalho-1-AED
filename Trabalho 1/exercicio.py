from abc import ABCMeta, abstractmethod

# Computador:
class Computador(metaclass=ABCMeta):
    def __init__(self, modelo, cor, preco):
        self.modelo = modelo
        self.cor = cor
        self.preco = preco
    
    def getInformacoes(self):
        return f"Modelo: {self.modelo}\nCor: {self.cor}\nPreço: {self.preco}"

    @abstractmethod
    def cadastrar(self):
        pass

# Desktop:
class Desktop(Computador):
    def __init__(self, modelo=None, cor=None, preco=None, potenciaDaFonte=None):
        super().__init__(modelo, cor, preco)
        self._potenciaDaFonte = potenciaDaFonte

    def getInformacoes(self):
        return super().getInformacoes() + f"\nPotência da Fonte: {self._potenciaDaFonte}w"

    def cadastrar(self, modelo, cor, preco, potenciaDaFonte):
        self.modelo = modelo
        self.cor = cor
        self. preco = preco
        self._potenciaDaFonte = potenciaDaFonte

# Notebook:
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

# Main:
from Desktop import Desktop
from Notebook import Notebook

d1 = Desktop("ThinkCentre", "preto", 3900, 500)
print(d1.getInformacoes())

print("----------------")

d2 = Desktop()
d2.cadastrar("Dell", "cinza", 4900, 1000)
print(d2.getInformacoes())

print("----------------")

n1 = Notebook()
n1.cadastrar("Samsung", "cinza", 5900, 8)
print(n1.getInformacoes())

