#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun  7 22:15:28 2021

@author: antonmolsen & nicolai kongstad
"""

# we start by importing our modules

import numpy as np

from functions.displayMenu import *
from functions.dataLoad import dataLoad
from functions.dataFilterBacteria import dataFilterBacteria
from functions.dataStatistics import dataStatistics
from functions.dataPlot import dataPlot


# menu items in main menu
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
        data_raw = input("Please enter the file you want to read (remember extension of file)")
        data = dataLoad(data_raw)
        print("data successfully imported. ")
        break

    if choice == 2:  # 2 Filter data
        filter_choice = input("What do you wish to filter?")
        # menuitems
        subMenuItems =


dat = dataLoad("test.txt")
