def Soma(num1,num2):
  print(num1 + num2)
def subtração (num1,num2):
  print(num1 - num2)
def divisão(num1,num2):
    print(num1 / num2)
def multiplicação (num1,num2):
    print(num1 * num2)
def potencialização (num1,num2):
    print(num1 ** num2)

print("Bem vindo! \n Por favor escolha umas das opções:\n 1.Adição\n 2.Subtração \n 3.multiplicação\n 4.divisão\n 5.potencialização\n ")
escolha = int(input())

num1 = float(input('digite um número: '))
num2 = float(input('digite segundo número: '))

if escolha == 1:
    Soma(num1,num2)
elif escolha == 2:
    subtração(num1,num2)
elif escolha == 3:
    multiplicação(num1,num2)
elif escolha == 4:
    divisão(num1,num2)
elif escolha == 5:
    potencialização(num1,num2)
else:
    print('digite opção invalida')



