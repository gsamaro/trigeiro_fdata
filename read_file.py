import pandas as pd
import numpy as np
from dataclasses import dataclass
import re


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
        self._instance = f"data/{instance}"
        sep = self._detect_delimiter()
        column_names = self._generate_cols(sep=sep)
        df = pd.read_csv(self._instance, sep=sep, header=None, lineterminator="\n", engine="c", names=column_names)
        self.nitems = int(df.iloc[0, 0])
        self.nperiodos = int(df.iloc[0, 1])        
        inicio = 2
        fim = inicio + 1
        self.cap = np.array(df.iloc[inicio:fim, 0].astype(float), dtype=int)
        inicio, fim = fim, fim + self.nitems
        self.vt = np.array(df.iloc[inicio:fim, 0].astype(float), dtype=int)
        self.hc = np.array(df.iloc[inicio:fim, 1].astype(float), dtype=int)
        self.st = np.array(df.iloc[inicio:fim, 2].astype(float), dtype=int)
        self.sc = np.array(df.iloc[inicio:fim, 3].astype(float), dtype=int)
        inicio, fim = fim, fim + self.nperiodos   
        if self.nitems <= 15:    
            self.d = np.array(df.iloc[inicio:fim, :].astype(float), dtype=int).T
        else:
            demanda_sup = np.array(df.iloc[inicio:fim, :].astype(float), dtype=int)
            inicio, fim = fim, fim + self.nperiodos  
            demanda_inf = np.array(df.iloc[inicio:fim, :].replace("\r", np.nan).dropna(axis=1).astype(float), dtype=int)
            self.d = np.append(demanda_sup, demanda_inf, axis=1).T

    def _detect_delimiter(self) -> str:
        with open(self._instance) as f:
            line_splitted = re.split("\t", f.readline())
        if len(line_splitted) > 1:
            return "\t"
        else:
            return r"\s+"
    
    def _generate_cols(self, sep: str) -> list:
        with open(self._instance, "r", encoding="utf-8") as temp_f:
            col_count = [len(re.split(sep, l.strip())) for l in temp_f.readlines()]
        column_names = [i for i in range(max(col_count))] 
        return column_names

if __name__ == '__main__':
    ler = LerDados("G73.dat")
    pass