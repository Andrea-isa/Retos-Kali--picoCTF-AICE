from PIL import Image
import numpy as np

img1=np.asarray(Image.open('scrambled1.png'))
img2=np.asarray(Image.open('scrambled2.png'))

print(img1)
print(img2)

datos=img1.copy() + img2.copy()

nueva = Image.fromarray(datos)

nueva.save('nueva.png','PNG')
