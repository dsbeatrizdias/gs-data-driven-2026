# ============================================================
# Global Solutions 2026 - 1º Semestre
# Disciplina: Data Driven Application & Data Science
# Integrantes:
#   - Ana Julia Santos Amorim
#   - Beatriz Dias da Silva (Representante)
# ============================================================

tipos_eventos  = []
paises         = []
regioes        = []
cidades        = []
areas_afetadas = []
intensidades   = []
ocorrencias    = []

while True:
    try:
        n = int(input("Insira a quantidade de eventos: "))
        if n > 0:
            break
        else:
            print("  A quantidade deve ser maior que zero.")
    except ValueError:
        print("  Digite um numero inteiro valido.")

for i in range(1, n + 1):
    print(f"\n--- Evento {i} ---")

    while True:
        tipo = input("Tipo (ex: desmatamento, queimadas): ").strip()
        if tipo:
            break
        print("  O tipo nao pode ser vazio.")

    while True:
        pais = input("Pais: ").strip()
        if pais:
            break
        print("  O pais nao pode ser vazio.")

    while True:
        regiao = input("Regiao: ").strip()
        if regiao:
            break
        print("  A regiao nao pode ser vazia.")

    while True:
        cidade = input("Cidade: ").strip()
        if cidade:
            break
        print("  A cidade nao pode ser vazia.")

    while True:
        try:
            area = float(input("Area afetada (km2): "))
            if area > 0:
                break
            else:
                print("  A area deve ser maior que zero.")
        except ValueError:
            print("  Digite um numero valido para a area.")

    while True:
        try:
            intensidade = int(input("Intensidade (1 a 10): "))
            if 1 <= intensidade <= 10:
                break
            else:
                print("  A intensidade deve estar entre 1 e 10.")
        except ValueError:
            print("  Digite um numero inteiro entre 1 e 10.")

    while True:
        try:
            num_ocorrencias = int(input("Numero de ocorrencias: "))
            if num_ocorrencias > 0:
                break
            else:
                print("  O numero de ocorrencias deve ser maior que zero.")
        except ValueError:
            print("  Digite um numero inteiro valido.")

    tipos_eventos.append(tipo)
    paises.append(pais)
    regioes.append(regiao)
    cidades.append(cidade)
    areas_afetadas.append(area)
    intensidades.append(intensidade)
    ocorrencias.append(num_ocorrencias)

total_eventos = len(tipos_eventos)
soma_areas = sum(areas_afetadas)
media_intensidade = sum(intensidades) / total_eventos
idx_maior_area = areas_afetadas.index(max(areas_afetadas))
idx_maior_oc = ocorrencias.index(max(ocorrencias))

soma_densidades = 0.0
for oc, ar in zip(ocorrencias, areas_afetadas):
    soma_densidades += oc / ar
densidade_media = soma_densidades / total_eventos

eventos_acima_media = 0
for intensidade in intensidades:
    if intensidade > media_intensidade:
        eventos_acima_media += 1

idx_critico = 0
for i in range(1, total_eventos):
    if intensidades[i] > intensidades[idx_critico]:
        idx_critico = i
    elif intensidades[i] == intensidades[idx_critico]:
        if areas_afetadas[i] > areas_afetadas[idx_critico]:
            idx_critico = i

print("\n" + "=" * 40)
print("        RELATORIO DE ANALISE")
print("=" * 40)
print(f"\nTotal de eventos registrados: {total_eventos}")
print("\n" + "-" * 40)
print("Resumo Geral")
print("-" * 40)
print(f"Area total afetada: {soma_areas:.0f} km2")
print(f"Media de intensidade: {media_intensidade:.1f}")
print("\n" + "-" * 40)
print("Analises")
print("-" * 40)
print(f"Regiao com maior numero de ocorrencias: {regioes[idx_maior_oc]}")
print(f"Quantidade de eventos acima da media de intensidade: {eventos_acima_media}")
print(f"Densidade media de ocorrencias: {densidade_media:.2f} ocorrencias/km2")
print("\n" + "-" * 40)
print("Evento Mais Critico")
print("-" * 40)
print(f"Tipo: {tipos_eventos[idx_critico]}")
print(f"Local: {cidades[idx_critico]}, {regioes[idx_critico]}, {paises[idx_critico]}")
print(f"Intensidade: {intensidades[idx_critico]}")
print(f"Area afetada: {areas_afetadas[idx_critico]:.0f} km2")
print("\n" + "=" * 40)
print(f"Total de desastres registrados: {total_eventos}")