import imageio
from matplotlib import pyplot as plt

class ImageProcessor:
    def load(self, path):
        try:
            img =  imageio.imread(path)
        except FileNotFoundError as fnf:
            print(fnf)
        except ValueError:
            print("Error: '"+path+"' is not and image")
        else:
            return(img[:,:,:3] / 255)
    def display(self, array):
        try:
            img = plt.imshow(array, interpolation='nearest')
            plt.axis("off")
            plt.show()
        except:
            print("Error: Array cannot be interpreted as an image")