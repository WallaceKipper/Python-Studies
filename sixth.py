class Calculadora:
    def __init__(self, num1, num2 ):
        self.a = num1
        self.b = num2
    def soma(self):
        return self.a + self.b

    def sub(self):
        return self.a - self.b

    def mult(self):
        return self.a * self.b

    def div(self):
        return self.a / self.b

# print(soma(4, 6))
# print(soma(6, 8))
# print(sub(23, 6))
# print(sub(6, 4))
# print(mult(4, 6))
# print(div(34, 6))

# calculadora = Calculadora(10,2)
# print(calculadora.a)
# print(calculadora.soma())
# print(calculadora.sub())
# print(calculadora.mult())
# print(calculadora.div())

class Calculadora_2:
    def __init__(self):
        pass
    def soma(self, a, b):
        return a + b

    def sub(self, a, b):
        return a - b

    def mult(self, a, b):
        return a * b

    def div(self, a, b):
        return a / b

# calculadora = Calculadora_2()
# print(calculadora.soma(5, 7))
# print(calculadora.sub(20, 10))
# print(calculadora.mult(5, 6))
# print(calculadora.div(70, 3 ))

class Telev:
    def __init__(self):
        self.lig = False
        self.canal = 5

    def power(self):
        if self.lig:
            self.lig = False
        else:
            self.lig = True

    def aument_canal(self):
        if self.lig:
            self.canal += 1

    def diminu_canal(self):
        if self.lig:
            self.canal -= 1

televisao = Telev()
print("Televisão está ligada: {}".format(televisao.lig))
televisao.power()
print("Televisão está ligada: {}".format(televisao.lig))
televisao.power()
print("Televisão está ligada: {}".format(televisao.lig))
print("Canal: {}".format(televisao.canal))
televisao.aument_canal()
televisao.power()
televisao.aument_canal()
print("Canal: {}".format(televisao.canal))
televisao.diminu_canal()
televisao.diminu_canal()
televisao.diminu_canal()
print("Canal: {}".format(televisao.canal))
