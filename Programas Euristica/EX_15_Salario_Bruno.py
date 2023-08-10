def Salario_Liquido(Salario_Bruto):
    Liquido = (Salario_Bruto + (Salario_Bruto * 0.05) - (Salario_Bruto * 0.07))
    return Liquido
Salario_Bruto = float(input("Digite o valor do salário: "))
print(f"O valor do salario Liquido é igual a {Salario_Liquido(Salario_Bruto)}")
 