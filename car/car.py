class Car:

    x = 'abcd' # Eu não preciso criar um objeto pro X existir

    def __init__(self, name, maker, color, ano):
        self.name = name
        self.maker =  maker
        self.color = color
        self.ano = ano


def drive (self):
    print(self.ano)
    print(self.color)
    print(self.maker)
    print(self.name)

@classmethod
def show(cls):
    print(cls.x)
