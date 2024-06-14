repetir = True 

while repetir:
    nome = input("Digite seu nome: ")
    idade = input("Digite sua idade: ")
    msg = "O seu nome é {0} e você tem {1} anos\n".format(nome,idade)
    print(msg)
    resposta = input("deseja registar mais pessoas?")
    if(resposta.lower()== "Sim" or resposta == "sim"):
        repetir = True
    else:
        repetir = False

