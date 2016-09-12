from mapa import Mapa
from robot import Robot
from monedas import Monedas
import time
import utilidades

nombre_mapa =  "mapas/" + (input("Ingrese: ")) + ".txt"
lista_mapa = utilidades.cargar_mapa(nombre_mapa)
nombre_instrucciones =  "instrucciones/" + (input("Ingrese: ")) + ".txt"
lista_instrucciones = utilidades.cargar_instrucciones(nombre_instrucciones)
#print(lista_mapa)
#print(lista_instrucciones)

objeto_mapa = Mapa((len(lista_mapa[0])) , (len(lista_mapa))) 

for i in range(len(lista_mapa)):
	for j in range(len(lista_mapa[0])):
		if lista_mapa[i][j] == "*":		
			objeto_robot = Robot(j ,i)
			objeto_robot.agregar_mapa(objeto_mapa)
			objeto_mapa.agregar_robot(objeto_robot)		
		elif int(lista_mapa[i][j]) > 0:	
			for k in range(int(lista_mapa[i][j])):
				objeto_moneda = Monedas(j , i)
				objeto_mapa.agregar_moneda(objeto_moneda)
				#print(objeto_mapa.contar_monedas(j , i))

print("")
print("Monedas en el mapa: " , objeto_mapa.monedas_en_mapa())
print("Tus monedas: " , objeto_robot.monedas)
print(objeto_mapa.dibujar())
print("")

for i in lista_instrucciones:
	#print(i)
	if i == "ROTATE":
		objeto_robot.rotar()
	elif i == "MOVE":
		objeto_robot.mover()
	else:
		objeto_robot.recoger()

	print("Monedas en el mapa: " , objeto_mapa.monedas_en_mapa())
	print("Tus monedas: " , objeto_robot.monedas)
	print("")		

	
	print (objeto_mapa.dibujar())								
	time.sleep(0.5)