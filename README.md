# OpenCV Multi-Window Fullscreen Display

In most computer vision projects, you might like to see several windows at the same time. This code allows you to display 9 windows side-by-side. 
Calling the <code>cv2.imshow(_ , _)</code> function multiple times displays the windows on top of each other. This code offers you 2 huge benefits:
1) Replace <code>cv2.imshow('image',img)</code> by <code>Display3x3('image',img,1)</code>. That's it! No additional code is required.
2) The original video will be automatically scaled to fit on your screen while preserving the aspect ratio.

<code>This is a code block.</code>

### Requirements
Python 2 or 3\
`numpy`\
`cv2`\
`tkinter`




### How to start
Run Snake_RL.py to start the game and watch the snake learning.
![image text](https://github.com/akob125/AI-Q-Reinforcement-Learning-Snake/blob/master/Media/Plot.jpg)
![image text](https://github.com/akob125/AI-Q-Reinforcement-Learning-Snake/blob/master/Media/GIF.gif)