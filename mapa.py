class Mapa(object):
	def __init__ (self , largo , ancho):
		self.largo = largo
		self.alto = alto
		self.monedas = []
		self.robot = None

	def agregar_robot(self, robot):
		self.robot = robot

	def agregar_moneda(self, monedas):	
		self.monedas.append(monedas)

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

	def contar_monedas(self, x, y):
		cont = 0
		for moneda in self.monedas:
			if moneda.x == x and moneda.y == y:
				cont+= 1
		return cont

	def restar_monedas(self , x , y):
		si_hay_monedas = -1
		for i in range(len(self.monedas)):
		moneda = self.monedas[i]
		if moneda.x == x and moneda.y == y:
			si_hay_monedas = i
			break 

		if si_hay_monedas >= 0:
			self.monedas.pop(si_hay_monedas)
	
	
		



					

