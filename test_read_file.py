from read_file import LerDados
import numpy as np


def test_ler_dados_F1():
    data = LerDados("F1.dat")
    assert data.nitems == 6
    assert data.nperiodos == 15
    assert data.cap == 728
    assert np.all(data.vt == np.all(np.array([1, 1, 1, 1, 1, 1])))
    assert np.all(data.hc == np.array([5, 3, 2, 3, 2, 4]))
    assert np.all(data.st == np.array([40, 50, 20, 40, 30, 30]))
    assert np.all(data.sc == np.array([1000, 600, 400, 1000, 400, 400]))
    assert data.d[0, 0] == 108
    assert data.d[-1, -1] == 103


def test_ler_dados_G73():
    data = LerDados("G73.dat")
    assert data.nitems == 24
    assert data.nperiodos == 30
    assert data.cap == 3016
    assert data.vt.sum() == 24
    assert data.hc[0] == 1
    assert data.hc[-1] == 2
    assert data.st[0] == 10
    assert data.st[-1] == 50
    assert data.sc[0] == 400
    assert data.sc[-1] == 800
    assert data.d[0, 0] == 0
    assert data.d[-1, -1] == 97
