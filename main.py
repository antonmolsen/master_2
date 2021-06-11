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
        print("data successfully imported.")


    if choice == 2:  # 2 Filter data
        # menuitems
        subMenuItems = np.array(["Filter by bacteria type", "Filter by bounds of growth rate"])
        # 1 Filter by bacteria type
        # 2 Filter by bounds of growth rate

        filter_choice = displayMenu(subMenuItems)

        #choice of filter
        if filter_choice == 1:
            print("you chose bacteria type filter. which bacteria do you wish to research")
            subSubMenuItems = np.array(["Salmonella enterica", "Bacillus cereus", "Listeria", "Brochothrix thermosphacta"])

            chosen_bacteria = displayMenu(subSubMenuItems)
            if chosen_bacteria == 1:
                chosen_bacteria = "Salmonella enterica"
            if chosen_bacteria == 2:
                chosen_bacteria == "Bacillus cereus"
            if chosen_bacteria == 3:
                chosen_bacteria = "Listeria"
            if chosen_bacteria == 4:
                chosen_bacteria = "Brochothrix thermosphacta"

            data = dataFilterBacteria(data,chosen_bacteria)

    if choice == 5:
        quit()




dat = dataLoad("test.txt")