#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun  7 22:15:28 2021

@author: antonmolsen
"""

# we start by importing our modules
from functions.displayMenu import displayMenu
import numpy as np

from functions.dataLoad import dataLoad
from functions.dataFilterBacteria import dataFilterBacteria
from functions.dataStatistics import dataStatistics
from functions.dataPlot import dataPlot

menuItems = np.array(["Load data", "Filter data", "Show statistics", "Generate plot", "Exit"])
# 1 Load data
# 2 Filter data
# 3 Show Statistics
# 4 Generate Plot
# 5 Exit

while True:
    choice = displayMenu(menuItems)

    # menu item chosen
    if choice == 1:
        # load data from txt
        data = input("Please enter the file you want to read (remember extension of file)")


dat = dataLoad("test.txt")

dataPlot(dat)

print(dataFilterBacteria(dat, "Brochothrix thermosphacta"))
