class Robot(object):
	def __init__(self , x, y):
		self.x = x #j
		self.y = y #i
		self.direccion = "UP"
		self.monedas = []
		self.mapa = None

	def agregar_mapa(mapa):
		self.mapa = mapa	

	def dibujar(self):
		if self.direccion == "UP":
			return "^" 
		elif self.direccion == "RIGHT":
			return ">"
		elif self.direccion == "DOWN":
			return "v"
		else:
			return "<"	

	def rotar(self):
		if self.direccion == "UP":
			self.direccion = "RIGHT"
		elif self.direccion == "RIGHT":
			self.direccion = "DOWN"
		elif self.direccion == "DOWN":
			self.direccion == "LEFT"
		else:
			self.direccion = "UP"

	def recoger(self):
		if self.mapa.contar_monedas(self.x , self.y) > 0:
			self.monedas += 1
			self.mapa.restar_monedas(x , y)

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

			