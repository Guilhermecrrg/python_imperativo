def media_ponderada (num = []):
    tamanho = len(num)
    cont = 0
    media_pond = 0
    peso = []

    for n in num:
        if(cont == 0 or cont == 1 or cont == (tamanho - 2) or cont == (tamanho - 1)):
           num[cont] = (n * 0.3)
           peso.append(0.3)
           cont= cont + 1
        else:
            num[cont] = (n  * 0.1)
            peso.append(0.1)
            cont= cont + 1

    media_pond = (sum(num)) / (sum(peso))
    return media_pond

num = [float(n) for n in input().split()]

if len(num)>=5:
    mediap = media_ponderada(num)
    print(mediap)
    
else:
    print("Digite no minimo 5 valores\n")