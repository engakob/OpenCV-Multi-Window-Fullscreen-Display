# OpenCV Multi-Window Fullscreen Display

In most computer vision projects, you might like to see several windows at the same time. This code allows you to display 9 windows side-by-side. 
Calling the <code>cv2.imshow(_ , _)</code> function multiple times displays the windows on top of each other. This code offers you 2 huge benefits:
1) Replace <code>cv2.imshow('image',img)</code> by <code>Display3x3('image',img,1)</code>. That's it! No additional code is required.
2) The original video will be automatically scaled to fit on your screen while preserving the aspect ratio.

![image text](https://github.com/engakob/OpenCV-Multi-Window-Fullscreen-Display/blob/master/Media/Pic1.jpg)


Low-res Video Sample:
![image text](https://github.com/engakob/OpenCV-Multi-Window-Fullscreen-Display/blob/master/Media/gif.gif)

### Requirements
Python 2 or 3\
`numpy`\
`cv2`\
`tkinter`

### How to start
1) Make sure that you have the A3x3.py file in your working directory
2) Add <code>from A3x3 import *</code>
3) Type <code>Display3x3("image",img,2)</code>, number "2" indicates the window position where you want the window to be.

Check A3x3.py for more info about window positions.