import numpy as np
import imageio
from qutip import Bloch
def animate_bloch(vectors, duration=0.1, save_all=False):

    b = Bloch()
    b.vector_color = ['r']
    b.view = [-10,30]
    images=[]
    
    global thetas
    thetas = np.arange(0, 181, 45)
    for a in reversed(np.linspace(0, 1, 4)):
        for theta in thetas:
            b.clear()
            b.add_vectors([np.sin(theta),np.cos(theta),a])
            print(a)
            print(theta)
            if save_all:
                b.save(dirc='tmp') #saving images to tmp directory
                filename="tmp/bloch_%01d.png" % a
            else:
                filename='temp_file.png'
                b.save(filename)
            images.append(imageio.imread(filename))
    imageio.mimsave('bloch_anim.gif', images, duration=duration)


vectors = []
thetas = np.arange(0, 91, 22.5)
for a,theta in zip( np.arange(0, 2, 0.25),thetas):
        vectors.append([np.sin(theta),np.cos(theta),a])
        #print(vectors)

animate_bloch(vectors, duration=0.1, save_all=False)    
