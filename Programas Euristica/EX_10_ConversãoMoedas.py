def Real_to_Dolar(Real):
    Dolar = Real * 0.21
    return Dolar

Real = float(input("Digite o valor de Reais a ser convertido: "))
print(f"O valor em Dolares de R$ {Real} é de U$ {Real_to_Dolar(Real)}")