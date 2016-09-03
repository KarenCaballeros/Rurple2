class Robot(object):
	def __init__(self , x, y):
		self.x = x #j
		self.y = y #i
		self.direccion = "UP"
		self.monedas = []
		self.mapa = None

	def agregar_mapa(mapa):
		self.mapa = mapa	

	def sumar_monedas(monedas):
		self.monedas = monedas

	def dibujar(self):
		for i in range(mapa.altura):
			for j in range(mapa.ancho):
				if j == y and i == x:
					return 

	def rotar(self):
		if self.direccion == "UP":
			self.direccion = "RIGHT"
		elif self.direccion == "RIGHT":
			self.direccion = "DOWN"
		elif self.direccion == "DOWN":
			self.direccion == "LEFT"
		else:
			self.direccion = "UP"

	def mover(self):
		if self.direccion == "UP":
			self.x -= 1
		elif self.direccion == "RIGHT":
			self.y += 1
		elif self.direccion == "DOWN":
			self.x += 1
		else:
			self.y -= 1
		
		if self.x <= 0:
			self.x = 0
		elif self.y <= 0:
			self.y = 0
		elif self.x >= ancho:
			self.x = ancho
		elif self.y >= altura:
			self.y = altura			 	


	def recoger(self):		
		if self.x == self.monedas.x and self.y == self.monedas.y:
			self.monedas +=1
			break


	def sumar_monedas(self):
		if self.monedas		

			