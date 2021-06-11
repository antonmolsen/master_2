#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun  7 14:10:39 2021

@author: antonmolsen
"""
import numpy as np
import pandas as pd

def dataStatistics(data, statistic):
    
    data = np.array(data)
    
    temp = data[:,0]
    g_rate = data[:,1]
    bacteria = data[:,2]
    
    if statistic == "Mean Temperature":
        result = np.mean(temp)
        
    elif statistic == "Mean Growth rate":
        result = np.mean(g_rate)
    
    elif statistic == "Std Temperature":
        result = np.std(temp, dtype=np.float64) 
        
    elif statistic == "Std Growth rate":
        result = np.std(g_rate, dtype=np.float64)
    
    elif statistic == "Rows":
        #no. rows
        result = len(data[:,0])
        
    elif statistic == "Mean Cold Growth rate":
        #degree <20
        accepted_data = (data < 20) #boolian argument
        
        result = np.mean(data[accepted_data])
    
    elif statistic == "Mean Hot Growth rate":
        #degree 50<
        accepted_data = (data > 50) #boolian argument
        
        result = np.mean(data[accepted_data])
    
    # statement to return if none of above is accepted?
    
    return result