lista_num = [int(n) for n in input().split()]
menor_num = lista_num[0]
maior_num = lista_num[0]
media = 0

for num in lista_num:
    if(menor_num > num):
        menor_num = num
    if(maior_num < num):
        maior_num = num
    media = media + num

media = media / len(lista_num)

print(f"O menor numero é {menor_num}\n")
print(f"O maior numero é {maior_num}\n")
print(f"A media é {media}\n")