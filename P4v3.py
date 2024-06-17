import pandas as pd

# Dados da rota 1 para o hospitai1 (distâncias em km , tempos em horas)
hospitais = {
    'Hospital 1': {

        # Distâncias entre locais
        'HD_HR_DIST_AMBU'  : 518,         # hospital doador e hospital receptor
        'HD_H2_DIST_HELI'  : 2.76,        # hospital doador e heliponto 2
        'HD_H1_DIST_AMBU'  : 3.6,         # hospital doador e heliponto 1
        'HD_A1_DIST_AMBU'  : 12.05,       # hospital doador e aeroporto 1
        'HD_A1_DIST_HELI'  : 13.06,       # hospital doador e aeroporto 1
        'H1_HR_DIST_HELI'  : 457,         # hospital receptor e heliponto 1
        'H1_H2_DIST_HELI'  : 9.55,        # heliponto 1 e heliponto 2
        'H1_A1_DIST_HELI'  : 9.55,        # heliponto 1 e aeroporto 1
        'H2_A1_DIST_HELI'  : 10.7,        # heliponto 2 e aeroporto 1
        'A1_A2_DIST_AVIA'  : 469,         # aeroporto 1 e aeroporto 2
        'A2_HR_DIST_AMBU'  : 10,          # aeroporto 2 e hospital receptor
        'A2_HR_DIST_HELI'  : 12.7,        # aeroporto 2 e hospital receptor
        'A2_H4_DIST_HELI'  : 8.76,        # aeroporto 2 e heliponto 4
        'A2_H3_DIST_AMBU'  : 58,          # aeroporto 2 e heliponto 3
        'H3_H4_DIST_HELI'  : 6.7,         # heliponto 3 e heliponto 4
        'H4_HR_DIST_HELI'  : 1.6,         # heliponto 4 e hospital receptor
        'H2A1_A1_DIST_HELI': 0,           # heliponto 2 e aeroporto 1
        'H3_HR_DIST_HELI'  : 7.41,        # heliponto 3 e hospital receptor
        'HD_H4_DIST_HELI'  : 462.5,       # hospital doador e heliponto 4
        'H1_H4_DIST_HELI'  : 457,         # heliponto 1 e heliponto 4
        
        # Tempos de viagem entre locais
        'FINAL_REM_CORACAO' : 0.5,      # "Finalização remoção coração doador",
        'EMBARQ_1_AMBU_TEMP': 0.02,     # "Embarque 1º ambulância",
        'VIAGEM_1_AMBU_TEMP': 5.755556, # "Viagem 1º ambulância",
        'DESEMB_1_AMBU_TEMP': 0.02,     # "Desembarque 1º ambulância",

        'EMBARQ_1_HELI_TEMP': 0.02,     # "Embarque 1º helicóptero",
        'VIAGEM_1_HELI_TEMP': 0,        # "Viagem 1º helicóptero",
        'DESEMB_1_HELI_TEMP': 0,     # "Desembarque 1º helicóptero",

        'EMBARQ_2_AMBU_TEMP': 0,     # "Embarque 2º ambulância",
        'VIAGEM_2_AMBU_TEMP': 0,     # "Viagem 2º ambulância",
        'DESEMB_2_AMBU_TEMP': 0,     # "Desembarque 2º ambulância",

        # "AVIÃO",
        'EMBARQ_AVIAO_TEMP': 0,     # "Embarque",
        'VIAGEM_AVIAO_TEMP': 0,     # "Viagem",
        'DESEMB_AVIAO_TEMP': 0,     # "Desembarque",

        'EMBARQ_3_AMBU_TEMP': 0,     # "Embarque 3º ambulância",
        'VIAGEM_3_AMBU_TEMP': 0,     # "Viagem 3º ambulância",
        'DESEMB_3_AMBU_TEMP': 0,     # "Desembarque 3º ambulância",

        'EMBARQ_2_HELI_TEMP': 0,     # "Embarque 2º helicóptero",
        'VIAGEM_2_HELI_TEMP': 0,     # "Viagem 2º helicóptero",
        'DESEMB_2_HELI_TEMP': 0,     # "Desembarque 2º helicóptero",

        'EMBARQ_4_AMBU_TEMP': 0,     # "Embarque 4º ambulância",
        'VIAGEM_4_AMBU_TEMP': 0,     # "Viagem 4º ambulância",
        'DESEMB_4_AMBU_TEMP': 0,     # "Desembarque 4º ambulância",

        # "Inicialização implante órgão receptor"
        'INIC_REM_CORACAO' : 0.5,
    },
}

# Velocidades médias (km/h)
velocidades = {'Ambulância': 60, 'Helicóptero': 250, 'Avião': 800}

# Tempos fixos (embarque, desembarque, cirurgia) em horas
tempos_fixos = {'Embarque': 0.5, 'Desembarque': 0.25, 'Cirurgia': 1.5}  # Tempo de cirurgia estimado

# Rotas possíveis (em ordem de preferência, para otimização)
rotas = [
    "Carro",
    "Helicóptero",
    "Carro → Helicóptero",
    "Helicóptero → Carro",
    "Carro → Helicóptero → Carro",
    "Carro → Avião → Carro",
    "Carro → Avião → Helicóptero",
    "Carro → Avião → Carro → Helicóptero",
    "Carro → Avião → Helicóptero → Carro",
    "Carro → Avião → Carro → Helicóptero → Carro",
    # ... (outras rotas)
]

# Função para calcular o tempo de viagem
def calcular_tempo_viagem(distancia, modal):
    if modal not in velocidades:
        raise ValueError(f"Modal de transporte inválido: {modal}")
    return distancia / velocidades[modal]

# Função para calcular o tempo total de uma rota
def calcular_tempo_total(rota, hospital_dados):
    tempo_total = 0
    etapas = rota.split(" → ")
    for i in range(len(etapas) - 1):  
        origem, destino = etapas[i], etapas[i + 1]
        distancia_key = f"{origem}_{destino}_distancia"
        if distancia_key not in hospital_dados:
            raise ValueError(f"Distância não encontrada para {origem} - {destino}")
        distancia = hospital_dados[distancia_key]

        tempo_viagem = calcular_tempo_viagem(distancia, destino) if destino in velocidades else 0
        tempo_total += tempos_fixos['Embarque'] + tempo_viagem + tempos_fixos['Desembarque']

    # Adicionar tempo de cirurgia no final
    tempo_total += tempos_fixos['Cirurgia']
    return tempo_total

# Função para encontrar a rota mais rápida
def encontrar_rota_mais_rapida(hospital_dados, rotas):
    rota_mais_rapida = None
    tempo_minimo = float('inf')
    for rota in rotas:
        try:
            tempo_total = calcular_tempo_total(rota, hospital_dados)
            if tempo_total < tempo_minimo:
                tempo_minimo = tempo_total
                rota_mais_rapida = rota
        except ValueError as e:
            print(f"Erro ao calcular tempo para rota '{rota}': {e}")
    return rota_mais_rapida, tempo_minimo

# Exemplo de uso (Hospital 1)
hospital_escolhido = "Hospital 1"
rota_mais_rapida, tempo_total = encontrar_rota_mais_rapida(hospitais[hospital_escolhido], rotas)
if rota_mais_rapida:
    print(f"A rota mais rápida para o {hospital_escolhido} é: {rota_mais_rapida}, com tempo total de {tempo_total:.2f} horas")
