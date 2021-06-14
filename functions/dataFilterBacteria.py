import numpy as np
import pandas as pd


def dataFilterBacteria(data, bacteria):  # bacteria is str
    # The function takes the name of a bateria and returns the data set with
    # every other bacteria sorted out. If the specified bateria isn't correct
    # then it returns false.

    arr = np.array(data)
    bacteria_list = [0, 0, 0]

    for i in '1234':
        if i in bacteria:
            accepted_bacteria = (int(i) == arr[:, 2])
            bacteria_list = np.vstack((bacteria_list, arr[accepted_bacteria]))

    bacteria_list = np.delete(bacteria_list, 0, axis=0)  # removal of initial [0,0,0]-array

    return bacteria_list
