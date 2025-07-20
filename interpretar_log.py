import json
from collections import defaultdict

def interpretar_log(filename="chronocell_log.json"):
    with open(filename, "r") as f:
        log = json.load(f)
    
    estatisticas = {}
    contadores_decisoes = defaultdict(lambda: defaultdict(int))
    soma_tau = defaultdict(float)
    soma_telomere = defaultdict(float)
    passos = len(log)
    
    for tick_data in log:
        for cell in tick_data["cells"]:
            cid = cell["id"]
            soma_tau[cid] += cell["tau"]
            soma_telomere[cid] += cell["telomere"]
            contadores_decisoes[cid][cell["decision"]] += 1
    
    for cid in soma_tau.keys():
        estatisticas[cid] = {
            "tau_medio": soma_tau[cid] / passos,
            "telomere_medio": soma_telomere[cid] / passos,
            "decisoes": dict(contadores_decisoes[cid])
        }
    
    # Mostrar relatório resumido
    print("Resumo do Log ChronoCell:")
    for cid, stats in estatisticas.items():
        print(f"\nCélula {cid}:")
        print(f"  Tempo subjetivo médio (tau): {stats['tau_medio']:.2f}")
        print(f"  Vitalidade média (telômero): {stats['telomere_medio']:.2f}")
        print("  Decisões:")
        for decisao, freq in stats["decisoes"].items():
            print(f"    {decisao}: {freq} vezes")

if __name__ == "__main__":
    interpretar_log()
