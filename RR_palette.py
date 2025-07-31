from matplotlib import rcParams
from cycler import cycler

#tailwind_palette = [
#    '#ad7577',  # Old rose
#    '#b9c1f1',  # Periwinkle
#    '#a09bb2',  # Rose quartz
#    '#776158',  # Wenge
#    '#9c5429',  # Brown
#    '#1e1b08'   # Smoky black
#]
tailwind_palette = [
    "#d14b57",  # Old rose
    "#5561f3",  # Periwinkle
    "#8c76da",  # Rose quartz
    "#705149",  # Wenge
    "#b65e1d",  # Brown
    "#262626",  # Smoky black
]

def set_tailwind_palette():
    """
    Apply the Tailwind-inspired palette globally.
    e.g. something like 
    plt.plot(x, y)  
    plt.plot(x, y2)
    will use cyclically colors from the palette.
    """
    rcParams['axes.prop_cycle'] = cycler(color=tailwind_palette)

named_palette = {
    '1': '#ad7577',
    '2': '#b9c1f1',
    '3': '#a09bb2',
    '4': '#776158',
    '5': '#9c5429',
    '6': '#1e1b08'
}

