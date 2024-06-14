def somar (a,b):
    resultado = a + b
    return resultado

def subtrair (a,b):
    resultado = a - b
    return resultado

def multiplar (a,b):
    resultado = a * b
    return resultado

def dividir (a,b):
    resultado = a / b
    return resultado

def main():
    while True:
        print("Digite 1 para Somar\n")
        print("Digite 2 para Subtrair\n")
        print("Digite 3 para Multiplicar\n")
        print("Digite 4 para Dividir\n")
        print("Digite 5 para Sair\n")
        opcao = input("Qual sua opção? ")
        if opcao == '5':
            print("Encerrando o programa.")
            break

        num1 = int(input("Digite o valor de A: "))
        num2 = int(input("Digite o valor de B: "))
    
        if opcao == "1":
                print("Resultado da soma:", somar(num1,num2))
        elif opcao == "2":
             print("Resultado da subtração:", subtrair(num1,num2))
        elif opcao == "3":
                print("Resultado da multiplicação:", multiplar(num1,num2))
        elif opcao == "4":
                print("Resultado da divisão:", dividir(num1,num2))
        else:
            print("Digite uma opção valida\n")
            
if __name__ == "__main__":
    main()