class Calculadora():
    def __init__(self):
        print('============= BOAS VINDAS À CALCULADORA DO MESTRE DOS MAGOS ==============')
        while True:
            operador = None
            while operador not in ['1','2','3','4','0']:
                operador = input('\nSelecione a operação desejada:\n1-Soma;\n2-Subtração;\n3-Divisão;\n4-Multiplicação;\n0-Sair;\n')

            if operador == '0': 
                print('Muito obrigado por usar a calculadora! Volte sempre!')
                break

            while True:
                try:
                    self.num1 = float(input('Escreva o primeiro número: '))
                    self.num2 = float(input('Escreva o segundo número: '))
                    break
                except ValueError:
                    print("Por favor, insira números válidos.\n")

            print('\n= = = = = = = = = = = =')
            if operador == '1': print(f'O resultado é {self.somar()}')
            if operador == '2': print(f'O resultado é {self.subtrair()}')
            if operador == '3': print(f'O resultado é {self.dividir()}')
            if operador == '4': print(f'O resultado é {self.multiplicar()}')
            print('= = = = = = = = = = = =')

    def somar(self):
        return self.num1 + self.num2
    
    def subtrair(self):
        return self.num1 - self.num2
    
    def dividir(self):
        return self.num1 / self.num2
    
    def multiplicar(self):
        return self.num1 * self.num2


calc = Calculadora()