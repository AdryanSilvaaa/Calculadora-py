#calculadora usando funçoes

def soma(a,b):
   return round(a + b, 1)

def subtrair(a,b):
    return round(a - b, 1)

def multiplicar(a,b):
    return round(a * b, 1)

def dividir(a,b):
    if b != 0:
        return round(a / b, 1)
    else:
        return "erro! Divisão por zero."
    
def calculadora():
    print("Selecione uma opção:")
    print("1. Adição")
    print("2. Subtração")
    print("3. Multiplicação")
    print("4. Divisão")

    escolha = input("Digite qual função deseja usar (1/2/3/4)")

    valor1 = float(input("Digite o primeiro valor "))
    valor2 = float(input("Digite o segundo valor "))

    if escolha == "1":
        print(f"{valor1} + {valor2} = {soma(valor1 , valor2)}")
    elif escolha == "2" :
        print(f"{valor1} - {valor2} = {subtrair(valor1, valor2)}")
    elif escolha == "3":
        print(f"{valor1} * {valor2} = {multiplicar(valor1, valor2)}")
    elif escolha == "4":
        print(f"{valor1} / {valor2} = {dividir(valor1, valor2)}")
    else:
            print("ERRO OPÇÃO ERRADA")

calculadora()




