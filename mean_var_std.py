# Importação da biblioteca
import numpy as np

# Definição da função
def calculate(list):
  # Se a lista tiver 9 entradas
  if len(list) == 9:
    # Transforma a lista em um array do numpy
      list = np.array(list)
    # Transforma numa matriz 3x3
      list.shape = (3, 3)
    # Cria o dicionario
      dictionary = {
          'mean': [(np.mean(list, axis = 0)).tolist(), (np.mean(list, axis = 1)).tolist(), float(np.mean(list))],
          'variance': [(np.var(list, axis = 0)).tolist(), (np.var(list, axis = 1)).tolist(), float(np.var(list))],
          'standard deviation': [(np.std(list, axis = 0)).tolist(), (np.std(list, axis = 1)).tolist(), float(np.std(list))],
          'max': [(np.max(list, axis = 0)).tolist(), (np.max(list, axis = 1)).tolist(), int(np.max(list))],
          'min': [(np.min(list, axis = 0)).tolist(), (np.min(list, axis = 1)).tolist(), int(np.min(list))],
          'sum': [(np.sum(list, axis = 0)).tolist(), (np.sum(list, axis = 1)).tolist(), int(np.sum(list))]
          }
      return dictionary
  else:  
    raise ValueError ("List must contain nine numbers.")
