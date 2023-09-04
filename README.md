# Install

```pip install -r requirements.txt```

# Usage

For a single machine instance:

```
from read_file import LerDados

data = LerDados("F1.dat")
```

For parallel machine instance:

```
from read_file import DataCs

data = DataCs("F1.dat", r=3)
```

Note that:

$cs_{itk} = (vc_{it} + \sum\limits_{u=t}^{T} hc_{iu})d_{ik}\quad\forall i=1,\dots,n,\quad\forall t=1,\dots,T\quad\forall k=1,\dots,T$

Where `r` is the amount of machines.

And `vt` is zero by default.

# Trigeiro et. al. (1989) datasets

William W Trigeiro, L Joseph Thomas, and John O McClain. Capacitated
lot sizing with setup times. Management science, 35(3):353–366, 1989.
