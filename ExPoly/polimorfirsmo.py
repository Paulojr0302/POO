class Super:
    def hello(self):
        print("Olá, sou a superclasse!")

class Sub(Super):
    def hello(self):
        print("Olá, sou a subclasse!")

class Subsub(Sub):
    def hello(self):
        print("Olá, sou a subsubclasse!")

mensagem = int(input(
    'Digite a mensagem que deseja ver: 1 para super, 2 para sub, 3 para subsub: '
))

if mensagem == 1:
    teste = Super()
elif mensagem == 2:
    teste = Sub()
elif mensagem == 3:
    teste = Subsub()
else:
    print('Opção inválida')
    exit()

teste.hello()
