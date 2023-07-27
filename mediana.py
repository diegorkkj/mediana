import os

vari = [0, 1, 2, 3, 4]

vari[0] = int(input("Digite o primeiro numero: "))
vari[1] = int(input("Digite o segundo numero: "))
vari[2] = int(input("Digite o terceiro numero: "))
vari[3] = int(input("Digite o quarto numero: "))
vari[4] = int(input("Digite o quinto numero: "))

maior = vari[0]
menor = vari[0]

for i in vari:
    if i > maior:
        maior = i
    if i < menor:
        menor = i

print(f"O maior numero é o {maior}")
print(f"O menor numero é o {menor}")

os.system("pause")
