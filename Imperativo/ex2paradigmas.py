def fatorial (num):
    if(num == 0):
        return 1
    else:
        return num * fatorial(num - 1)
    
p = int(input("Digite o valor de p:"))
q = int(input("Digite o valor de q:"))
pfat = 0
qfat = 0
pqfat = 0
resultado = 0

pfat = fatorial(p)
qfat = fatorial(q)

if(p>=q):
    pqfat = fatorial(p-q)
    resultado = pfat / (qfat * pqfat)
    print(f"Resultado = {resultado}")
else:
    pqfat = fatorial(q-p)
    resultado = qfat / (pfat * pqfat)
    print(f"Resultado = {resultado}")