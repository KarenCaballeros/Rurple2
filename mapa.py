class Mapa(object):
	def __init__ (self , largo , ancho):
		self.largo = largo
		self.alto = alto
		self.monedas = []
		self.robot = None

	def agregar_robot(self, robot):
		self.robot = robot

	def agregar_modenas(self, monedas):	
		self.monedas = monedas

	def dibujar(self):
		resultado = ""
		for i in range(self.alto):
			for j in range(self.ancho):
			if j == self.robot.x and i == self.robot.y:
				resultado += robot
			elif j == self.monedas.x and i == self.monedas.y:
				resultado += 1
			else:
				resultado += " "

	def restar_monedas():
					

