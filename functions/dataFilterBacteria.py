#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun  8 14:51:11 2021

@author: antonmolsen
"""
import numpy as np
import pandas as pd

def dataFilterBacteria(data,bacteria) :
    arr = np.array(data)
    #bacteria is taken as a string

    if bacteria == "Salmonella enterica" :
        accepted_bacteria = (1 == arr[:, 2])
        bacteria_list = arr[accepted_bacteria]

    elif bacteria == "Bacillus cereus" :
        accepted_bacteria = (2 == arr[:, 2])
        bacteria_list = arr[accepted_bacteria]

    elif bacteria == "Listeria" :
        accepted_bacteria = (3 == arr[:, 2])
        bacteria_list = arr[accepted_bacteria]

    elif bacteria == "Brochothrix thermosphacta" :
        accepted_bacteria = (4 == arr[:, 2])
        bacteria_list = arr[accepted_bacteria]


    return print("you chose",bacteria,": \n",bacteria_list)
