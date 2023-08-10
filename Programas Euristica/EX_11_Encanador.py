def Tarifas_das_Taxas(numero):
    if numero == 0: 
        return 0
    else:
       Custo = (80 + (numero * 55))
    return Custo

numero = int(input("Quantos dias o encanador irá trabalhar: "))
print(f"O custo do serviço do operador será igual: R$ {Tarifas_das_Taxas(numero)}")