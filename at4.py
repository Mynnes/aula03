n1 = float(input("digite o valor da nota1"))
n2 = float(input("digite o valor da nota 2"))
n3 = float(input("digite o valor da nota 3"))

soma = (n1 + n2 + n3)/3

if soma > 6 :
    print(f" aprovado sua nota é {soma}")
else:
    print(f" reprovado sua nota é {soma}")