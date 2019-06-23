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

import os
import re
import subprocess

THERMAL_PATH = '/sys/devices/virtual/thermal/'

def get_thermal_zone_paths():
    '''
    Returns a list of the thermal zone paths
    '''
    return [os.path.join(THERMAL_PATH, m.group(0)) \
        for m in [re.search('thermal_zone[0-9]', d) \
            for d in os.listdir(THERMAL_PATH)] if m]

def read_sys_value(pth):
    return(subprocess.check_output(['cat', pth]).decode('utf-8').rstrip('\n'))

def get_thermal_zone_names(zone_paths):
    '''
    Gets the thermal zone names from
    /sys/devices/virtual/thermal/thermal_zone[0-9]/type
    '''
    return([read_sys_value(os.path.join(p, 'type')) for p in zone_paths])

def get_thermal_zone_temps(zone_paths):
    '''
    Gets the thermal zone temperature values from
    /sys/devices/virtual/thermal/thermal_zone[0-9]/temp
    '''
    return([int(read_sys_value(os.path.join(p, 'temp'))) for p in zone_paths])

def main():
    ''' Test program '''
    zone_paths = get_thermal_zone_paths()
    zone_names = get_thermal_zone_names(zone_paths)
    print(zone_names)
    zone_temps = get_thermal_zone_temps(zone_paths)
    print(zone_temps)

if __name__ == "__main__":
    main()
