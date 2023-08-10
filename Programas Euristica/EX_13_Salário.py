def Aumento(Salario):
    Salario_Final = (Salario + (Salario * 0.25))
    return Salario_Final

Salario = float(input("Informe o salário do funcionário: "))

print(f"O novo salário é igual R$ {Aumento(Salario)}")