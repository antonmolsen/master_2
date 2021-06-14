import numpy as np
import pandas as pd


def dataFilterGrowthRate(data, lowerBound, upperBound):
    # Takes the current data array and sorts it by what is inputted as
    # acceptable upper and lower bounds. Returns the sorted array.

    accepted_rates = (np.array(data)[:, 1] > lowerBound) & (np.array(data)[:, 1] < upperBound)

    growth_rate_in_interval = data[accepted_rates]

    return growth_rate_in_interval
