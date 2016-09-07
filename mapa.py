class Mapa(object):
	def __init__ (self , largo , alto):
		self.largo = largo
		self.alto = alto
		self.monedas = []
		self.robot = None
		self.contador = 0

	def agregar_robot(self, robot):
		self.robot = robot

	def agregar_moneda(self, monedas):	
		self.monedas.append(monedas)

	def dibujar(self):
		resultado = ""
		#resultado += ("_" * self.largo)
		for i in range(self.alto):
			for j in range(self.largo):
				if j == self.robot.x and i == self.robot.y:
					resultado += self.robot.dibujar()
				elif self.contar_monedas(j , i) > 0:
					resultado += str(self.contar_monedas(j, i))
				else:
					resultado += " "
			resultado +=  "\n" 
		resultado += ("_" * self.largo)			
		return resultado			

	def contar_monedas(self, x, y):
		cont = 0
		lista_monedas = self.monedas
		while (x , y) in lista_monedas:
			cont += 1
			lista_monedas.pop((x, y))
		return cont	



	#	contador_monedas = 0
	#	for moneda in self.monedas:
	#		if moneda.x == x and moneda.y == y:
	#			if 
	#			contador_monedas += 1
	#	return contador_monedas		


	def restar_monedas(self , x , y):
		si_hay_monedas = -1
		for i in range(len(self.monedas)):
			moneda = self.monedas[i]
			if moneda.x == x and moneda.y == y:
				si_hay_monedas = i
				break 

		if si_hay_monedas >= 0:
			self.monedas.pop(si_hay_monedas)
	
	def monedas_en_mapa(self):
		contador = 0
		for moneda in self.monedas:
			contador += 1
		return contador	
	
		



					

