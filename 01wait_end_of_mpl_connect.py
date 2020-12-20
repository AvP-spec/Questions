# -*- coding: utf-8 -*-
"""
Created on Thu Dec 10 15:30:56 2020

@author: Pipa
quation to canvas.mpl_connect
"""

from matplotlib import pyplot as plt
from matplotlib.widgets import Cursor
from numpy import arange 


Sel_x = []
def main():
    fig = plot_figure_cid(make_data())
    cursor = fig[1] # keeping cursor alive!

    print('main selected x = ', Sel_x)
    fig[0].show()
    print('cursor', cursor)
    #??????????????????????????????????????????????????
    # wait for data selection. How to wait? 
    print('press enter to continue')
    input() 
    
    #return(cursor)

def make_data():     
    notes = 'text'          # later used for file name
    x = arange(0, 100, 1.1) 
    y = ((x-50)*(x-50))
    data = [notes, x, y]
    return (data)

def plot_figure_cid(data):
    plt.ion()
    fig = plt.figure(figsize=(8, 6))
    ax = fig.add_subplot(111, facecolor='#FFFFCC')
    wave, = ax.plot(data[1], data[2], 'bo')
    cursor = Cursor(ax, useblit=True, color='red', linewidth=2)
    fig.canvas.mpl_connect('button_press_event', onclick)
#    fig.canvas.mpl_connect('close_event', fig_closed ) # does not solve the problem

    
    return (fig, cursor)

def onclick(event):
        ######################################################################
    # origenal print function from Matplotlib documantation
    # used for debaging 
#    print('%s click: button=%d, x=%d, y=%d, xdata=%f, ydata=%f' %
#              ('double' if event.dblclick else 'single', event.button,
#               event.x, event.y, event.xdata, event.ydata)) 
    Sel_x.append(event.xdata)
    print('onclik selected x = ', Sel_x)
#    return(Sel_x)