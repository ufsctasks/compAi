def algoritmo_moeda(troco, moedas_disponiveis):
    resultado = []
    for moeda in sorted(moedas_disponiveis, reverse=True):
        while troco >= moeda:
            troco -= moeda
            resultado.append(moeda)
    return resultado

moedas_disponiveis = [50, 25, 10, 5, 1]

troco = 28

resultado = algoritmo_moeda(troco, moedas_disponiveis)

print(f"Menor número de moedas: {len(resultado)}")
print(f"Moedas usadas: {resultado}")
