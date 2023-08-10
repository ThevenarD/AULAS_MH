def Desconto(Valor):
    Valor_Final = (Valor - (Valor * 0.12))
    return Valor_Final

Valor = float(input("Digite o valor do produto: "))
print(f"\nO valor do produto após o desconto é igual {Desconto(Valor)} ")