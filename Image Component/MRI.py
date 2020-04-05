###########################################################################################################################################
# Project : Task 1
# File Name: MRI..py
# Description: Bloch Equation Simulation
# Author: Team ---
########################################################################################################################################





import numpy as np
from cv2 import cv2 as cv
import matplotlib.pyplot as p
from numpy import random
def main ():
    img=cv.imread('1.jpg',0)
    spectrum =np.fft.fftshift(np.fft.fft2(img))
    p.subplot(321)
    p.imshow(img, cmap='gray')
    p.title('input image') 
    p.subplot(322)
    p.imshow( np.log(np.abs(spectrum)) , cmap='gray')
    p.title('Magnitude Spectrum') 
    p.subplot(323)
    p.imshow(np.angle(spectrum),cmap='gray')
    p.title('Phase Spectrum') 
    p.subplot(324)
    p.imshow(np.real(spectrum),cmap='gray')
    p.title('real Spectrum') 
    p.subplot(325)
    p.imshow(  np.imag(spectrum),cmap='gray')
    p.title('imaginary Spectrum') 
    p.show()
############################################   Plot Random Variable     ################################################################
    z = random.random(200)
    p.ylabel("Z axis")
    p.xlabel("Time")
    p.plot(z)
    p.show()
    
if __name__=="__main__":
    main()