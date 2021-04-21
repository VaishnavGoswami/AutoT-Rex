from PIL import ImageGrab, ImageOps
import pyautogui
from numpy import*
while True:

    #Construct a small box in front of the dino to read grey scaling
    #'x1' and 'y1' are the co-ordinates for the upper right vertice of the box
    #'a' and 'b' are the length and breath of the box
    x1,y1,a,b= 292,259,94,31
    box = (x1,y1,y1+a,y1+b)
    image = ImageGrab.grab(box)
    gray = ImageOps.grayscale(image)
    a = array(gray.getcolors())
    value = a.sum()
    print(value)
    #Test run the code and replace the "1924" with the continuous output reading given (without obsticle).
    if(value != 1924) :pyautogui.press('space')
    # Re run the code and your dino game should be automated