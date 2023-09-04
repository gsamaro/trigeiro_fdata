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

Where `r` is the amount of machines.

# Trigeiro et. al. (1989) datasets

William W Trigeiro, L Joseph Thomas, and John O McClain. Capacitated
lot sizing with setup times. Management science, 35(3):353–366, 1989.
