vet = []
impar = 0
pos = 0
neg = 0
par = 0 
for i in range(5):
    num = int(input())
    vet.append(num)
for num in vet:
    if(num % 2 == 0):
        par = 1 + par
    else:
        impar =  1 + impar
    if(num>0):
        pos = 1 + pos 
    if(num<0):
        neg = 1 + neg
print(f"{par} valor(es) par(es)\n")
print(f"{impar} valor(es) impar(es)\n")
print(f"{pos} valor(es) positivo(s)\n")
print(f"{neg} valor(es) negativo(s)\n")