import pandas as pd
import matplotlib.pyplot as plt
import tkinter as tk
from tkinter import filedialog
import numpy as np
from scipy.stats import *

### TKinter Setup ###
window = tk.Tk()
window.withdraw()

### Open Excel file ###
x = True
while x == True:
    try:
        file_path = filedialog.askopenfilename()
        df = pd.read_excel(file_path)
        x = False
    except Exception:
        print('Not a valid file!')
        stop = input('press C to continue, else press any key to stop: ')
        if stop.lower() == 'c':
            continue
        else:
            exit()

### Variables ###

column_dict = {}
column_counter = 1

### Functions ###

for row in df:
    column_dict.update({column_counter:row})
    column_counter = column_counter+1

for item in column_dict:
    print(str(item) + ' '+ str(column_dict[item]))

x2 = True
while x2 == True:
    try:
        col_x_index = column_dict[int(input('Type index of column for X-axis: '))]
        col_y_index = column_dict[int(input('Type index of column for Y-axis: '))]
        col_x = df[col_x_index]
        col_y = df[col_y_index]
        x2 = False
    except Exception:
        print('Not valid columns!')

def PlotOneColumn(x,y):
    slope, intercept, r_value, p_value, std_err = linregress(x, y)
    plt.scatter(x,y)
    plt.xlabel(col_x_index)
    plt.ylabel(col_y_index)
    z = np.polyfit(x,y,1)
    p = np.poly1d(z)
    plt.plot(x,p(x),"r--")
    plt.grid(alpha=.4, linestyle='--')
    plt.text(x[0],y[0],'  r2 = ' + str(round(pow(r_value,2),4)))
    plt.show()

x3 = True
while x3 == True:
    try:
        PlotOneColumn(col_x, col_y)
        x3 = False
    except Exception as e:
        print(e)