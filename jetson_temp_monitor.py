#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# MIT License
#
# Copyright (c) 2019 Tsutomu Furuse
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE. 

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import thermal_zone

NUM_BUF_POINTS = 180
PLOT_INTERVAL = 1000

Data = None

def plot(i, zone_paths, zone_names):
    global Data

    zone_temps = thermal_zone.get_thermal_zone_temps(zone_paths)
    print(zone_temps)
    zone_temps = [t / 1000.0 for t in zone_temps]
    Data = np.append(Data, np.array([zone_temps]), axis = 0)
    if i >= NUM_BUF_POINTS:
        Data = np.delete(Data, 0, axis = 0)
    
    plt.cla()
    plt.plot(Data, marker = 'x')
    plt.xlim(0, NUM_BUF_POINTS)
    plt.ylim(0.0, 90.0)
    plt.title('Jetson Thermal Monitor', fontsize = 14)
    plt.xlabel('Sample', fontsize = 10)
    plt.ylabel('Temperature [C]', fontsize = 10)
    plt.tick_params(labelsize=10)
    plt.grid(True)
    plt.legend(labels = zone_names, loc = 'upper left', fontsize = 10)

def main():
    '''
    Plots real-time temperatures from the Jetson on-module thermal sensors
    '''

    global Data

    zone_paths = thermal_zone.get_thermal_zone_paths()
    zone_names = thermal_zone.get_thermal_zone_names(zone_paths)
    print(zone_names)

    Data = np.empty((0, len(zone_names)), float)

    fig = plt.figure(figsize=(10, 4))
    ani = animation.FuncAnimation(fig, plot, \
        fargs = (zone_paths, zone_names), interval = PLOT_INTERVAL)
    plt.show()

if __name__ == "__main__":
    main()