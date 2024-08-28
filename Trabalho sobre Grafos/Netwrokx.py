import networkx as nx

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
    'PE': 'Petrolândia',
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

# Criando o grafo
G = nx.Graph()

# Adicionando as arestas com pesos ao grafo
edges = [
    ('SA', 'WI', 54.34),
    ('SA', 'DE', 75.46),
    ('SA', 'TA', 19.01),
    ('WI', 'DE', 20.5),
    ('WI', 'PG', 28.5),
    ('WI', 'JB', 55.88),
    ('JB', 'DE', 39.38),
    ('JB', 'PG', 35.64),
    ('JB', 'IB', 20.5),
    ('PG', 'IB', 11.7),
    ('PG', 'RS', 27.4),
    ('PG', 'DE', 24.15),
    ('IB', 'LO', 34.8),
    ('LO', 'RS', 25.6),
    ('LO', 'PN', 29.3),
    ('PN', 'VR', 21.01),
    ('VR', 'IM', 21.01),
    ('VR', 'IT', 31.6),
    ('IM', 'IT', 38.4),
    ('IT', 'AU', 13.3),
    ('IT', 'CL', 18.8),
    ('IT', 'PE', 26.8),
    ('IT', 'AL', 62.04),
    ('AU', 'RS', 26.4),
    ('CL', 'PE', 55.44),
    ('AL', 'TC', 14.1),
    ('TC', 'BT', 14.4),
    ('TC', 'PR', 17.4),
    ('TC', 'AG', 55.2),
    ('BT', 'PR', 80.96),
    ('AG', 'PR', 75.03),
    ('AG', 'RS', 10.7),
    ('AG', 'LA', 8.9),
    ('PR', 'MD', 37.4),
    ('PR', 'TA', 19.4),
    ('MD', 'TA', 19.4),
    ('TA', 'RO', 71.06),
    ('TA', 'DE', 90.64),
    ('RO', 'LA', 16.6),
    ('LA', 'RS', 13.01),
]

G.add_weighted_edges_from(edges)

def converter_para_codigo(nome_ou_codigo):
    """Converte um nome por extenso para código ou verifica se é um código válido."""
    nome_ou_codigo = nome_ou_codigo.strip().upper()
    if nome_ou_codigo in cidades_abreviado:
        return cidades_abreviado[nome_ou_codigo]
    elif nome_ou_codigo in cidades_extenso:
        return nome_ou_codigo
    else:
        raise ValueError(f"{nome_ou_codigo} não é um código ou nome de cidade válido.")

# Entrada do usuário para origem e destino
entrada_source = input("Informe a cidade de origem (por extenso ou código): ").strip()
entrada_destination = input("Informe a cidade de destino (por extenso ou código): ").strip()

try:
    source = converter_para_codigo(entrada_source)
    destination = converter_para_codigo(entrada_destination)

    # Verificar se os nós estão no grafo
    if source not in G.nodes:
        print(f"Nó de origem '{source}' não está no grafo.")
    if destination not in G.nodes:
        print(f"Nó de destino '{destination}' não está no grafo.")
    
    # Adicionar uma verificação se os nós realmente existem no grafo
    if source in G.nodes and destination in G.nodes:
        # Encontrar o caminho mais curto e o comprimento do caminho
        shortest_path = nx.shortest_path(G, source=source, target=destination, weight='weight')
        shortest_path_length = nx.shortest_path_length(G, source=source, target=destination, weight='weight')

        # Converter códigos das cidades para nomes por extenso
        shortest_path_names = [cidades_extenso[cidade] for cidade in shortest_path]

        # Formatar o comprimento do caminho para 2 casas decimais e adicionar "km"
        shortest_path_length_formatted = f"{shortest_path_length:.2f} km"

        # Exibindo o resultado
        print("Caminho mais curto entre", cidades_extenso[source], "e", cidades_extenso[destination], ":", ' -> '.join(shortest_path_names))
        print("Comprimento do caminho:", shortest_path_length_formatted)
    else:
        if source not in G.nodes:
            print(f"Nó de origem '{source}' não está presente no grafo.")
        if destination not in G.nodes:
            print(f"Nó de destino '{destination}' não está presente no grafo.")
except ValueError as e:
    print(e)
except nx.NetworkXNoPath as e:
    print(f"Não há um caminho entre '{entrada_source}' e '{entrada_destination}'.")
except nx.NodeNotFound as e:
    print(f"Erro: {e}")
