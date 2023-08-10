import math
def Media_Aluno(n1,n2,n3,n4):
    Media = ((n1 + n2 + n3 + n4) / 4)
    return Media

n1 = float(input("Digite a primeira nota: "))
n2 = float(input("Digite a segunda nota: "))
n3 = float(input("Digite a terceira nota: "))
n4 = float(input("Digite a quarta nota: "))

print(f"A Média do Aluno é igual {Media_Aluno(n1,n2,n3,n4)}")