import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import seaborn as sns
from main import *

# basic styling 
sns.set_style("white")

# plottig our dataframe
def plot_class1():
    graph = sns.barplot(data = df.reset_index(), x = 'Labels', y = 'Class 1')
    plt.show()

def plot_class2():
    graph2 = sns.barplot(data = df.reset_index(), x = 'Labels', y = 'Class 2')
    plt.show()

def plot_class3():
    graph3 = sns.barplot(data = df.reset_index(), x = 'Labels', y = 'Class 3')
    plt.show()

# to plot a class select one of 3 functions
# plot_class2()
plot_class2()
