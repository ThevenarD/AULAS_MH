def celsius_to_kelvin (K):
    return K + 273.15

def kelvin_to_celsius (C):
    return C - 273.15

Option = input("Escolha o Modulo de Conversão:\n[C Para Celsius]\n[K Para Kelvin]\nSELECT: ")
Temp = float(input("Escolha a Temperatura Desejada: "))

Switch = {
    "K": celsius_to_kelvin,
    "C": kelvin_to_celsius
}

Resultado = Switch[Option](Temp)
print(f"A Temperatura é {Resultado}")