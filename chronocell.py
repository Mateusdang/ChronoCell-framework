# ChronoCell Framework
# Células Computacionais com Percepção de Passagem do Tempo
# Versão 0.1 - Alpha

import random
import json

class ChronoCell:
    """
    Uma célula computacional com percepção subjetiva do tempo,
    baseada em estímulos e vitalidade (telômero).
    """
    def __init__(self, id, base_clock=1.0, telomere_length=100.0):
        self.id = id
        self.tau = 0.0  # Tempo subjetivo
        self.clock_factor = base_clock
        self.telomere = telomere_length
        self.memory = []

    def perceive_time(self, real_time_passed):
        perceived = real_time_passed * self.clock_factor
        self.tau += perceived
        self.telomere -= perceived * 0.01
        return perceived

    def receive_stimulus(self, intensity):
        self.clock_factor *= (1 + intensity)

    def is_exhausted(self):
        return self.telomere <= 0

    def decide_action(self, task_urgency):
        if self.clock_factor > 1.5 or self.telomere < 20:
            return "prioritize"
        elif self.clock_factor < 0.5:
            return "procrastinate"
        return "normal"

    def serialize(self):
        return {
            "id": self.id,
            "tau": self.tau,
            "clock_factor": self.clock_factor,
            "telomere": self.telomere,
            "memory": self.memory
        }

class ChronoSimulator:
    """
    Simulador de uma rede de ChronoCells
    """
    def __init__(self, num_cells=5):
        self.cells = [ChronoCell(id=i) for i in range(num_cells)]
        self.tick = 0
        self.log = []

    def step(self):
        step_data = {"tick": self.tick, "cells": []}

        for cell in self.cells:
            stimulus = random.uniform(0.0, 0.3)
            urgency = random.uniform(0.0, 1.0)

            cell.receive_stimulus(stimulus)
            perceived = cell.perceive_time(1)
            decision = cell.decide_action(task_urgency=urgency)

            state = {
                "id": cell.id,
                "tau": round(cell.tau, 2),
                "telomere": round(cell.telomere, 2),
                "clock_factor": round(cell.clock_factor, 2),
                "decision": decision
            }
            step_data["cells"].append(state)

        self.log.append(step_data)
        self.tick += 1

    def run(self, steps=50):
        for _ in range(steps):
            self.step()

    def export_log(self, filename="chronocell_log.json"):
        with open(filename, "w") as f:
            json.dump(self.log, f, indent=2)

if __name__ == "__main__":
    sim = ChronoSimulator(num_cells=5)
    sim.run(steps=100)
    sim.export_log()
    print("Simulação concluída. Log exportado para 'chronocell_log.json'.")
