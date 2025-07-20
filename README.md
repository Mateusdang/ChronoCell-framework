# ChronoCell Framework 🧬🕒

**ChronoCell** é um simulador computacional inspirado em células biológicas que percebem o tempo de forma subjetiva. Ele combina conceitos de **biologia celular**, **física do tempo (relatividade)** e **computação simbólica**, resultando em um sistema adaptativo capaz de simular urgência, procrastinação e envelhecimento computacional.

---

## Princípios Científicos Fundamentais

- **Relatividade Temporal:** O tempo subjetivo pode acelerar ou desacelerar conforme o estado da célula e estímulos externos.
- **Cronobiologia:** Células e organismos possuem ritmos internos que modulam processos biológicos e comportamentais.
- **Envelhecimento Celular:** O conceito de telômeros é utilizado para modelar a vitalidade e a longevidade computacional da célula.

## 🧠 Conceito

Cada "célula computacional" possui: `ChronoCell` 
- Um **relógio interno subjetivo (τ)**;
- Um **estado de vitalidade** (semelhante a telômeros);
- Um mecanismo de **percepção temporal variável**;
- Capacidade de **tomar decisões** baseadas em estímulo, urgência e vitalidade.

---

- **Atributos:**
  - `tau`: Tempo subjetivo acumulado.
  - `clock_factor`: Fator que modifica a percepção do tempo (aceleração/desaceleração).
  - `telomere`: Medida da vitalidade/restante da célula.
  - `memory`: Histórico simbólico de estímulos ou decisões.

- **Métodos:**
  - `perceive_time(real_time_passed)`: Atualiza o tempo subjetivo e diminui vitalidade.
  - `receive_stimulus(intensity)`: Modula o relógio interno baseado em estímulos.
  - `decide_action(task_urgency)`: Decide prioridade da ação baseado na percepção temporal e urgência.
  - `is_exhausted()`: Verifica se a célula está "morta" (telômeros esgotados).

### ChronoSimulator

- Simula uma rede de ChronoCells em ticks de tempo discreto.
- Aplica estímulos randômicos e urgência variável para cada célula.
- Registra estado e decisões em log JSON para análise posterior.

---

## 🚀 Como usar

### Baixe Esse Repositorio
```bash
git clone https://github.com/Mateusdang/ChronoCell-framework.git
```

```bash
cd ChronoCell-framework

```
### Inicio
```bash
python chronocell.py
```

### Veja Os Dados Gerado
```bash
python interpretar_log.py
```

## 📂 Estrutura
- `chronocell.py`: Código principal
- `chronocell_log.json`: Saída gerada após a execução
- `interpretar_log.py`:  Interpretador de Saidas
- `README.md`:
- `LICENSE`: Licença do projeto (MIT)
- `requirements.txt`: Dependências

---

**Possíveis Extensões e Aplicações**

- Avatares em jogos e simulações: NPCs que "sentem" o tempo passar de formas únicas, influenciando decisões, procrastinação e envelhecimento.
- Sistemas sociais adaptativos: Modelar grupos com ritmos individuais, permitindo estudos de dinâmicas coletivas sob percepção temporal variável.
- IA e robótica: Agentes que priorizam tarefas baseados em percepção subjetiva da urgência e desgaste computacional.
- Visualização avançada: Integrar com visualizadores 3D para mapear o tempo subjetivo como deformações espaciais, aproximando-se de modelos de cristalografia sináptica.

**Arquitetura de Desenvolvimento**

- Código modular para fácil extensão das células e mecanismos de decisão.
- Registro completo em JSON para auditoria, análise estatística e integração com outras ferramentas.
- Facilmente integrável com frameworks de IA, jogos e simulações em Python.


# ChronoCell Log Interpreter

Este script (`interpretar_log.py`) faz parte do projeto **ChronoCell — Células Computacionais com Percepção de Passagem do Tempo**. Ele serve como uma ferramenta para interpretar o arquivo de log `chronocell_log.json` gerado pela simulação do sistema.

## 📄 Objetivo

Fornecer um resumo legível do comportamento das células simuladas:
- **Tempo subjetivo médio (`tau`)**
- **Vitalidade média (`telômero`)**
- **Frequência das decisões tomadas** (`prioritize`, `procrastinate`, `normal`)

## 📦 Estrutura Esperada do Log

O arquivo `chronocell_log.json` deve conter uma lista de registros por "tick" (passo de tempo), e em cada registro há dados de todas as células vivas naquele momento:

```json
[
  {
    "tick": 0,
    "cells": [
      {"id": 0, "tau": 0.75, "telomere": 0.95, "decision": "normal"},
      {"id": 1, "tau": 0.68, "telomere": 0.98, "decision": "prioritize"}
    ]
  },
  ...
]
```

## 🧪 O que o script faz

1. **Lê o JSON de log**
2. **Agrupa os dados por célula**
3. **Calcula médias de `tau` e `telômero`**
4. **Conta quantas vezes cada tipo de decisão foi tomada**
5. **Imprime um resumo formatado para cada célula**

## 📊 Exemplo de saída

```
Resumo do Log ChronoCell:

Célula 0:
  Tempo subjetivo médio (tau): 0.76
  Vitalidade média (telômero): 0.91
  Decisões:
    prioritize: 8 vezes
    normal: 11 vezes
    procrastinate: 1 vezes
```

## ⚙️ Estrutura básica de uma célula ChronoCell

```python
class ChronoCell:
    def __init__(self, id, base_clock=1.0, telomere_length=100.0):
        self.id = id
        self.tau = 0.0  # Tempo subjetivo
        self.clock_factor = base_clock  # Modulado por estímulos
        self.telomere = telomere_length  # Vitalidade
        self.memory = []

    def perceive_time(self, real_time_passed):
        perceived = real_time_passed * self.clock_factor
        self.tau += perceived
        self.telomere -= perceived * 0.01  # Envelhecimento
        return perceived

    def receive_stimulus(self, intensity):
        # Aumenta a aceleração do tempo subjetivo
        self.clock_factor *= (1 + intensity)

    def is_exhausted(self):
        return self.telomere <= 0

    def decide_action(self, task_urgency):
        # Se tempo subjetivo está acelerado ou telômero baixo → age rápido
        if self.clock_factor > 1.5 or self.telomere < 20:
            return "prioritize"
        elif self.clock_factor < 0.5:
            return "procrastinate"
        return "normal"
```

---

## 🧬 Simulação de um Microssistema com Várias ChronoCells

```python
cells = [ChronoCell(id=i) for i in range(5)]

for t in range(100):
    for cell in cells:
        stimulus = random.uniform(0.0, 0.3)
        cell.receive_stimulus(stimulus)
        perceived = cell.perceive_time(1)
        decision = cell.decide_action(task_urgency=random.uniform(0.0, 1.0))

        print(f"Célula {cell.id} | τ={cell.tau:.2f} | Telômero={cell.telomere:.2f} | Ação: {decision}")

        if cell.is_exhausted():
            print(f"Célula {cell.id} esgotou-se!")
```

---


## ▶️ Como usar

Certifique-se de ter o Python instalado e execute no terminal:

```bash
python interpretar_log.py
```

O arquivo `chronocell_log.json` precisa estar no mesmo diretório.

## 📈 Extensões possíveis

- Exportar os dados interpretados para CSV
- Visualizações com matplotlib ou Streamlit
- Dashboard em tempo real para acompanhar simulações
- Análise histórica por célula

## 📁 Arquivos necessários

- `interpretar_log.py`: Script analisador
- `chronocell_log.json`: Arquivo de entrada gerado pela simulação principal


## Referências

- Einstein, A. (1905). Sobre a eletrodinâmica dos corpos em movimento.
- López-Otín, C., et al. (2013). The Hallmarks of Aging. Cell.
- Refinetti, R., Lissen, G., & Halberg, F. (2007). Procedures for numerical analysis of circadian rhythms. Biological Rhythm Research.
- Relógios Biológicos Internos

Células Cronológicas ou Relógios Celulares Resumidamente

No campo da biologia, os relógios celulares são mecanismos moleculares complexos presentes nas células de quase todos os seres vivos. Eles regulam os ritmos biológicos, que são as flutuações cíclicas de processos fisiológicos e comportamentais. O exemplo mais conhecido é o ritmo circadiano, um ciclo de aproximadamente 24 horas que influencia o sono, a alimentação, a temperatura corporal, a produção hormonal e muitos outros processos.

Esses relógios são compostos por um conjunto de genes (os genes relógio) e proteínas que interagem em um ciclo de feedback. Eles respondem a sinais externos, como a luz (o "marcador de tempo" mais importante), ajustando o corpo aos ciclos diários do ambiente.

**Funções:**

Regulação do sono e vigília: Ditando quando nos sentimos sonolentos ou alertas.

Hormônios: Controlando a liberação de hormônios como o cortisol e a melatonina.

Metabolismo: Influenciando a digestão e o uso de energia.

Função imune: Afetando a atividade do sistema imunológico.

Envelhecimento: Desempenham um papel crucial no processo de envelhecimento e na saúde geral.

**Relógios Epigenéticos e Idade Biológica**

Em outro contexto, o termo "relógio celular" pode se referir a relógios epigenéticos, que são ferramentas científicas que estimam a idade biológica de uma pessoa ou célula. Ao contrário da idade cronológica (quantos anos você viveu), a idade biológica reflete o "desgaste" das suas células e tecidos, influenciado por fatores genéticos, estilo de vida (dieta, exercícios) e ambiente.


Esses relógios analisam padrões de metilação do DNA, que são modificações químicas no DNA que não alteram a sequência genética, mas influenciam a expressão dos genes. Certos padrões de metilação são associados ao envelhecimento e podem ser usados para estimar se as células de uma pessoa estão "envelhecendo" mais rápido ou mais devagar do que sua idade cronológica. O comprimento dos telômeros (estruturas nas extremidades dos cromossomos que encurtam com a idade) também é um indicador de idade biológica.

**Funções:**

Pesquisa sobre o envelhecimento: Ajudam a entender o que causa o envelhecimento e como intervenções podem afetá-lo.

Avaliação de saúde: Podem ser usados como um indicador da saúde geral e do risco de doenças relacionadas à idade.

Aplicações forenses: Em alguns casos, podem estimar a idade de um indivíduo a partir de amostras biológicas.

Em resumo, enquanto os relógios biológicos internos são os sistemas que mantêm o tempo dentro das nossas células e corpos, os relógios epigenéticos são ferramentas que medem a idade dessas células com base em marcadores moleculares.


## Autor

Desenvolvido por **Mateus Dang**  
[GitHub: @Mateusdang](https://github.com/Mateusdang)

## 📜 Licença

Este projeto está licenciado sob a Licença MIT. Veja o arquivo `LICENSE` para mais detalhes.