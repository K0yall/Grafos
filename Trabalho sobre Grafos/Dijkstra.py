import heapq

# Dicionário de conexões do grafo com distâncias
grafo = {
    'SA': {'WI': 54.34, 'DE': 75.46, 'TA': 19.01},
    'WI': {'SA': 54.34, 'DE': 20.5, 'PG': 28.5, 'JB': 55.88},
    'PG': {'WI': 28.5, 'JB': 35.64, 'IB': 11.7, 'RS': 27.4, 'DE': 24.15},
    'DE': {'SA': 75.46, 'WI': 20.5, 'JB': 39.38, 'PG': 24.15, 'TA': 90.64},
    'JB': {'WI': 55.88, 'DE': 39.38, 'PG': 35.64, 'IB': 20.5},
    'IB': {'JB': 20.5, 'PG': 11.7, 'LO': 34.8},
    'LO': {'IB': 34.8, 'RS': 25.6, 'PN': 29.3},
    'PN': {'LO': 29.3, 'VR': 21.01},
    'VR': {'PN': 21.01, 'IM': 21.01, 'IT': 31.6},
    'IM': {'VR': 21.01, 'IT': 38.4},
    'IT': {'VR': 31.6, 'IM': 38.4, 'AU': 13.3, 'CL': 18.8, 'AL': 62.04},
    'AU': {'IT': 13.3, 'RS': 26.4},
    'CL': {'IT': 18.8},
    'AL': {'IT': 62.04, 'TC': 14.1},
    'TC': {'AL': 14.1, 'BT': 14.4, 'PR': 17.4, 'AG': 55.2},
    'BT': {'TC': 14.4, 'PR': 80.96},
    'AG': {'TC': 55.2, 'PR': 75.03, 'RS': 10.7, 'LA': 8.9},
    'PR': {'BT': 80.96, 'AG': 75.03, 'MD': 37.4, 'TA': 19.4},
    'MD': {'PR': 37.4, 'TA': 19.4},
    'TA': {'SA': 19.01, 'DE': 90.64, 'PR': 19.4, 'MD': 19.4, 'RO': 71.06},
    'RO': {'TA': 71.06, 'LA': 16.6},
    'LA': {'RO': 16.6, 'AG': 8.9, 'RS': 13.01},
    'RS': {'PG': 27.4, 'IB': 25.6, 'LO': 25.6, 'AU': 26.4, 'AG': 10.7, 'LA': 13.01}
}

# Dicionário de cidades com nomes por extenso
cidades_extenso = {
    'SA': 'Salete',
    'WI': 'Witmarsum',
    'PG': 'Presidente Getúlio',
    'DE': 'Dona Emma',
    'JB': 'José Boiteux',
    'IB': 'Ibirama',
    'LO': 'Lontras',
    'PN': 'Presidente Nereu',
    'VR': 'Vidal Ramos',
    'IM': 'Imbuia',
    'IT': 'Ituporanga',
    'CL': 'Chapadão do Lageado',
    'AU': 'Aurora',
    'AL': 'Agrolândia',
    'TC': 'Trombudo Central',
    'AG': 'Agronômica',
    'PR': 'Pouso Redondo',
    'BT': 'Braço do Trombudo',
    'LA': 'Laurentino',
    'RO': 'Rio do Oeste',
    'TA': 'Taió',
    'MD': 'Mirim Doce',
    'RS': 'Rio do Sul'
}

# Dicionário invertido para converter nomes por extenso em códigos
cidades_abreviado = {v.upper(): k for k, v in cidades_extenso.items()}

def converter_para_codigo(nome_ou_codigo):
    """Converte um nome por extenso para código ou verifica se é um código válido."""
    nome_ou_codigo = nome_ou_codigo.strip().upper()
    if nome_ou_codigo in cidades_abreviado:
        return cidades_abreviado[nome_ou_codigo]
    elif nome_ou_codigo in cidades_extenso.values():
        return cidades_abreviado[nome_ou_codigo.upper()]
    else:
        raise ValueError(f"{nome_ou_codigo} não é um código ou nome de cidade válido.")

def dijkstra(grafo, inicio, fim):
    """Implementa o algoritmo de Dijkstra para encontrar o caminho mais curto."""
    if inicio not in grafo or fim not in grafo:
        raise ValueError("Cidade de origem ou destino não está no grafo.")

    distancias = {cidade: float('inf') for cidade in grafo}
    distancias[inicio] = 0
    predecessores = {cidade: None for cidade in grafo}
    heap = [(0, inicio)]  # (distância, cidade)

    while heap:
        distancia_atual, cidade_atual = heapq.heappop(heap)

        if distancia_atual > distancias[cidade_atual]:
            continue

        if cidade_atual == fim:
            break

        for vizinho, peso in grafo[cidade_atual].items():
            nova_distancia = distancia_atual + peso
            if nova_distancia < distancias[vizinho]:
                distancias[vizinho] = nova_distancia
                predecessores[vizinho] = cidade_atual
                heapq.heappush(heap, (nova_distancia, vizinho))

    caminho = []
    cidade_atual = fim
    while cidade_atual is not None:
        caminho.insert(0, cidade_atual)
        cidade_atual = predecessores[cidade_atual]
    
    if caminho[0] == inicio:
        return caminho, distancias[fim]
    else:
        return [], float('inf')

# Entrada do usuário para origem e destino
entrada_source = input("Informe a cidade de origem (por extenso ou código): ").strip()
entrada_destination = input("Informe a cidade de destino (por extenso ou código): ").strip()

try:
    source = converter_para_codigo(entrada_source)
    destination = converter_para_codigo(entrada_destination)

    caminho, distancia = dijkstra(grafo, source, destination)

    if caminho:
        caminho_nomes = [cidades_extenso[cidade] for cidade in caminho]
        print("Caminho mais curto entre", cidades_extenso[source], "e", cidades_extenso[destination], ":", ' -> '.join(caminho_nomes))
        print("Comprimento do caminho:", f"{distancia:.2f} km")
    else:
        print(f"Não há um caminho entre '{cidades_extenso[source]}' e '{cidades_extenso[destination]}'.")
except ValueError as e:
    print(f"Erro: {e}")
except KeyError as e:
    print(f"Erro de chave: {e}")
except Exception as e:
    print(f"Erro inesperado: {e}")
