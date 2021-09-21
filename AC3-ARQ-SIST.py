import abc
from unittest import TestCase, main


class Calculadora(object):
	
	def calcular(self,valor1,valor2,operador):
		recebeOperador = OperacaoFabrica()
		qualOperacao = recebeOperador.criar(operador)
		resultado = qualOperacao.executar(valor1,valor2)
		return resultado


class OperacaoFabrica(object) :

	def criar(self,operador):
		if operador == "+":
			return Soma()
		elif operador == "-":
			return Subtracao()
		elif operador == "*":
			return Multiplicacao()
		elif operador == "/":
			return Divisao()
			

class Operacao(metaclass=abc.ABCMeta):
	
	@abc.abstractmethod
	def executar(self,valor1,valor2):
		pass


#Soma
class Soma(object):

	def executar(self,valor1,valor2):
		resultado = valor1 + valor2
		return resultado


#Subtração
class Subtracao(object):

	def executar(self,valor1,valor2):
		resultado = valor1 - valor2
		return resultado


#Multiplicação
class Multiplicacao(object):

	def executar(self,valor1,valor2):
		resultado = valor1 * valor2
		return resultado


#Divisão
class Divisao(object):

	def executar(self,valor1,valor2):
		resultado = valor1 / valor2
		return resultado



class TestaOperacoes(TestCase):

	def teste_soma(self):
		calculadora = Calculadora()
		resultado = calculadora.calcular(15,15,"+")
		self.assertEqual(resultado, 30)

	def teste_soma2(self):
		calculadora = Calculadora()
		resultado = calculadora.calcular(200,300,"+")
		self.assertEqual(resultado, 500)

	def teste_soma3(self):
		calculadora = Calculadora()
		resultado = calculadora.calcular(33,33,"+")
		self.assertEqual(resultado, 66)

	def teste_subtracao(self):
		calculadora = Calculadora()
		resultado = calculadora.calcular(100,50,"-")
		self.assertEqual(resultado, 50)

	def teste_subtracao2(self):
		calculadora = Calculadora()
		resultado = calculadora.calcular(15,5,"-")
		self.assertEqual(resultado, 10)
	
	def teste_subtracao3(self):
		calculadora = Calculadora()
		resultado = calculadora.calcular(27,7,"-")
		self.assertEqual(resultado, 20)

	def teste_multiplicacao(self):
		calculadora = Calculadora()
		resultado = calculadora.calcular(10,10,"*")
		self.assertEqual(resultado, 100)

	def teste_multiplicacao2(self):
		calculadora = Calculadora()
		resultado = calculadora.calcular(5,5,"*")
		self.assertEqual(resultado, 25)

	def teste_multiplicacao3(self):
		calculadora = Calculadora()
		resultado = calculadora.calcular(20,4,"*")
		self.assertEqual(resultado, 80)

	def teste_divisao(self):
		calculadora = Calculadora()
		resultado = calculadora.calcular(18,3,"/")
		self.assertEqual(resultado, 6.0)

	def teste_divisao2(self):
		calculadora = Calculadora()
		resultado = calculadora.calcular(100,5,"/")
		self.assertEqual(resultado, 20)
	
	def teste_divisao3(self):
		calculadora = Calculadora()
		resultado = calculadora.calcular(102,17,"/")
		self.assertEqual(resultado, 6)


if __name__ == '__main__':
	main ()
