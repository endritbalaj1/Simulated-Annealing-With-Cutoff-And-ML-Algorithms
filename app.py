from models import Parser
from models import Solver


import os
import time
import multiprocessing
# import tkinter as tk
# from tkinter import messagebox

solver = Solver()

directory = os.listdir('input')

print("---------- Simulated Annealing With Cutoff And ML Algorithms----------")
for file in directory:
    if file.endswith('.txt'):
        parser = Parser(f'./input/{file}')
        data = parser.parse()
        score, solution = solver.simulated_annealing_with_cutoff_and_ml_algorithms(data, total_time_ms=2000)

        solution.export(f'./output/{file}')
        print(f'Final score: {score:,}')
        print(f'Solution exported to ./output/{file}')

input_folder = './input'
output_folder = './output'  
os.makedirs(output_folder, exist_ok=True)
