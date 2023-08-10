

valor = float(input("Digite o valor da venda: "))
tipo = int(input("Digite 1 para À Vista, ou 2 para Parcelado: "))

if tipo == 1:
        valor_comissao = ((valor - (valor * 0.1))*(0.05))
        valor_final = (valor - (valor * 0.1))
        print(f"O valor da venda é R$ {valor_final}\nO valor da comissão é R$ {valor_comissao}")
else:
        valor_comissao = (valor * 0.05)
        valor_parcela = (valor / 3)
        print(f"O valor da parcela em 3x é R$ {valor_parcela}\nO valor da comissão é R$ {valor_comissao}")

