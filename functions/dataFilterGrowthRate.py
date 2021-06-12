#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun  8 14:51:11 2021

@author: antonmolsen
"""
import numpy as np
import pandas as pd


def dataFilterGrowthRate(data, lowerBound, upperBound):
    # Takes the current data array and sorts it by what is inputtet as
    # acceptable upper and lower bounds. Returns the sortet array.

    growth_collumn = np.array(data)[:, 1]

    accepted_rates = (np.array(data)[:, 1] > lowerBound) & (np.array(data)[:, 1] < upperBound)

    growth_rate_in_interval = data[accepted_rates]

    return growth_rate_in_interval
