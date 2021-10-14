
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
%matplotlib inline
#import sklearn as sk
#from sklearn.datasets import load_sample_image

image = Image.open('C:\cloudxlab\skin_identification\dataverse_files\HAM10000_images_part_1\ISIC_0024306.jpg') 

data = np.asarray(image)
print(type(data))
print(data.shape)
print(data)
plt.imshow(data[:,:,0])


#load_img_rz = np.array(Image.open('C:\cloudxlab\skin_identification\dataverse_files\HAM10000_images_part_1\ISIC_0024306.jpg') .resize((254,254)))
