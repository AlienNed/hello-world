import pandas as pd
import matplotlib.pyplot as plt
import tkinter as tk
from tkinter import filedialog
import numpy as np
from scipy.stats import *
from os import system

# TKinter Setup
window = tk.Tk()
window.withdraw()

# VARIABLES
df = []
column_dict = {}
column_counter = 1
col_x_index = []
col_y_index = []
col_x = []
col_y = []

# FUNCTIONS

def load_excel():
    global df
    file_path = filedialog.askopenfilename()
    df = pd.read_excel(file_path)

def define_axis():
    global col_x
    global col_y
    global col_x_index
    global col_Y_index
    global column_counter
    global column_dict
    for row in df:
        column_dict.update({column_counter: row})
        column_counter = column_counter + 1
    for item in column_dict:
        print(str(item) + ' ' + str(column_dict[item]))
    col_x_index = column_dict[int(input('Type index of column for X-axis: '))]
    col_y_index = column_dict[int(input('Type index of column for Y-axis: '))]
    col_x = df[col_x_index]
    col_y = df[col_y_index]

def plot_one_column(x,y):
    slope, intercept, r_value, p_value, std_err = linregress(x, y)
    plt.scatter(x, y)
    plt.xlabel(col_x_index)
    plt.ylabel(col_y_index)
    z = np.polyfit(x, y, 1)
    p = np.poly1d(z)
    plt.plot(x, p(x), "r--")
    plt.grid(alpha=.4, linestyle='--')
    plt.text(x[0], y[0], '   r2 = ' + str(round(pow(r_value, 2), 4)))
    plt.show()

# PROGRAM CONTROL

def program_control():
    x1 = True
    while x1 == True:
        try:
            load_excel()
            x1 = False
        except:
            print('No file- or not a valid file type selected')
            stop = input('press L to load a new file, else press any key to stop: ')
            if stop.lower() == 'l':
                system('cls')
                continue

            else:
                exit()
    define_axis()
    plot_one_column(col_x,col_y)


program_control()

#print(col_x, col_y)