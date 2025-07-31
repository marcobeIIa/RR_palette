This colour palette will fill with joy your wednesday afternoons with the most popular meme of all time!

the image used for the palette is

https://jollycontrarian.com/index.php?title=File:Rickroll.jpg

and I've used the tool from

https://coolors.co/

as a starting point for the palette.


## USAGE
Asssuming my folder structure is something like  

├── RR_palette/
│   └── RR_palette.py             ← contains the color palette
│
└── analysis/
    └── plot_figures.py        ← wants to use the palette

My python code will look something like:

```python
# import sys
import os
import matplotlib.pyplot as plt

# Add parent dir (where RR_palette.py lives) to sys.path
parent_dir = os.path.abspath('../RR_palette') # or whatever!!
if parent_dir not in sys.path:
    sys.path.insert(0, parent_dir)

import RR_palette

RR_palette.set_tailwind_palette()

x = range(10)
for i in range(6):
    y = [xi * (i + 1) for xi in x]
    plt.plot(x, y, label=f"Line {i+1}")

plt.legend()
plt.show()

```

<img width="543" height="413" alt="immagine" src="https://github.com/user-attachments/assets/42c21c0b-0430-42e3-a237-530763c5e3dc" />

[currently the color palette is not representative of the image. will fix]
