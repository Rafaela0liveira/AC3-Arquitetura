import abc
from unittest import TestCase, main

class Calculadora (object):

    def Calcular(self, valor1, valor2, operador):
        opFab = OperacaoFabrica()
        operacao = opFab.criar(operador)
        if(operacao == None):
            return 0 
        else:
            resultado = operacao.executar(valor1, valor2)
            return resultado
class OperacaoFabrica(object):
    def criar(self, operador):
        if(operador == 'soma'):
            return Soma()
        elif(operador == 'subtracao'):
            return Subtracao()
        elif (operador == 'divisao'):
            return Divisao()
        elif(operador == 'multiplicacao'):
            return Multiplicacao()

class Operacao(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def executar(self, valor1, valor2):
        pass
class Soma(Operacao):
    def executar(self, valor1, valor2):
        resultado = valor1 + valor2
        return resultado

class Multiplicacao(Operacao):
    def executar(self, valor1, valor2):
        resultado = valor1 * valor2
        return resultado

class Subtracao(Operacao):
    def executar(self, valor1, valor2):
        resultado = valor1 - valor2
        return resultado

class Divisao(Operacao):
    def executar(self, valor1, valor2):
        resultado = valor1 / valor2
        return resultado

class Testes(TestCase):
    def test_soma(self):
        calc = Calculadora()
        result = calc.Calcular(2, 3, 'soma')
        self.assertEqual(result, 5)

    def test_multiplicar(self):
        calc1 = Calculadora()
        self.assertEqual(calc1.Calcular(3,7, 'multiplicacao'), 21)

    def test_divisao(self):
        calc2 = Calculadora()
        self.assertEqual(calc2.Calcular(16,2, 'divisao'), 8)
    
    def test_subtracao(self):
        calc3 = Calculadora()
        self.assertEqual(calc3.Calcular(14,4, 'subtracao'), 10)
    



C = Calculadora()
x = C.Calcular(16,2, 'divisao')
print(x)

if __name__ == '__main__':
    main()