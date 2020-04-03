import numpy as np
import imageio
from qutip import Bloch
def animate_bloch(vectors, duration=0.1, save_all=False):

    b = Bloch()
    b.vector_color = ['r']
    b.view = [-10,30]
    images=[]
    global thetas
    thetas = np.arange(0, 91, 22.5)
    for theta in thetas:    
            b.clear()
            b.add_vectors([np.sin(theta),0,1])
            print(theta)
            if save_all:
                b.save(dirc='tmp') #saving images to tmp directory
                filename="tmp/bloch_%01d.png" % theta
            else:
                filename='temp1_file.png'
                b.save(filename)
            images.append(imageio.imread(filename))
    imageio.mimsave('bloch1_anim.gif', images, duration=duration)


vectors = []
for theta in thetas:
    vectors.append([np.sin(theta),0,1])
    print(vectors)
animate_bloch(vectors, duration=0.1, save_all=False)    