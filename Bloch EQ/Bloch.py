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