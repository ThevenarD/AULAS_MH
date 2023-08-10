def Kilometer_to_Meter(km):
    m = km / 3.6
    return m

km = (input("Digite o valor em Km/hr que deseja converter: "))
km = float(km)

print(f"O valor informado foi {km} km/hr e sua conversão é igual {Kilometer_to_Meter(km)} m/s")