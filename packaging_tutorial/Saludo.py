import typing


class Saludo:
    def __init__(self, nombre=str):
        self.__nombre = nombre

    def saludo_daniela(self):
        return f'Hola {self.__nombre} este paquete te envia un saludo'