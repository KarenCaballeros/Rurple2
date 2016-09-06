from mapa import Mapa
from robot import Robot
from moneda import Monedas
import time
import utilidades

nombre_mapa =  "mapas/" + (input("Ingrese: ")) + ".txt"
lista_mapa = utilidades.cargar_mapa(nombre_mapa)
nombre_instrucciones =  "instrucciones/" + (input("Ingrese: ")) + ".txt"
lista_instrucciones = utilidades.cargar_instrucciones(nombre_instrucciones)

mi_mapa = Mapa( (len(lista_mapa[0])) , (len(lista_mapa)) )

for i in lista_mapa:
	for j in i:
		if j == "*":		
			objeto_robot = Robot(j ,i)
			objeto_robot.agregar_mapa(mi_mapa)
			mi_mapa.agregar_robot(mi_robot)		
		else:	
			for i in range(j):
				mi_moneda = Monedas(j , i)
				objeto_mapa.agregar_monedas()

for i in lista_instrucciones:
	if i == "ROTATE":
		mi_robot.rotar()
	elif i == "MOVE":
		mi_robot.mover()
	else:
		mi_robot.recoger()

print(mi_mapa.dibujar())								
time.sleep(1)
