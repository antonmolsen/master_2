#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun  8 14:51:11 2021

@author: antonmolsen
"""
import numpy as np
import pandas as pd


def dataFilterBacteria(data, bacteria):
    # The function takes the name of a bateria and returns the data set with
    # every other bacteria sorted out. If the specified bateria isn't correct
    # then it returns false.

    arr = np.array(data)

    if bacteria == "Salmonella enterica":
        accepted_bacteria = (1 == arr[:, 2])
        bacteria_list = arr[accepted_bacteria]

    elif bacteria == "Bacillus cereus":
        accepted_bacteria = (2 == arr[:, 2])
        bacteria_list = arr[accepted_bacteria]

    elif bacteria == "Listeria":
        accepted_bacteria = (3 == arr[:, 2])
        bacteria_list = arr[accepted_bacteria]

    elif bacteria == "Brochothrix thermosphacta":
        accepted_bacteria = (4 == arr[:, 2])
        bacteria_list = arr[accepted_bacteria]

    else:
        bacteria_list = False

    return bacteria_list
