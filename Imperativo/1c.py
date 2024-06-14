lista_palavras = input().split()

if len(lista_palavras) == 3:
    maior_palavra = " "
    lista_caixa_alta =[]
    for x in lista_palavras:
        lista_caixa_alta.append(x.upper())
        if len(maior_palavra)<len(x):
            maior_palavra = x.upper()
    
    print(f"Palavras em caixa alta = {lista_caixa_alta}\n")
    print(f"Maior palavra = {maior_palavra}")
    
    
