# Crie um tipo abstrato de dado (TAD) para manipular números complexos na linguagem Python.

# O método deve:

# - calcular três números complexos;
# - realizar todas as operações básicas;
# - e imprimir as propriedades real e img dos números. 

class Complex:
  def __init__(self, numOne, numTwo):
    self.numOne = numOne
    self.numTwo = numTwo

  def numComplexo(self):
    numComplex = complex(self.numOne, self.numTwo)
    return numComplex

objeto = Complex(10, 2)
numeroComplexo = objeto.numComplexo()

objeto1 = Complex(5, 3)
numeroComplexo1 = objeto1.numComplexo()

objeto2 = Complex(23, 4)
numeroComplexo2 = objeto2.numComplexo()

print("Números complexos:", numeroComplexo, numeroComplexo1, numeroComplexo2)
print("")

print("Operações entre o número 1 e 2")
print("")
print("Soma:", numeroComplexo + numeroComplexo1)
print("Subtração:", numeroComplexo - numeroComplexo1)
print("Multiplicação:", numeroComplexo - numeroComplexo1)
print("Divisão:", numeroComplexo / numeroComplexo1)
print("")

print("Parte real e imaginária do número " + str(numeroComplexo) + " : " + str(numeroComplexo.real) + ", " + str(numeroComplexo.imag))
print("Parte real e imaginária do número " + str(numeroComplexo1) + " : " + str(numeroComplexo1.real) + ", " + str(numeroComplexo1.imag))
print("Parte real e imaginária do número " + str(numeroComplexo2) + " : " + str(numeroComplexo2.real) + ", " + str(numeroComplexo2.imag))