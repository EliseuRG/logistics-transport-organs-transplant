import networkx as nx

abreviacoes = ["A1", "A2", "H1", "H2", "H3", "H4", "HD", "HR"]

possibilidades_trajeto = [
["HD", "HR"],
["HD", "H2", "A1", "A2", "HR"],
["HD", "H2", "A1", "A2", "H4", "HR"],
["HD", "H2", "A1", "A2", "H3", "HR"],
["HD", "H1", "H2", "A1", "A2", "HR"],
["HD", "A1", "A2", "HR"],
["HD", "A1", "A2", "H3", "HR"],
["HD", "A1", "A2", "H3", "H4", "HR"],
["HD", "A1", "A2", "H3", "HR"],
["HD", "H4", "HR"],
["HD", "H1", "H4", "HR"],
["HD", "H1", "HR"]
]

# Tempo de transbordo em cada nó
transbordo = {
    "EMB_AMB1": 0.02, 
    "VIA_AMB1": 0,
    "DES_AMB1": 0.02,
    "EMB_HEL1": 0.25,
    "VIA_HEL1": 0,
    "DES_HEL1": 0.25,
    "EMB_AMB2": 0.02, 
    "VIA_AMB2": 0,
    "DES_AMB2": 0.02,
    "EMB_AVI" : 0.5, 
    "VIA_AVI" : 0.625333,
    "DES_AVI" : 0.5,
    "EMB_AMB3": 0.02, 
    "VIA_AMB3": 0,
    "DES_AMB3": 0.02,
    "EMB_HEL2": 0.25,
    "VIA_HEL2": 0,
    "DES_HEL2": 0.25,
    "EMB_AMB4": 0.02,
    "VIA_AMB4": 0,
    "DES_AMB4": 0.02,
}

# Possíveis rotas
rotas = [
    "CAR",
    "HEL",
    "CAR-HEL",
    "HEL-CAR",
    "CAR-HEL-CAR",
    "CAR-AVI-CAR",
    "CAR-AVI-HEL",
    "CAR-AVI-CAR-HEL",
    "CAR-AVI-HEL-CAR",
    "CAR-AVI-CAR-HEL-CAR",
    "HEL-AVI-CAR",
    "HEL-AVI-HEL",
    "HEL-AVI-CAR-HEL",
    "HEL-AVI-HEL-CAR",
    "HEL-AVI-CAR-HEL-CAR",
    "CAR-HEL-AVI-CAR",
    "CAR-HEL-AVI-HEL",
    "CAR-HEL-AVI-CAR-HEL",
    "CAR-HEL-AVI-HEL-CAR",
    "CAR-HEL-AVI-CAR-HEL-CAR",
    "HEL-CAR-AVI-CAR",
    "HEL-CAR-AVI-HEL",
    "HEL-CAR-AVI-CAR-HEL",
    "HEL-CAR-AVI-HEL-CAR",
    "HEL-CAR-AVI-CAR-HEL-CAR",
    "CAR-HEL-CAR-AVI-CAR",
    "CAR-HEL-CAR-AVI-HEL",
    "CAR-HEL-CAR-AVI-CAR-HEL",
    "CAR-HEL-CAR-AVI-HEL-CAR",
    "CAR-HEL-CAR-AVI-CAR-HEL-CAR"
]

tempos_rotas_hospital_receptor = [
[0.02, 0.30222, 0.02, None, None, None, 0.5, 0.625333, 0.5, 0.02, 0.282222, 0.02, None, None, None, None, None, None, None, None, None,],
[0.02, 0.30222, 0.02, None, None, None, 0.5, 0.625333, 0.5, None, None, 0.25, 0.04, 0.25, None, None, None, None, None, None,],
[0.02, 0.30222, 0.02, None, None, None, 0.5, 0.625333, 0.5, 0.02, 0.128889, 0.02, 0.25, 0.02964, 0.25, None, None, None, None],
# demais rotas para o Hospital 1
]
colunas = [
"FIN_REM", "EMBARQ1_AMBU", "VIAGEM1_AMBU", "DESEMB1_AMBU", "EMBARQ1_HELI", "VIAGEM1_HELI", "DESEMB1_HELI",
"EMBARQ2_AMBU", "VIAGEM2_AMBU", "DESEMB2_AMBU", "EMBARQ1_AVIA", "VIAGEM1_AVIA", "DESEMB1_AVIA", "EMBARQ3_AMBU",
"VIAGEM3_AMBU", "DESEMB3_AMBU", "EMBARQ2_HELI", "VIAGEM2_HELI", "DESEMB2_HELI", "EMBARQ4_HELI", "VIAGEM4_HELI",
"DESEMB4_HELI", "INI_REMO", "TOTAL"
]

# Crie o grafo
G = nx.DiGraph()

# Adicione os nós ao grafo
for local in abreviacoes:
    G.add_node(local)

# Adicione as arestas ao grafo
for trajeto in possibilidades_trajeto:
    for i in range(len(trajeto) - 1):
        origem, destino = trajeto[i], trajeto[i+1]
        G.add_edge(origem, destino)

# Crie um dicionário para mapear cada par de nós para o seu tempo de viagem
tempos_viagem = {}
for trajeto, tempos in zip(possibilidades_trajeto, tempos_rotas_hospital_receptor):
    for i in range(len(trajeto) - 1):
        origem, destino = trajeto[i], trajeto[i+1]
        if (origem, destino) not in tempos_viagem or tempos_viagem[(origem, destino)] > tempos[-1]:
            tempos_viagem[(origem, destino)] = tempos[-1]

# Defina os pesos das arestas
for origem, destino in tempos_viagem:
    G[origem][destino]['tempo'] = tempos_viagem[(origem, destino)]

# Encontre a rota mais rápida
origem, destino = 'HD', 'HR'
rota_mais_rapida = nx.dijkstra_path(G, origem, destino, weight='tempo')
print('Rota mais rápida:', ' → '.join(rota_mais_rapida))

# Encontre o tempo total da rota mais rápida
tempo_total = nx.dijkstra_path_length(G, origem, destino, weight='tempo')
print('Tempo total da rota mais rápida:', tempo_total)