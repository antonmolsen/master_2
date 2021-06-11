# created by Anton Molsen 09 Jun

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

def dataPlot(data):

    # we sort our data from lowest to highest temperature
    data = data[np.argsort(data[:, 0])]

    #first we plot out bacterias in a histogram
    x = [1,2,3,4]

     # y data is the number of each bacteria
    sal = data[(data[:,2] == 1)]
    bac = data[(data[:,2] == 2)]
    lis = data[(data[:,2] == 3)]
    bro = data[(data[:,2] == 4)]
    y = [np.size(sal[:,0]),np.size(bac[:,0]),np.size(lis[:,0]),np.size(bro[:,0])]

    # consistent colors through plot
    c_sal = "navy"
    c_bac = "gold"
    c_lis = "teal"
    c_bro = "tomato"

    plt.bar(x,y,color=[c_sal,c_bac,c_lis,c_bro])
    plt.title("Number of each type of bacteria")
    plt.xlabel("Bacteria")
    plt.ylabel("No. bacteria")
    plt.xticks(x, ["Salmonella \n enterica", "Bacillus \n cereus", "Listeria", "Brochothrix \n thermosphacta"])
    plt.tight_layout()
    plt.show()

    # growth rate by temperature plot

    x_sal = sal[:, 0]
    x_bac = bac[:, 0]
    x_lis = lis[:, 0]
    x_bro = bro[:, 0]
    y_sal = sal[:, 1]
    y_bac = bac[:, 1]
    y_lis = lis[:, 1]
    y_bro = bro[:, 1]

    # plot of data
    plt.plot(x_sal, y_sal, "s",color = c_sal, label = "Salmonella enterica")
    plt.plot(x_bac, y_bac, "d",color = c_bac, label = "Bacillus \ncereus")
    plt.plot(x_lis, y_lis, "o",color = c_lis, label = "Listeria")
    plt.plot(x_bro, y_bro, "*",color = c_bro, label = "Brochothrix \nthermosphacta")

    plt.title("Growth rate vs temperature")
    plt.xlabel("Temperature")
    plt.ylabel("Growth rate")
    plt.ylim([0,1.2])
    plt.legend(loc = "upper left",ncol = 2)
    plt.grid()
    plt.show()
