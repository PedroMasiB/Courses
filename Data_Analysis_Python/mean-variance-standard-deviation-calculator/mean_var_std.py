import numpy as np


def calculate(list):
  if len(list) != 9:
    print("List must contain nine numbers.")
    return ValueError

  n_arr = np.array(list).reshape(3, 3)
  print(n_arr)
  calculations = {
      'mean':
      [n_arr.mean(axis=0).tolist(),
       n_arr.mean(axis=1).tolist(),
       n_arr.mean()],
      'variance':
      [n_arr.var(axis=0).tolist(),
       n_arr.var(axis=1).tolist(),
       n_arr.var()],
      'standard deviation':
      [n_arr.std(axis=0).tolist(),
       n_arr.std(axis=1).tolist(),
       n_arr.std()],
      'max':
      [n_arr.max(axis=0).tolist(),
       n_arr.max(axis=1).tolist(),
       n_arr.max()],
      'min':
      [n_arr.min(axis=0).tolist(),
       n_arr.min(axis=1).tolist(),
       n_arr.min()],
      'sum':
      [n_arr.sum(axis=0).tolist(),
       n_arr.sum(axis=1).tolist(),
       n_arr.sum()]
  }

  return calculations
