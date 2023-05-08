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
