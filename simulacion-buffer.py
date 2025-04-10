import time
import random

class Nodo: 
    def __init__(self, nombre):
        #inicializa un nodo con un nombre y una lista de conexiones vacia
        self.nombre = nombre
        self.conexiones = []

    def agrega_conexion(self, nodo):
        #agrega un nodo a la lista de conexiones
        self.conexiones.append(nodo)

    def eliminar_conexion(self, nodo):
        #elimina un nodo de la lista de conexiones si esta presente
        if nodo in self.conexiones:
            self.conexiones.remove(nodo)
    
    def procesar_buffer(self, nodo, mensaje):
        if nodo in self.conexiones:
            if random.random() < 0.3:
                #simula una probabilidad del 30% de perdida del paquete
                print(f"Paquete perdido de {self.nombre} a {nodo.nombre}")
                time.sleep(1)
            else:
                #si no se pierde el paquete, se envia el mensaje al nodo destino
                nodo.recibir_mensaje(mensaje, self.nombre)


    def enviar_mensaje(self, mensaje):
        #envia un mensaje a todos los nodos conectados
        print(f"{self.nombre} envia mensaje: {mensaje}")
        for nodo in self.conexiones:
            nodo.recibir_mensaje(mensaje, self.nombre)

    def recibir_mensaje(self, mensaje, remitente):
        #recibe un mensaje de otro nodo e imprime el mensaje recibido
        print(f"{self.nombre} recibio mensaje de {remitente}: {mensaje}")

#crear nodos
servidor = Nodo("Servidor")
cliente1 = Nodo("Cliente1")
cliente2 = Nodo("Cliente2")
cliente3 = Nodo("Cliente3")

#establecer conexiones iniciales
servidor.agrega_conexion(cliente1)
servidor.agrega_conexion(cliente2)
servidor.agrega_conexion(cliente3)

#enviar mensaje inicial
servidor.enviar_mensaje("Hola, clientes!")

#simulacion de desconexion
print("\nSimulando desconexion de Cliente2...\n")
servidor.eliminar_conexion(cliente2)

#esperar 1 segundo para simular el retraso
time.sleep(1)

#simulacion de reconexion
print("\nSimulando desconexion y reconexión dinamica...\n")
servidor.agrega_conexion(cliente2)

#enviar mensaje despues de la reconexion
servidor.enviar_mensaje("¡Hola de nuevo a todos!")

servidor.procesar_buffer(cliente3, "Mensaje importante")
#envia un mensaje al nodo cliente3 simulando perdidas de paquete

