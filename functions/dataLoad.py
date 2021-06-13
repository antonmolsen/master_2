#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jun  6 17:48:37 2021

@author: antonmolsen
"""

# dataLoad("test.txt")


import numpy as np
import pandas as pd


def dataLoad(filename):
    # The function loads in the data as a numpy array. The data is then
    # filtered so known bad data is removed.

    # inital condition is that the data is accepted
    data = [0, 0, 0]
    read = True

   # we read in our data
    temp_file = pd.read_csv(filename, header=None, delim_whitespace=True,
                            dtype=float)  # delimiter is whitespace

    arr = np.array(temp_file)  # numpy array, every row is true

    for i in range(len(arr[:, 1])):  # length of dataset
        if len(np.array(arr)[i, :]) == 3:  # only use rows with 3 elements

            # temperature boundary in 0'th collumn
            if 10 >= np.array(arr)[i, 0] or np.array(arr)[i, 0] >= 60:
                read = False
                print("Error in temperature in line", i+1, ", data removed")

            if np.array(arr)[i, 1] < 0:  # growth rate in 1'st collumn
                read = False
                print("Error in growth rate in line", i+1, ", data removed")

            if 1 > np.array(arr)[i, 2] or np.array(arr)[i, 2] > 4:
                read = False
                print("Error in bacteria class in line", i+1, ", data removed")

            if read:  # understand this as it is not NOT read, so therefore it is read
                # we then stack i'th array on to the datastack
                data = np.vstack((data, arr[i]))

            read = True  # we reset all to true when false ones arent read

        else:  # if faulty row, it responds here
            print("Error in line", i+1, ", not enough information")

    data = np.delete(data, 0, axis=0)  # removal of inital [0,0,0] array
    org_data = data

    return data, org_data
