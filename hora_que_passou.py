import math as mm

signal_power = 10
noise_power = 30
ratio = signal_power / noise_power
decibels = 10 * mm.log10(ratio)
radians = 0.7
height = mm.sin(radians)
print(height,ratio)