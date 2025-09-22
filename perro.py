#Creamos clase perro
class Perro:
    def __init__(self, color, color_ojo, altura, largo, peso, nombre, raza, comportamiento):
        self.color = color
        self.color_ojo = color_ojo
        self.altura = altura
        self.largo = largo
        self.peso = peso
        self.nombre = nombre
        self.raza = raza
        self.comportamiento = comportamiento

#Definimos los getters
    def get_color(self):
        return self.color

    def get_color_ojo(self):
        return self.color_ojo

    def get_altura(self):
        return self.altura

    def get_largo(self):
        return self.largo

    def get_peso(self):
        return self.peso

    def get_nombre(self):
        return self.nombre

    def get_raza(self):
        return self.raza

    def get_comportamiento(self):
        return self.comportamiento
    
#Definimos los setters

    def set_color(self, color):
        self.color = color

    def set_color_ojo(self, color_ojo):
        self.color_ojo = color_ojo

    def set_altura(self, altura):
        self.altura = altura

    def set_largo(self, largo):
        self.largo = largo

    def set_peso(self, peso):
        self.peso = peso

    def set_nombre(self, nombre):
        self.nombre = nombre

    def set_raza(self, raza):
        self.raza = raza

    def set_comportamiento(self, comportamiento):
        self.comportamiento = comportamiento