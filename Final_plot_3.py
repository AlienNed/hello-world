import pandas as pd
import matplotlib.pyplot as plt
import tkinter as tk
from tkinter import filedialog
import numpy as np
from scipy.stats import *

### TKinter Setup ###
window = tk.Tk()
window.withdraw()

### Variables ###

df = []

### Functions ###

def excel():
    global df
    file_path = filedialog.askopenfilename()
    df = pd.read_excel(file_path)

def list_columns(data):
    column_dict = {}
    counter = 1
    for row in data:
        print(str(counter) + ' ' + str(row))
        column_dict.update({counter:row})
        counter= counter + 1

def column_pick(data):
    col_dict = {}
    counter = 1
    for row in data:
        col_dict.update({counter:row})
        counter= counter + 1
    index = int(input('Choose a column: '))
    return col_dict[index]

def sorted_df(data):
    global df
    print('Columns available as identifiers: ')
    list_columns(data)
    chosen_column = data[column_pick(data)]
    uniq_list = list(chosen_column.unique())
    list_columns(uniq_list)
    index = int(input('Choose index for Identifier Column: '))-1
    new_list = []
    for item in chosen_column:
        if item == uniq_list[index]:
            new_list.append(True)
        else:
            new_list.append(False)
    df = data[new_list]

def plot_columns(x,y,data):
    a = data[x]
    b = data[y]
    slope, intercept, r_value, p_value, std_err = linregress(a, b)
    plt.scatter(a,b)
    plt.xlabel(x)
    plt.ylabel(y)
    z = np.polyfit(a,b,1)
    p = np.poly1d(z)
    plt.plot(a,p(a),"r--")
    plt.grid(alpha=.4, linestyle='--')
    plt.text(a[-1:],b[-1:],'  r2 = ' + str(round(pow(r_value,2),4)))

### Program Control ###

def normal_run(data):
    list_columns(data)
    plot_columns(column_pick(data),column_pick(data),data)
    plt.show()

def sorted_run(data):
    sorted_df(data)
    plot_columns(column_pick(df),column_pick(df),df)
    plt.show()

### Running Program ###

def run_program():
    mode = int(input('Type 1 for plotting whole column, type 2 for plotting from selection of column: '))
    if mode == 1:
        try:
            excel()
            normal_run(df)
        except Exception as e:
            print(e)
    elif mode == 2:
        try:
            excel()
            sorted_run(df)
        except Exception as e:
            print(e)
    else:
        print('No available mode was chosen - program terminated.')
        pass

run_program()