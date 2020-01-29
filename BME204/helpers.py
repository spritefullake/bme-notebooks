from math import *
# Rounds to the correct number of sig figs
def sig(x, figs=3): 
    return round(x, -int(floor(log10(x))) + (figs - 1))