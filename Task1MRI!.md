# MRI Assignement_1
 
 | Name | sec |Bn Number
| ------ | ------ |------|
|Abdullah Ahmed Zahran|2|5|
|Samar Ibrahim|1|40|
|Shymaa Gamal|2|1|
|Sondos Mohamed|1|42|
 

This is a representation for Bloch Equation in 3-d space using Python IDE

  - Excitation -Relaxation Mode
  - Excitation -Relaxation Trajectory
  - Relaxation-Excitation Mode
  - Relaxation-Excitation Trajectory
 

# Bloch Equation Code:

 ```ruby
 
import numpy as np
import imageio
from qutip import Bloch
def animate_bloch(vectors, duration=0.1, save_all=False):
    numberOfLoops = 2 #Enter '1' to apply only ONE mode [Excitation or Relaxation] or '2' to to apply only BOTH modes [Excitation and Relaxation] starting with the selected mode
    if numberOfLoops == 1:
        maxAngle = 2*np.pi
    elif numberOfLoops == 2:
        maxAngle = 4*np.pi
    mode = 0 #Enter '0' to activate Excitation Mode or '1' to activate Relaxation Mode 
    omega = 0
    z = np.pi/4
    sqAngle = np.pi/2
    a = 5
    vectorM = Bloch()
    # vectorM.view = [90,90] #Activate this line to view magnetization’s trajectory on x-y plane
    images=[]
    for t in np.arange(omega, maxAngle, 0.1):
        if mode == 0:
            z = np.pi/2 * np.sin(t/(4))
            if t == 2*np.pi:
                mode = 1
        elif mode == 1:
            z = np.pi/2 * np.cos(t/(4))
            if t == 2*np.pi:
                mode = 0
        else:
            pass
        vectorM.clear()
        vectorM.add_vectors([np.sin(omega)*np.cos(t), np.sin(omega)*np.sin(t), np.cos(omega)])
        vectorM.add_vectors([np.sin(z)*np.cos(a*t), np.sin(z)*np.sin(a*t), np.cos(z)])
        vectorM.add_vectors([np.sin(sqAngle)*np.cos(t), np.sin(sqAngle)*np.sin(t), np.cos(sqAngle)])
        filename = 'temp_file.png'
        vectorM.save(filename)
        images.append(imageio.imread(filename))
    imageio.mimsave('bloch_anim.gif', images, duration=duration)
vectors = []
animate_bloch(vectors, duration=0.1, save_all=False)
 
 ```
 # Animations in 3-D :
 ![Excitaion-Relaxation Mode](https://raw.githubusercontent.com/Abdolla25/MRI-Task_1/master/Bloch%20EQ/GIFs/Excitation-Relaxation%20Mode.gif?token=AKO3RT3TEDCMH6PFGTGOLNC6SOJRC)
 **Excitaion-Relaxation Mode**
 ![Excitaion Relaxation trajectory](https://raw.githubusercontent.com/Abdolla25/MRI-Task_1/master/Bloch%20EQ/GIFs/Excitation-Relaxation%20Trajectory.gif?token=AKO3RT7BPH7ZYXQF6U5UICC6SOJZA)
 **Excitaion Relaxation trajectory**
 ![](https://raw.githubusercontent.com/Abdolla25/MRI-Task_1/master/Bloch%20EQ/GIFs/Relaxation%20-%20Excitation%20Mode.gif?token=AKO3RT7T5UBASXM2422XB5C6SOJ3W)
 **Relaxation-Excitation Mode**
 ![](https://raw.githubusercontent.com/Abdolla25/MRI-Task_1/master/Bloch%20EQ/GIFs/Relaxation%20-%20Excitation%20Trajectory.gif?token=AKO3RT2HDY4YMXYREVWJEYK6SOJ6I)
 **Relaxation-excitation Trajectory**

# Fourrier Code:
``` ruby

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
```
# Image And its forrier
 
![1](https://user-images.githubusercontent.com/43890895/78510819-4edc0d80-7798-11ea-971a-e93dc3bf3dce.jpg)


![comp](https://user-images.githubusercontent.com/43890895/78510849-8a76d780-7798-11ea-895d-5629a38e94fc.jpg)
**its forrier**

 
 
![gray_beam](https://user-images.githubusercontent.com/43890895/78510869-a4181f00-7798-11ea-9d93-33ace5797d00.jpg)
**gray_beam**

 
![plot](https://user-images.githubusercontent.com/43890895/78510878-b003e100-7798-11ea-8847-1b8ce6e6b295.jpg)
**plot Random Variable**
 
 
 
 
 
 
 
   
