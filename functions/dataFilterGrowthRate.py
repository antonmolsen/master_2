#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun  8 14:51:11 2021

@author: antonmolsen
"""
import numpy as np
import pandas as pd

import numpy as np
def dataFilterGrowthRate(data, lowerBound, upperBound):
    growth_collumn = np.array(data)[:,1]

    accepted_rates = (growth_collumn > lowerBound) & (growth_collumn < upperBound)

    growth_rate_in_interval = growth_collumn[accepted_rates]

    return growth_rate_in_interval







