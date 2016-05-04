# in this program i am using dictionaries to  overload the constructor
# using python 2
class Electrodomestico :

	""" This class Represents a Electrodomestico """

	def __init__(self,dicio) :

		#default

		if len(dicio) == 0 :

			self.color = "blanco"
			self.consumo = "f"
			self.precio = 100
			self.peso = 5
			self.precio_final()

		# with precio and peso

		if "precio" in dicio and "peso" in dicio and "color" not in dicio and "consumo" not in dicio :

			self.precio = dicio["precio"]
			self.peso = dicio["peso"]
			self.color = "blanco"
			self.consumo = 5
			self.precio_final()

		# with all parameters

		if "color" in dicio and "consumo" in dicio and "precio" in dicio and "peso" in dicio :

			if self.comprobar_color(dicio["color"]) == True :

				self.color = dicio["color"]

			else :
				self.color = "blanco"

			if self.comprobar_consumo(dicio["consumo"]) == True :

				self.consumo = dicio["consumo"]
			else :

				self.consumo = "f"

			self.consumo = dicio["consumo"]
			self.precio = dicio["precio"]
			self.peso = dicio["peso"]
			self.precio_final()

	# get methods

	def getcolor(self) :

		return self.color

	def getconsumo(self) :

		return self.consumo

	def getprecio(self) :

		return self.precio

	def getpeso(self) :

		return self.peso

	def comprobar_color(self,color) :

		if color == "blanco" or color == "negro" or color == "azul" or color == "gris" or color == "rojo" :

			return True

		return False

	def comprobar_consumo(self,consumo) :

		if consumo == "a" or consumo == "b" or consumo == "c" or consumo == "d" or consumo == "e" or consumo == "f" :

			return True

		return False

	def precio_final(self) :

		# comprobando consumo

		if self.consumo == "a" :

			self.precio = self.precio + 100

		elif self.consumo == "b" :

			self.precio = self.precio + 80

		elif self.consumo == "c" :

			self.precio = self.precio + 60

		elif self.consumo == "d" :

			self.precio = self.precio + 50

		elif self.consumo == "e" :

			self.precio = self.precio + 30

		elif self.consumo == "f" :

			self.precio = self.precio + 10

		# comprobando peso

		if self.peso >= 0 and self.peso <= 19 :

			self.precio += 10

		elif self.peso >= 20 and self.peso <= 49 :

			self.precio += 50

		elif self.peso >= 50 and self.peso <= 79 :

			self.precio += 80

		elif self.peso >= 80 :

			self.precio += 100


class Lavadora(Electrodomestico) :

	""" This class Represent a washer and it inherit from Electrodomestico"""

	#default constructor

	def __init__(self, dicio) :

		if len(dicio) == 0 :
			Electrodomestico.__init__(self,dicio)
			self.carga = 5
			self.preciofinal(self)

		# with peso and precio

		if "precio" in dicio and "peso" in dicio and "color" not in dicio and "consumo" not in dicio and "carga" not in dicio:

			Electrodomestico.__init__(self,dicio)
			self.carga = 5
			self.preciofinal()

		# with all parameters

		if "color" in dicio and "consumo" in dicio and "precio" in dicio and "peso" in dicio and "carga" in dicio :

			Electrodomestico.__init__(self,dicio)
			self.carga = dicio["carga"]
			self.preciofinal()

	def preciofinal(self) :

		if self.carga > 30 :

			self.precio = self.precio + 50









	









