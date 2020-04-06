# MRI Assignement_1
 
| Name | Section |Bench
| ------ | ------ |------|
|Abdullah Ahmed Zahran|2|5|
|Samar Ibrahim|1|40|
|Shymaa Gamal|2|1|
|Sondos Mohamed|1|42|
 

This is a representation for Bloch Equation in 3-D space using Python IDE

The animations below shows the following:

  - M vector with angular frequency 30deg
  - Excitation Mode with angular frequency 30deg
  - Relaxation Mode with angular frequency 30deg
  - Excitation - Relaxation Mode
  - Excitation - Relaxation Trajectory on X-Y plane
  - Relaxation - Excitation Mode
  - Relaxation - Excitation Trajectory on X-Y plane
 

# Bloch Equation Code:
Main Equations for M vector:-
> X = sin(z) * cos(t)

> Y = sin(z) * sin(t)

> Z = cos(z)

where t represents the angle of rotation, z is the angular frequency, by changing z value with respect to t time we have the following representations:

Excitation Model
> z =  pi/2 * sin(t/(4))

Relaxation Model
> z =  pi/2 * cos(t/(4))

Also you can set numberOfLoops = 1 to generate single mode [Excitaion or Relaxation] only or = 2 to generate dual modes.

 ```python
import numpy as np
import imageio
from qutip import Bloch
def animate_bloch(vectors, duration=0.1, save_all=False):
    numberOfLoops = 1 #Enter '1' to apply only ONE mode [Excitation or Relaxation] or '2' to to apply only BOTH modes [Excitation and Relaxation] starting with the selected mode
    if numberOfLoops == 1:
        maxAngle = 2*np.pi
    elif numberOfLoops == 2:
        maxAngle = 4*np.pi
    mode = 1 #Enter '0' to activate Excitation Mode or '1' to activate Relaxation Mode 
    omega = np.pi/6 #Enter the angular frequency 
    z = 0
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
 ---

# Animations in 3-D:

Tho following vectors represents different cases:

- Green: M vector on Relaxation with 0/30deg angular frequency.
- Orange: M vector on Excitation/Relaxation with B.
- Blue: M vector on Excitation with 90deg with Z vector.

**M vector with angular frequency 30deg**

![M vector with angular frequency 30deg](/Bloch%20EQ/GIFs/M%20vector%20with%20angular%20frequency%2030deg.gif)

**Excitation Mode with angular frequency 30deg**

![Excitation Mode with angular frequency 30deg](/Bloch%20EQ/GIFs/Excitation%20Mode%20with%20angular%20frequency%2030deg.gif)

**Relaxation Mode with angular frequency 30deg**

![Relaxation Mode with angular frequency 30deg](/Bloch%20EQ/GIFs/Relaxation%20Mode%20with%20angular%20frequency%2030deg.gif)

---

**Excitaion-Relaxation Mode**
 
![Excitaion-Relaxation Mode](/Bloch%20EQ/GIFs/Excitation-Relaxation%20Mode.gif)

**Excitaion-Relaxation Trajectory**

![Excitaion Relaxation Trajectory](/Bloch%20EQ/GIFs/Excitation-Relaxation%20Trajectory.gif)

**Relaxation-Excitaion Mode**

![Relaxation-Excitaion Mode](/Bloch%20EQ/GIFs/Relaxation%20-%20Excitation%20Mode.gif)

**Relaxation-Excitaion Trajectory**

![Relaxation-Excitaion Trajectory](/Bloch%20EQ/GIFs/Relaxation%20-%20Excitation%20Trajectory.gif)

# Fourrier Code:

Here we use absoulute, angle ,real and imaginary to show each fourier component in Matplot show

``` python
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
# Image And its Fourier Components

**Original Image**

![1](https://user-images.githubusercontent.com/43890895/78510819-4edc0d80-7798-11ea-971a-e93dc3bf3dce.jpg)

**Fourier transform components**

![comp](https://user-images.githubusercontent.com/43890895/78510849-8a76d780-7798-11ea-895d-5629a38e94fc.jpg)

**Gray Beam**
 
![gray_beam](https://user-images.githubusercontent.com/43890895/78510869-a4181f00-7798-11ea-9d93-33ace5797d00.jpg)

**Plot Random Variable**
 
![plot](https://user-images.githubusercontent.com/43890895/78510878-b003e100-7798-11ea-8847-1b8ce6e6b295.jpg)