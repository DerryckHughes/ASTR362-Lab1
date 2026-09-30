import matplotlib.pyplot as plt
import numpy as np
import glob

def sixteen_to_twelve_correction(sixteen_bit_image):
    return sixteen_bit_image / 16 + 1