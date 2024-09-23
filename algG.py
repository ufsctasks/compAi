def algoritmo_moeda(troco, moedas_disponiveis):
    resultado = []
    for moeda in sorted(moedas_disponiveis, reverse=True):
        while troco >= moeda:
            troco -= moeda
            resultado.append(moeda)
    return resultado

moedas_disponiveis = [200, 100, 50, 20, 10, 5, 2, 1, 0.5, 0.25, 0.10, 0.05, 0.01]

troco = 20.78 #em reais

resultado = algoritmo_moeda(troco, moedas_disponiveis)

print(f"Menor número de moedas: {len(resultado)}")
print(f"Moedas usadas: {resultado}")
