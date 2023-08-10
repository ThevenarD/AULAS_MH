import math

def Radianos(G):
    R = ((G * math.pi)/180.0)
    return R

G = float(input("Digite o valor em Graus que deseja converter para radianos: "))

print(f"O valor de {G} em Graus, foi convertido para {Radianos(G)}")