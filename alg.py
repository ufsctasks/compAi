import heapq

class GrafoMatriz:
    def __init__(self, vertices):
        self.num_vertices = vertices
        self.matriz = [[0] * vertices for _ in range(vertices)]

    def adicionar_aresta(self, u, v, peso):
        self.matriz[u][v] = peso
        self.matriz[v][u] = peso

    def mostrar_matriz(self):
        for linha in self.matriz:
            print(linha)

    def heuristica(self, atual, destino):
        heuristicas = {
            0: {1: 30, 2: 120},  # Estimativas para A (0)
            1: {0: 30, 2: 60},   # Estimativas para B (1)
            2: {0: 120, 1: 60},  # Estimativas para C (2)
        }
        return heuristicas.get(atual, {}).get(destino, 0)

    def a_estrela(self, inicio, fim):
        fila_prioridade = [(0, 0, inicio, [])]
        visitados = set()

        while fila_prioridade:
            f_atual, g_atual, atual, caminho = heapq.heappop(fila_prioridade)

            if atual in visitados:
                continue

            visitados.add(atual)
            caminho = caminho + [atual]

            if atual == fim:
                return caminho, g_atual

            for vizinho in range(self.num_vertices):
                peso_aresta = self.matriz[atual][vizinho]

                if peso_aresta == 0:
                    continue

                g_vizinho = g_atual + peso_aresta
                h_vizinho = self.heuristica(vizinho, fim)
                f_vizinho = g_vizinho + h_vizinho
                heapq.heappush(fila_prioridade, (f_vizinho, g_vizinho, vizinho, caminho))

        return None, float('inf')

# Exemplo de uso
grafo_matriz = GrafoMatriz(3)
grafo_matriz.adicionar_aresta(0, 1, 50)  # A <-> B: 50 km
grafo_matriz.adicionar_aresta(0, 2, 150) # A <-> C: 150 km
grafo_matriz.adicionar_aresta(1, 2, 80)  # B <-> C: 80 km

grafo_matriz.mostrar_matriz()

caminho, custo_total = grafo_matriz.a_estrela(2, 0)

print(f"Menor caminho: {caminho}")
print(f"Custo total: {custo_total}")
