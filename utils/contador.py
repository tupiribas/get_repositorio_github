from time import time


class Contador():
    def __init__(self):
        self.inicio
        self.fim

    def inicio(self):
        self.inicio = time()

    def fim(self):
        self.fim = time()

    def tempo_total(self):
        return self.fim - self.inicio
