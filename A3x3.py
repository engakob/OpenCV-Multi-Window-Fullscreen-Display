###################################################################
######################   Abdallah Kobresli   ######################
########################   December 2018   ########################
###################################################################

import cv2
import sys
import tkinter as tk
import numpy as np

root = tk.Tk()

screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()


window_width = int (screen_width/3) 
window_height = int( window_width / (screen_width / screen_height) )
 
# DISPLAY MATRIX
# -------------------------------------
# |           |           |           |
# |     1     |     2     |     3     |
# |           |           |           |
# -------------------------------------
# |           |           |           |
# |     4     |     5     |     6     |
# |           |           |           |
# -------------------------------------
# |           |           |           |
# |     7     |     8     |     9     |
# |           |           |           |
# -------------------------------------

WIN_POS = {
    1 : [0,0],
    2 : [window_width,0],
    3 : [window_width * 2,0],
    4 : [0,window_height],
    5 : [window_width,window_height],
    6 : [window_width * 2,window_height],
    7 : [0,window_height *2],
    8 : [window_width ,window_height *2],
    9 : [window_width * 2,window_height *2],

}

def Display3x3(Name,Fr,Position):
    """Name is the name of your window, Fr is the desired Frame to display, Position is (1->9) check the Display Matrix"""

    WinName = str(Name)
    resized_window1 = cv2.resize(Fr, (window_width, window_height))
    
    try:
        POS = WIN_POS[Position]
    except:
        print("*** ERROR Enter a Position Value from 1 -> 9 only. Check Display Matrix ***")
        exit()
    cv2.namedWindow(WinName)
    cv2.moveWindow(WinName, POS[0],POS[1])
    cv2.imshow(WinName, resized_window1)