from PIL import ImageGrab
import time
import os
def screenGrab():
    snap = ImageGrab.grab()
    snap.save(os.getcwd() + "\\john_snap_" +str(int(time.time())) + ".png", "PNG")

if __name__ =='__main__':
    screenGrab()