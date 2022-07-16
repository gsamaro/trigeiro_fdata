import pandas as pd
import numpy as np
from dataclasses import dataclass


@dataclass
class LerDados:
    instance: str
    nitems: int
    nperiodos: int
    cap: int
    vt: np.ndarray
    hc: np.ndarray
    st: np.ndarray
    sc: np.ndarray
    d: np.ndarray

    def __init__(self, instance: str):
        self.instance = instance        
        df = pd.read_csv(f"data/{instance}", sep='\t', header=None)
        self.nitems = int(df.iloc[0, 0])
        self.nperiodos = int(df.iloc[0, 1])        
        inicio = 2
        fim = inicio + 1
        self.cap = np.array(df.iloc[inicio:fim, 0], dtype=int)
        inicio, fim = fim, fim + self.nitems
        self.vt = np.array(df.iloc[inicio:fim, 0], dtype=int)
        self.hc = np.array(df.iloc[inicio:fim, 1], dtype=int)
        self.st = np.array(df.iloc[inicio:fim, 2], dtype=int)
        self.sc = np.array(df.iloc[inicio:fim, 3], dtype=int)
        inicio, fim = fim, fim + self.nperiodos       
        self.d = np.array(df.iloc[inicio: fim, :], dtype=int).T        

if __name__ == '__main__':
    ler = LerDados("F1.dat")
    pass