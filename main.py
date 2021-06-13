#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun  7 22:15:28 2021

@author: antonmolsen & nicolai kongstad
"""

#modules import
import numpy as np
import matplotlib as plt
from functions.displayMenu import *
from functions.dataLoad import dataLoad
from functions.dataFilterBacteria import dataFilterBacteria
from functions.dataFilterGrowthRate import dataFilterGrowthRate
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
    try:
        if choice>1 and (np.size(data) == 0):
            raise
        # menu item chosen
        if choice == 1:
            # load data from txt
            while True:
                try:
                    dataTemp=input(
                        "Please enter the file you want to read (remember extension of file)")
                    if dataTemp == '':
                        print('Returning to menu.')
                        break
                    data = dataLoad(dataTemp)[0]
                    org_data = dataLoad(dataTemp)[1] # for removal of filters, we go back to this original data set
                    print('Errornous data removed.')
                    break
                except FileNotFoundError:
                    print('File could not be found.')

        if choice == 2:  # 2 Filter data
            # menuitems
            subMenuItems=np.array(["Filter by bacteria type", "Filter by bounds of growth rate","Remove Filters"])
            # 1 Filter by bacteria type
            # 2 Filter by bounds of growth rate

            filter_choice=displayMenu(subMenuItems)

            # choice of filter
            if filter_choice == 1:
                print("you chose bacteria type filter. which bacteria do you wish to research")
                subSubMenuItems=np.array(
                    ["Salmonella enterica", "Bacillus cereus", "Listeria", "Brochothrix thermosphacta"])

                chosen_bacteria = displayMenu(subSubMenuItems)
                if chosen_bacteria == 1:
                    chosen_bacteria = "Salmonella enterica"
                if chosen_bacteria == 2:
                    chosen_bacteria == "Bacillus cereus"
                if chosen_bacteria == 3:
                    chosen_bacteria = "Listeria"
                if chosen_bacteria == 4:
                    chosen_bacteria = "Brochothrix thermosphacta"

                data = dataFilterBacteria(data, chosen_bacteria)

            if filter_choice == 2:
                lowerBound = float(input("Please enter the lower bound"))
                upperBound = float(input("Please enter the upper bound"))

                data = dataFilterGrowthRate(data, lowerBound, upperBound)

            if filter_choice == 3: # remove filters
                data = org_data
                print("Filters removed succesfully")

        if choice == 3:  # show statistics
            statMenuItems = np.array(["Mean Temperature", "Mean Growth rate", "Std Temperature",
                                      "Std Growth rate", "Rows", "Mean Cold Growth rate", "Mean Hot Growth rate"])
            statChoice = int(displayMenu(statMenuItems))
            print("The {} is {}.".format(statMenuItems[statChoice - 1], dataStatistics(data, statChoice)))

        if choice == 4:
           dataPlot(data)
           print("Plots created succesfully")

        if choice == 5:
           break
    except:
        print('Please load data before researching data')
